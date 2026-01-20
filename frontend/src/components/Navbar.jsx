function Navbar() {
  return (
    <nav className="w-full bg-black border-t-4 border-blue-500">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex justify-between items-center">
        <div className="flex items-center gap-2 -ml-2">
          <h1 className="text-white font-semibold text-lg">AnalyzeAI</h1>
        </div>
        <button className="!bg-white text-black px-4 py-1.5 rounded-md text-sm font-medium hover:!bg-gray-100 transition-colors">
          Get started
        </button>
      </div>
    </nav>
  );
}

export default Navbar;
