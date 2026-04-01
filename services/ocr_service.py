"""
OCR サービス
インターフェースを定義し、デフォルトはモック実装。
将来: Google Vision API / Tesseract / マルチモーダル LLM に差し替え可能。
"""
from abc import ABC, abstractmethod
from typing import Optional
import io
from PIL import Image


class OcrService(ABC):
    """OCR サービスのインターフェース"""

    @abstractmethod
    def extract_text(self, image_bytes: bytes) -> str:
        """画像からテキストを抽出して返す"""
        ...


class MockOcrService(OcrService):
    """
    MOCK: 実際の OCR は行わず、画像サイズに基づいてダミーテキストを返す。
    将来: 実装を差しみえるだけで動作する。
    """

    def extract_text(self, image_bytes: bytes) -> str:
        try:
            img = Image.open(io.BytesIO(image_bytes))
            width, height = img.size
            # 画像サイズで疑似的に異なるテキストを返す (MOCK)
            seed = (width * height) % len(_MOCK_TEXTS)
            return _MOCK_TEXTS[seed]
        except Exception:
            return ""


# MOCK: ダミー OCR テキストのバリエーション
_MOCK_TEXTS = [
    "Canon EOS Kiss X7 18-55mm Kit",
    "Nikon D5300 AF-P DX",
    "Nikon D7100 Body",
    "Canon EOS 5D Mark IV",
    "Nikon D3300 Red",
    "Canon EF 50mm F1.8 STM",
    "Nikon AF-S DX 35mm f/1.8G",
    "TAMRON 28-75mm F2.8",
    "",  # 読み取り失敗ケース
]
