from fastapi import APIRouter
from services.evaluator import Evaluator
from models.schemas import EvaluateRequest, EvaluationResult

router = APIRouter()
evaluator = Evaluator()

@router.post("/evaluate", response_model=EvaluationResult)
async def evaluate(req: EvaluateRequest):
    return evaluator.evaluate(req)
