from fastapi import FastAPI
from app.api.routes import booking, users, pricing, recommendations
from app.core.database import create_tables

app = FastAPI(title="Space Travel Booking API")

# Include API routes
app.include_router(booking.router, prefix="/booking", tags=["Booking"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(pricing.router, prefix="/pricing", tags=["Pricing"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])

@app.on_event("startup")
def startup():
    create_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to Space Travel Booking API"}
