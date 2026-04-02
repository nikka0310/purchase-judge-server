from fastapi import APIRouter, UploadFile, File, HTTPException
from services.ocr_service import MockOcrService
from services.product_matcher import ProductMatcher
from models.schemas import AnalyzeResponse

router = APIRouter()
ocr_service = MockOcrService()
matcher = ProductMatcher()
CONFIDENCE_WARNING_THRESHOLD = 0.50

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_image(image: UploadFile = File(...)):
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="画像ファイルを送信してください")
    image_bytes = await image.read()
    if len(image_bytes) == 0:
        raise HTTPException(status_code=400, detail="空の画像ファイルです")
    ocr_text = ocr_service.extract_text(image_bytes)
    candidates = matcher.match(ocr_text, top_k=3)
    warning = None
    if candidates and candidates[0].confidence < CONFIDENCE_WARNING_THRESHOLD:
        warning = "精度が低いため、型番ロゴの追加撮影をおすすめします。値札や型番部分のアップがあると精度が上がります。"
    return AnalyzeResponse(candidates=candidates, ocr_text=ocr_text, warning=warning)
