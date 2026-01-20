import { useState } from "react";
import Navbar from "../components/Navbar";
import UploadForm from "../components/UploadForm";
import Results from "../components/Results";
import { analyzeResume } from "../services/api";

function Analyze() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleAnalyze = async (resumeFile, jobDescription) => {
    try {
      setLoading(true);
      setError("");
      setResult(null);

      const data = await analyzeResume(resumeFile, jobDescription);
      setResult(data);
    } catch {
      setError("Failed to analyze resume. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Navbar />

      <div className="max-w-4xl mx-auto mt-10 px-4">
        <UploadForm onAnalyze={handleAnalyze} />

        {loading && (
          <p className="text-center mt-6 text-gray-500">
            Analyzing resume...
          </p>
        )}

        {error && (
          <p className="text-center mt-6 text-red-500">
            {error}
          </p>
        )}

        {result && <Results data={result} />}
      </div>
    </>
  );
}

export default Analyze;
