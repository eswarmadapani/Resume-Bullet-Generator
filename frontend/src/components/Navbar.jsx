import { useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();

  return (
    <nav className="w-full bg-black/90 backdrop-blur-md border-b border-white/10 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        
        <div className="flex items-center gap-3">
          

          <h1
            className="text-white font-semibold text-lg tracking-wide cursor-pointer hover:text-gray-200 transition-colors"
            onClick={() => navigate("/")}
          >
            AnalyzeAI
          </h1>
        </div>

        <button
          className="bg-white text-black px-5 py-2 rounded-xl text-sm font-semibold hover:bg-gray-100 active:scale-[0.98] transition-all"
          onClick={() => navigate("/analyze")}
        >
          Get started
        </button>
      </div>
    </nav>
  );
}

export default Navbar;
