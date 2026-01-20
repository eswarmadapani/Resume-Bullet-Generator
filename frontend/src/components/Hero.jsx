function Hero({ onTry }) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[calc(100vh-200px)] px-4 py-20">
      <div className="text-center">
        <h1 className="text-5xl sm:text-6xl font-bold text-gray-900 mb-4">
          AnalyzeAI
        </h1>
        <p className="text-gray-600 text-base sm:text-lg mb-8">
          Analyze your resume for the better
        </p>

        <button
          onClick={onTry}
          className="bg-black text-white px-6 py-2 rounded-md text-sm font-medium hover:bg-gray-800 transition-colors"
        >
          Try It
        </button>
      </div>
    </div>
  );
}

export default Hero;
