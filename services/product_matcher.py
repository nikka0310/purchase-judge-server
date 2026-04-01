"""
商品候補推定サービス
OCR テキストをルールベースでマッチングし、候補を返す。
"""
import random
from typing import List
from data.products import SAMPLE_PRODUCTS
from models.schemas import ProductCandidate


class ProductMatcher:
    """
    OCR テキストから商品候補を推定する。
    現在実装: キーワードマッチング + スコアリング
    """

    def match(self, ocr_text: str, top_k: int = 3) -> List[ProductCandidate]:
        text_lower = ocr_text.lower()
        scored: List[tuple] = []

        for product in SAMPLE_PRODUCTS:
            score = self._score(text_lower, product["keywords"])
            if score > 0:
                scored.append((score, product))

        # スコア降順でソート
        scored.sort(key=lambda x: x[0], reverse=True)

        # OCR テキストが空 or マッチなし → ランダムに候補を返す (MOCK フォールバック)
        if not scored:
            return self._mock_fallback(top_k)

        candidates = []
        max_score = scored[0][0] if scored else 1
        for score, product in scored[:top_k]:
            confidence = min(score / max_score, 1.0)
            # ランダム揺らぎを加える (MOCK)
            confidence = min(1.0, confidence * random.uniform(0.75, 1.0))
            candidates.append(
                ProductCandidate(
                    id=product["id"],
                    name=product["name"],
                    brand=product["brand"],
                    model=product["model"],
                    category=product["category"],
                    confidence=round(confidence, 2),
                )
            )

        return candidates

    def _score(self, text: str, keywords: List[str]) -> float:
        if not text:
            return 0.0
        hit = sum(1 for kw in keywords if kw in text)
        return hit / len(keywords) if keywords else 0.0

    def _mock_fallback(self, top_k: int) -> List[ProductCandidate]:
        """OCR が空の場合のフォールバック (MOCK)"""
        pool = random.sample(SAMPLE_PRODUCTS, min(top_k, len(SAMPLE_PRODUCTS)))
        candidates = []
        for i, product in enumerate(pool):
            # 順位が下きるほど信頼度を下げる
            confidence = round(random.uniform(0.25, 0.45) - i * 0.05, 2)
            confidence = max(0.05, confidence)
            candidates.append(
                ProductCandidate(
                    id=product["id"],
                    name=product["name"],
                    brand=product["brand"],
                    model=product["model"],
                    category=product["category"],
                    confidence=confidence,
                )
            )
        return candidates
