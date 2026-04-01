from pydantic import BaseModel, Field
from typing import List, Optional


# ── 商品候補 ─────────────────────────────────────────────
class ProductCandidate(BaseModel):
    id: str
    name: str
    brand: str
    model: str
    category: str
    confidence: float = Field(..., ge=0.0, le=1.0, description="信頼度 0.0〜1.0")


# ── /analyze レスポンス ──────────────────────────────────
class AnalyzeResponse(BaseModel):
    candidates: List[ProductCandidate]
    ocr_text: str = ""  # デバッグ用 OCR テキスト (MOCK)
    warning: Optional[str] = None


# ── /market/lookup ───────────────────────────────────────
class MarketLookupRequest(BaseModel):
    product_id: str
    product_name: str


class MarketData(BaseModel):
    product_id: str
    sold_median: int
    sold_min: int
    sold_max: int
    active_median: int
    shipping_estimate: int
    sample_count: int
    note: str = ""  # MOCK データであることを示すフラグ


class MarketLookupResponse(BaseModel):
    market_data: MarketData
    is_mock: bool = True  # MOCK であることを明示


# ── /evaluate ────────────────────────────────────────────
class EvaluateRequest(BaseModel):
    sold_median: int = Field(..., description="売り切れ中央値")
    shipping_estimate: int = Field(..., description="送料目安")
    purchase_price: int = Field(..., description="仕入れ価格")
    desired_profit: int = Field(0, description="希望利益")


class EvaluationResult(BaseModel):
    mercari_fee: int
    net_receive: int           # 受取額 = 売値 × 0.90 - 送料
    estimated_profit: int      # 想定利益
    safe_purchase_limit: int   # 安全仕入れ上限
    verdict: str               # "仕入れ候補" | "薄利" | "見送り"
    verdict_color: str         # "green" | "yellow" | "red"
