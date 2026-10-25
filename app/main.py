from fastapi import FastAPI

app = FastAPI(
    title="QuickStock API",
    description="Inventory management for quick-commerce operations.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}