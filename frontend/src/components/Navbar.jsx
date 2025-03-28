import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-gray-900 text-white p-4 flex justify-between">
      <h1 className="text-xl font-bold">Space Travel</h1>
      <div>
        <Link to="/" className="mr-4">Home</Link>
        <Link to="/booking">Book Trip</Link>
      </div>
    </nav>
  );
};

export default Navbar;
