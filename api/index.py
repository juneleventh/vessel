from fastapi import FastAPI, request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="JSON read")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post('/')
async def vessel(request:Request):
    body = await request.json
    metrics = {
  {
    "regions": "apac",
    "avg_latency": "171.3825",
    "p95_latency": "209.5625",
    "avg_uptime ": "98.42858333",
    "breaches": "8"
  },
  {
    "regions": "emea",
    "avg_latency": "173.6325",
    "p95_latency": "210.3925",
    "avg_uptime ": "98.52191667",
    "breaches": "8"
  }
    }
    return metrics

