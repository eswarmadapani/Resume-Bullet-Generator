// API service functions
import axios from 'axios';

export const analyzeResume = async (resumeFile, jobDescription) => {
    const formData = new FormData();

    formData.append('resume', resumeFile);
    formData.append('job_description', jobDescription);

    const response = await axios.post(
        "http://localhost:8000/api/analyze",
        formData,
    );
    return response.data;
}
