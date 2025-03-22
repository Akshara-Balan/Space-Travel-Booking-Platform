from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    departure_date = Column(DateTime)
    destination = Column(String)
    seat_class = Column(String)

    user = relationship("User", back_populates="bookings")
