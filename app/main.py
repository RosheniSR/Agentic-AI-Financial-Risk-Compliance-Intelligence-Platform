from fastapi import FastAPI

# Import routes
from app.routes import fraud, agent, health
from app.routes.compliance_routes import router as compliance_router
from app.routes.upload_routes import router as upload_router


# Create FastAPI app
app = FastAPI(title="AI Fintech Risk Platform")


# -------------------------------
# ROUTERS (WITH PREFIXES ✅)
# -------------------------------
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(fraud.router, prefix="/fraud", tags=["Fraud"])
app.include_router(agent.router, prefix="/agent", tags=["Agent"])

app.include_router(compliance_router, prefix="/compliance", tags=["Compliance"])
app.include_router(upload_router, prefix="/upload", tags=["Upload"])


# -------------------------------
# ROOT ENDPOINT
# -------------------------------
@app.get("/")
def root():
    return {"message": "AI Fintech Platform is running"}