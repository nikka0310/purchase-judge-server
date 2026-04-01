import sys
import os

# routers / services が同じパッケージとして import できるようにする
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import analyze, market, evaluate

app = FastAPI(
    title="仕入れ判断 API",
    description="写真 1 枚から商品候補を推定し、仕入れ判断を返す MVP API",
    version="0.1.0",
)

# Flutter ローカル開発用 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(analyze.router)
app.include_router(market.router)
app.include_router(evaluate.router)


@app.get("/health")
async def health():
    return {"status": "ok", "version": "0.1.0"}
