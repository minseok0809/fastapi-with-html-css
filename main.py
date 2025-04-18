import uvicorn
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
templates = Jinja2Templates(directory="./")
app.mount("/static", StaticFiles(directory="./"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("./index.html", {"request": request})

@app.get("/event", response_class=HTMLResponse)
async def read_event(request: Request):
    return templates.TemplateResponse("./pencil_co/event_overview.html", {"request": request})

@app.get("/event_1", response_class=HTMLResponse)
async def event_1(request: Request):
    return templates.TemplateResponse("./pencil_co/event_1.html", {"request": request})

@app.get("/event_2", response_class=HTMLResponse)
async def event_2(request: Request):
    return templates.TemplateResponse("./pencil_co/event_2.html", {"request": request})

@app.get("/goods", response_class=HTMLResponse)
async def goods(request: Request):
    return templates.TemplateResponse("./pencil_co/good_overviews.html", {"request": request})

@app.get("/goods_1", response_class=HTMLResponse)
async def goods_1(request: Request):
    return templates.TemplateResponse("./pencil_co/goods_1.html", {"request": request})

@app.get("/goods_2", response_class=HTMLResponse)
async def goods_2(request: Request):
    return templates.TemplateResponse("./pencil_co/goods_2.html", {"request": request})

@app.get("/goods_3", response_class=HTMLResponse)
async def goods_3(request: Request):
    return templates.TemplateResponse("./pencil_co/goods_3.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("./pencil_co/Contact.html", {"request": request})

@app.get("/image")
async def main():
    return FileResponse("./pencil_co/picture/pecil.png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
