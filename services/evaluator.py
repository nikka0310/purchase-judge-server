"""
利益計算・仕入れ判定サービス
実ロジックを実装。
"""
from models.schemas import EvaluateRequest, EvaluationResult

MERCARI_FEE_RATE = 0.10


class Evaluator:
    def evaluate(self, req: EvaluateRequest) -> EvaluationResult:
        sold_median = req.sold_median
        shipping = req.shipping_estimate
        purchase = req.purchase_price
        desired_profit = req.desired_profit

        # メルカリ手数料
        mercari_fee = int(sold_median * MERCARI_FEE_RATE)

        # 受取額 = 売値 × 0.90 - 送料
        net_receive = int(sold_median * (1 - MERCARI_FEE_RATE)) - shipping

        # 想定利益 = 売値 - (売値 × 0.10) - 送料 - 仕入れ価格
        estimated_profit = net_receive - purchase

        # 安全仕入れ上限 = 売り切れ中央値 × 0.85 - 送料 - 希望利益
        safe_purchase_limit = int(sold_median * 0.85) - shipping - desired_profit

        # 判定
        if purchase <= safe_purchase_limit:
            verdict = "仕入れ候補"
            verdict_color = "green"
        elif estimated_profit > 0:
            verdict = "薄利"
            verdict_color = "yellow"
        else:
            verdict = "見送り"
            verdict_color = "red"

        return EvaluationResult(
            mercari_fee=mercari_fee,
            net_receive=net_receive,
            estimated_profit=estimated_profit,
            safe_purchase_limit=safe_purchase_limit,
            verdict=verdict,
            verdict_color=verdict_color,
        )
