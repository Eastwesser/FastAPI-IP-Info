from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from handlers import router as handlers_router

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(handlers_router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# python -m uvicorn main:app --reload
