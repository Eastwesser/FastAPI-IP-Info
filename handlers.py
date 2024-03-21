from fastapi import APIRouter, Form, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_info_by_ip(ip_address) -> dict:
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch IP information"}

@router.post("/process_ip", response_class=HTMLResponse)
async def process_ip(ip_address: str = Form(...), request: Request = Request):
    ip_info = get_info_by_ip(ip_address)
    return templates.TemplateResponse("index.html", {"request": request, "ip_info": ip_info})