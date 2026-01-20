// API service functions
import axios from 'axios';

// Use environment variable or fallback to localhost
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5173';

export const analyzeResume = async (resumeFile, jobDescription) => {
    const formData = new FormData();

    formData.append('resume', resumeFile);
    formData.append('job_description', jobDescription);

    const response = await axios.post(
        `${API_URL}/api/analyze`,
        formData,
    );
    return response.data;
}
