from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    user_id: int
    departure_date: datetime
    destination: str
    seat_class: str
