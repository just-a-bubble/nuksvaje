from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from weather import get_current_weather, get_forecast
from db import save_last_city, get_last_cities

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    last_cities = get_last_cities()
    return templates.TemplateResponse("index.html", {"request": request, "last_cities": last_cities})

@app.get("/api/current")
def current(city: str):
    save_last_city(city)
    return get_current_weather(city)

@app.get("/api/forecast")
def forecast(city: str):
    save_last_city(city)
    return get_forecast(city)

@app.get("/api/last-cities")
def last_cities():
    return get_last_cities()
