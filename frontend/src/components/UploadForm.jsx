import { useState } from "react";

function UploadForm({ onAnalyze }) {
  const [jobDescription, setJobDescription] = useState("");
  const [resumeFile, setResumeFile] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!jobDescription || !resumeFile) return;

    onAnalyze(resumeFile, jobDescription);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="border rounded-lg p-6"
    >
      <h2 className="text-xl font-semibold mb-4">
        Upload Resume & Job Description
      </h2>

      <textarea
        className="w-full border rounded-md p-3 h-40 mb-4"
        placeholder="Paste job description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

      <input
        type="file"
        accept=".pdf,.docx"
        className="mb-4"
        onChange={(e) => setResumeFile(e.target.files[0])}
      />

      <button
        type="submit"
        disabled={!jobDescription || !resumeFile}
        className="bg-black text-white px-6 py-2 rounded-md disabled:opacity-50"
      >
        Analyze
      </button>
    </form>
  );
}

export default UploadForm;
