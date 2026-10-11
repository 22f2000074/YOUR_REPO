from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 212.21,
    "uptime_pct": 99.242,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 198.78,
    "uptime_pct": 97.906,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 107.74,
    "uptime_pct": 97.403,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 202.71,
    "uptime_pct": 97.97,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 187.47,
    "uptime_pct": 97.289,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 145.16,
    "uptime_pct": 98.647,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 219.08,
    "uptime_pct": 98.646,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 132.51,
    "uptime_pct": 97.914,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 147.16,
    "uptime_pct": 98.629,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 216.2,
    "uptime_pct": 98.674,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 153.96,
    "uptime_pct": 98.894,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 131.23,
    "uptime_pct": 97.34,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 144.68,
    "uptime_pct": 97.11,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 127.19,
    "uptime_pct": 98.164,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 178.65,
    "uptime_pct": 97.338,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 178.63,
    "uptime_pct": 99.021,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 230.38,
    "uptime_pct": 99.498,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 114.54,
    "uptime_pct": 99.146,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 140.29,
    "uptime_pct": 99.222,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 215.91,
    "uptime_pct": 97.889,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 210.9,
    "uptime_pct": 97.143,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 205.53,
    "uptime_pct": 97.62,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 139.35,
    "uptime_pct": 97.539,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 121.79,
    "uptime_pct": 97.431,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 145.72,
    "uptime_pct": 98.771,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 166.39,
    "uptime_pct": 98.172,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 107.02,
    "uptime_pct": 99.015,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 193.11,
    "uptime_pct": 97.386,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 229.79,
    "uptime_pct": 97.126,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 159.02,
    "uptime_pct": 98.227,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 129.22,
    "uptime_pct": 97.563,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 165.3,
    "uptime_pct": 98.585,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 190.48,
    "uptime_pct": 98.694,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 101.55,
    "uptime_pct": 98.424,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 223.29,
    "uptime_pct": 99.147,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 120.29,
    "uptime_pct": 99.239,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
