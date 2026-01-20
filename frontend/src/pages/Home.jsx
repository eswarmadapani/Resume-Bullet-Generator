import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-white">
      <Navbar />
      <Hero onTry={() => navigate("/analyze")} />
    </div>
  );
}

export default Home;
