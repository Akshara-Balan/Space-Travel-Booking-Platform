from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.booking import Booking
from app.schemas.booking import BookingCreate

router = APIRouter()

@router.post("/")
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    new_booking = Booking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking
