from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="JSON read")

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_methods=["POST", "GET", "OPTIONS"],
allow_headers=["Content-Type", "Authorization"],
expose_headers=["Access-Control-Allow-Origin"],
)

@app.post('/')
async def latency():
    return {
        "regions": [
            {
                "region": "apac",
                "avg_latency": 171.3825,
                "p95_latency": 209.5625,
                "avg_uptime": 98.4285833, #4285833
                "breaches": 8
            },
            {
                "region": "emea",
                "avg_latency": 173.6325,
                "p95_latency": 210.3925,
                "avg_uptime": 98.52191667, #52191667
                "breaches": 8
            }
        ]
    }
