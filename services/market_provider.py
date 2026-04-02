"""
相場データプロバイダー
インターフェース定義 + MockMercariMarketDataProvider デフォルト実装。
"""
from abc import ABC, abstractmethod
from models.schemas import MarketData


class MarketDataProvider(ABC):
    @abstractmethod
    def get_market_data(self, product_id: str, product_name: str) -> MarketData:
        ...


class MockMercariMarketDataProvider(MarketDataProvider):
    _MOCK_DATA: dict = {
        "canon_kiss_x7": {"sold_median": 22000, "sold_min": 14000, "sold_max": 32000, "active_median": 25000, "shipping_estimate": 1000, "sample_count": 47},
        "nikon_d5300": {"sold_median": 25000, "sold_min": 17000, "sold_max": 38000, "active_median": 28000, "shipping_estimate": 1200, "sample_count": 62},
        "nikon_d7100": {"sold_median": 30000, "sold_min": 20000, "sold_max": 45000, "active_median": 33000, "shipping_estimate": 1200, "sample_count": 38},
        "canon_5d4": {"sold_median": 180000, "sold_min": 140000, "sold_max": 220000, "active_median": 195000, "shipping_estimate": 1500, "sample_count": 29},
        "nikon_d3300_red": {"sold_median": 18000, "sold_min": 10000, "sold_max": 28000, "active_median": 20000, "shipping_estimate": 1000, "sample_count": 55},
        "canon_ef50": {"sold_median": 12000, "sold_min": 8000, "sold_max": 18000, "active_median": 13500, "shipping_estimate": 600, "sample_count": 120},
        "nikon_35dx": {"sold_median": 11000, "sold_min": 7000, "sold_max": 16000, "active_median": 12000, "shipping_estimate": 600, "sample_count": 98},
        "tamron_2875": {"sold_median": 48000, "sold_min": 35000, "sold_max": 65000, "active_median": 52000, "shipping_estimate": 800, "sample_count": 74},
    }
    _DEFAULT = {"sold_median": 15000, "sold_min": 8000, "sold_max": 25000, "active_median": 17000, "shipping_estimate": 1000, "sample_count": 10}

    def get_market_data(self, product_id: str, product_name: str) -> MarketData:
        data = self._MOCK_DATA.get(product_id, self._DEFAULT)
        return MarketData(
            product_id=product_id,
            sold_median=data["sold_median"],
            sold_min=data["sold_min"],
            sold_max=data["sold_max"],
            active_median=data["active_median"],
            shipping_estimate=data["shipping_estimate"],
            sample_count=data["sample_count"],
            note="MOCK DATA - メルカリ公開 API 非使用",
        )
