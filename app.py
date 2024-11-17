from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers import users, permissions, ml
from database import engine, Base

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Include routers
app.include_router(users.router)
app.include_router(permissions.router)
app.include_router(ml.router)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend's domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# Ensure all tables are created at startup
@app.on_event("startup")
async def startup_event():
    logger.info("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Tables created!")
