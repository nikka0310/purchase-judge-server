from fastapi import APIRouter
from services.market_provider import MockMercariMarketDataProvider
from models.schemas import MarketLookupRequest, MarketLookupResponse

router = APIRouter()
market_provider = MockMercariMarketDataProvider()

@router.post("/market/lookup", response_model=MarketLookupResponse)
async def lookup_market(req: MarketLookupRequest):
    market_data = market_provider.get_market_data(req.product_id, req.product_name)
    return MarketLookupResponse(market_data=market_data, is_mock=True)
