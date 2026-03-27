from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# ---- Model ----
class User(BaseModel):
    name: str
    email: EmailStr
    age: int


# ---- Fake DB ----
users_db = []


# ---- Routes ----

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit", response_class=HTMLResponse)
def submit_form(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    age: int = Form(...)
):
    user = User(name=name, email=email, age=age)
    users_db.append(user)

    return templates.TemplateResponse(
        "success.html",
        {"request": request, "user": user}
    )


@app.get("/users")
def get_users():
    return users_db