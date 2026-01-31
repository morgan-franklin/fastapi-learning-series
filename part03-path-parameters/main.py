from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Morgan Franklin",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "January 29, 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "January 29, 2026",
    },  {
        "id": 3,
        "author": "John Smith",
        "title": "Python is Great for QA Testing",
        "content": "Python is a great language for QA testing, and FastAPI makes it even better.",
        "date_posted": "January 29, 2026",
    }
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts",  include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title":"Home"})
    
@app.get("/api/posts")
def get_posts():
    return posts