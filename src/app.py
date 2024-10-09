import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
import httpx

from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from src.config import settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.remove()
    logger.add(sys.stderr, level=settings.log_lvl)

    logger.info("🚀 Starting application")

    yield

    logger.info("⛔ Stopping application")


app = FastAPI(title="converter", root_path="/api", lifespan=lifespan)



@logger.catch
@app.get("/v1/convert")
async def convert_currency(amount: float, from_currency: str, to_currency: str):
    url = f"{settings.EXTERNAL_API_URL}?from={from_currency}&to={to_currency}&amount={amount}&api_key={settings.API_KEY}"
    print(f"Request URL: {url}")

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code != 200:
            print(f"Error response: {response.text}")
            logger.error("Error fetching currency data")
            raise HTTPException(
                status_code=response.status_code, detail="Error fetching currency data"
            )

        data = response.json()

        if "result" not in data:
            print(f"Error details: {data}")
            logger.error("Invalid response structure")
            raise HTTPException(status_code=400, detail="Invalid response structure")

        converted_amount = data["result"].get(to_currency)
        if converted_amount is None:
            logger.error("Currency not found")
            raise HTTPException(status_code=400, detail="Currency not found")

        rate = data["result"].get("rate")

        return {
            "result": converted_amount,
        }


# Cors
origins = [
    "http://localhost",
    "http://localhost:8100",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)
