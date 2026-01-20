import bgImage from '../assets/download (2).jpg';

function Hero({ onTry }) {
  return (
    <div className="isolate relative flex flex-col items-center justify-center min-h-screen px-4 py-20 overflow-hidden">
      
      {/* Background Image */}
      <div className="absolute inset-0 -z-10">
        <img 
          src={bgImage}
          alt="Background" 
          className="w-full h-full object-cover"
        />
        {/* Dark overlay for better text readability */}
        <div className="absolute inset-0 bg-black/40" />
      </div>

      <div className="text-center max-w-2xl">
        {/* Transparent badge */}
        <p className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-white/30 bg-white/20 backdrop-blur-md text-xs font-medium text-white mb-6 shadow-lg">
          ⚡ ATS Resume Analyzer + Keyword Match
        </p>

        {/* Transparent title */}
        <h1 className="text-5xl sm:text-6xl font-extrabold text-white mb-4 tracking-tight drop-shadow-2xl">
          Analyze<span className="text-white/90">AI</span>
        </h1>

        {/* Transparent description */}
        <p className="text-white/90 text-base sm:text-lg mb-10 leading-relaxed drop-shadow-lg">
          Upload your resume, paste the job description, and get an instant ATS score with missing keyword insights.
        </p>

        {/* Glassmorphic button */}
        <button
          onClick={onTry}
          className="bg-white/20 backdrop-blur-md border border-white/30 text-white px-7 py-2.5 rounded-xl text-sm font-semibold shadow-lg hover:shadow-xl hover:bg-white/30 active:scale-[0.98] transition-all"
        >
          Try It →
        </button>
      </div>
    </div>
  );
}

export default Hero;
