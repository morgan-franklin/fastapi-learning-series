# Part 2: HTML Frontend - Jinja2 Templates

## Video Info
**Duration:** 37:26  
**Completed:** January 30, 2026 ✅

## What I Built

HTML frontend using Jinja2 templates with static file serving.

**Files Created:**
```
part02-html-frontend/
├── main.py
├── templates/
│   ├── base.html
│   ├── home.html
│   └── about.html
└── static/css/main.css
```

## Running This Code
```bash
cd part02-html-frontend
uvicorn main:app --reload
# Visit: http://localhost:8000
```

## Key Learnings

- ✅ Jinja2 template engine setup
- ✅ Template inheritance with `{% extends %}`
- ✅ Static file serving
- ✅ Passing data to templates
- ✅ Template variables `{{ variable }}`
- ✅ Loops `{% for item in list %}`

## Code Highlights

**Setup:**
```python
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
```

**Render Template:**
```python
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "posts": posts}
    )
```

**Template (home.html):**
```html
{% extends "base.html" %}

{% block content %}
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
{% endfor %}
{% endblock %}
```

## My Notes

- Template inheritance keeps code DRY
- `url_for()` handles static file paths
- Much cleaner than string concatenation!

---

**Status:** ✅ Complete  
**Next:** Part 3 - Path Parameters