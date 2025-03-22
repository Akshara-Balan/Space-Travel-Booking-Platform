import { useState } from "react";
import axios from "axios";

const Booking = () => {
  const [bookingData, setBookingData] = useState({
    user_id: 1,
    departure_date: "",
    destination: "",
    seat_class: "Economy",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post("http://127.0.0.1:8000/booking", bookingData);
    alert("Booking Confirmed: " + response.data.id);
  };

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Book Your Space Trip</h1>
      <form onSubmit={handleSubmit}>
        <input type="date" onChange={(e) => setBookingData({ ...bookingData, departure_date: e.target.value })} required />
        <input type="text" placeholder="Destination" onChange={(e) => setBookingData({ ...bookingData, destination: e.target.value })} required />
        <select onChange={(e) => setBookingData({ ...bookingData, seat_class: e.target.value })}>
          <option>Economy</option>
          <option>Business</option>
          <option>VIP</option>
        </select>
        <button type="submit" className="bg-blue-500 text-white px-4 py-2">Book Now</button>
      </form>
    </div>
  );
};

export default Booking;
