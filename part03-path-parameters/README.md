# Part 3: Path Parameters - Validation and Error Handling

## Video Info
**Duration:** 36:56  
**Completed:** January 30, 2026 ✅

## What I Built

Dynamic routing with path parameters and validation.

## Running This Code
```bash
cd part03-path-parameters
uvicorn main:app --reload
# Visit: http://localhost:8000/docs
```

## Key Learnings

- ✅ Path parameters (`/post/{id}`)
- ✅ Type validation (automatic with type hints)
- ✅ Query parameters
- ✅ Optional parameters with `Optional[str]`
- ✅ Error handling with `HTTPException`
- ✅ Status codes (404, 400, etc.)

## Code Highlights

**Path Parameters:**
```python
@app.get("/post/{id}")
def get_post(id: int):
    # FastAPI validates id is an integer
    post = next((p for p in posts if p["id"] == id), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
```

**Query Parameters:**
```python
@app.get("/posts")
def get_posts(limit: int = 10, skip: int = 0):
    return posts[skip:skip + limit]
```

**Optional Parameters:**
```python
from typing import Optional

@app.get("/search")
def search(q: Optional[str] = None):
    if q:
        return [p for p in posts if q.lower() in p["title"].lower()]
    return posts
```

## My Notes

- Type hints enable automatic validation
- FastAPI returns 422 for invalid types
- `HTTPException` for custom error responses
- Path parameters come before query parameters

---

**Status:** ✅ Complete  
**Next:** Part 4 - Pydantic Schemas
