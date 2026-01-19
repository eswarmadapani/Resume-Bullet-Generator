from fastapi import FastAPI
from dotenv import load_dotenv
from app.config import setup_cors
from app.routes.analyze import router as  analyze_router

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Resume Bullet Generator",
    description="API for generating resume bullets",
    version="1.0.0"
)

setup_cors(app)
app.include_router(analyze_router,prefix="/api")
@app.get('/')
def read_root():
    return {"message": "Server is running"}
