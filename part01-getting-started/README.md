# Part 1: Getting Started - Building Your First API

## Video Info
**Duration:** 23:54  
**Link:** [Part 1 - Getting Started](https://www.youtube.com/watch?v=7AMjmCTumuo)  
**Completed:** January 29, 2026 ✅

## What I Built

Simple **Blog API** with in-memory data storage.

### Endpoints
- `GET /` → HTML: Displays first post title
- `GET /posts` → HTML: Displays first post title
- `GET /api/posts` → JSON: Returns all blog posts

### Sample Data
3 blog posts with structure:
```python
{
    "id": int,
    "author": str,
    "title": str,
    "content": str,
    "date_posted": str
}
```

## Running This Code
```bash
cd part01-getting-started
uvicorn main:app --reload
```

**Access:**
- Homepage: http://localhost:8000/
- API: http://localhost:8000/api/posts
- Docs: http://localhost:8000/docs

## Key Learnings

### Concepts
- ✅ FastAPI app creation (`app = FastAPI()`)
- ✅ Route decorators (`@app.get()`)
- ✅ Type hints (`list[dict]`)
- ✅ `response_class=HTMLResponse` for HTML responses
- ✅ `include_in_schema=False` to hide from API docs
- ✅ Automatic JSON serialization
- ✅ Multiple routes to same function

### Code Highlights

**Type-hinted data:**
```python
posts: list[dict] = [...]
```

**HTML response:**
```python
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"
```

**JSON response:**
```python
@app.get("/api/posts")
def get_posts():
    return posts  # Auto-converts to JSON!
```

## My Notes

**Awesome Features:**
- Automatic API documentation at `/docs`
- No manual JSON serialization needed
- Type validation happens automatically
- Can mix HTML and JSON in same app

**Next Steps:**
- Part 2: Replace basic HTML with Jinja2 templates
- Add path parameters (e.g., `/api/posts/{id}`)
- Add POST endpoint to create posts

---

**Status:** ✅ Complete  
**Time:** ~1 hour
