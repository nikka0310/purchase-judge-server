# サンプル商品辞書 (MOCK DATA)
# 将来: DB / 外部APIに差し替え可能

from typing import List, Dict, Any

SAMPLE_PRODUCTS: List[Dict[str, Any]] = [
    {
        "id": "canon_kiss_x7",
        "name": "Canon EOS Kiss X7 ボディ",
        "brand": "Canon",
        "model": "EOS Kiss X7",
        "category": "一眼レフ",
        "keywords": ["kiss", "x7", "canon", "eos", "kiss x7"],
    },
    {
        "id": "nikon_d5300",
        "name": "Nikon D5300 ボディ",
        "brand": "Nikon",
        "model": "D5300",
        "category": "一眼レフ",
        "keywords": ["d5300", "nikon", "5300"],
    },
    {
        "id": "nikon_d7100",
        "name": "Nikon D7100 ボディ",
        "brand": "Nikon",
        "model": "D7100",
        "category": "一眼レフ",
        "keywords": ["d7100", "nikon", "7100"],
    },
    {
        "id": "canon_5d4",
        "name": "Canon EOS 5D Mark IV ボディ",
        "brand": "Canon",
        "model": "EOS 5D Mark IV",
        "category": "一眼レフ",
        "keywords": ["5d", "5d4", "mark iv", "canon", "mark4"],
    },
    {
        "id": "nikon_d3300_red",
        "name": "Nikon D3300 レッド",
        "brand": "Nikon",
        "model": "D3300",
        "category": "一眼レフ",
        "keywords": ["d3300", "nikon", "3300", "red", "レッド"],
    },
    {
        "id": "canon_ef50",
        "name": "Canon EF 50mm F1.8 STM",
        "brand": "Canon",
        "model": "EF 50mm F1.8 STM",
        "category": "レンズ",
        "keywords": ["50mm", "f1.8", "stm", "canon", "ef50"],
    },
    {
        "id": "nikon_35dx",
        "name": "Nikon AF-S DX 35mm f/1.8G",
        "brand": "Nikon",
        "model": "AF-S DX 35mm f/1.8G",
        "category": "レンズ",
        "keywords": ["35mm", "f1.8", "dx", "nikon", "af-s"],
    },
    {
        "id": "tamron_2875",
        "name": "TAMRON 28-75mm F/2.8 Di III RXD",
        "brand": "TAMRON",
        "model": "28-75mm F/2.8 Di III RXD",
        "category": "レンズ",
        "keywords": ["28-75", "tamron", "2875", "f2.8", "di iii"],
    },
]

# 商品IDでのルックアップ用
PRODUCTS_BY_ID: Dict[str, Dict[str, Any]] = {p["id"]: p for p in SAMPLE_PRODUCTS}
