# Part 4: Pydantic Schemas - Request and Response Models

## Video Info
**Duration:** 24:23  
**Completed:** February 2, 2026 ✅

## What I Built

Request/response validation using Pydantic models for type safety and data validation.

## Running This Code
```bash
cd part04-pydantic-schemas
uvicorn main:app --reload
# Visit: http://localhost:8000/docs
```

## Key Learnings

- ✅ Pydantic BaseModel for data validation
- ✅ Request body schemas
- ✅ Response models with `response_model`
- ✅ Automatic data validation
- ✅ Type hints for documentation
- ✅ Field validation with `Field()`
- ✅ Optional fields with `Optional[Type]`

## Code Highlights

**Pydantic Schema:**
```python
from pydantic import BaseModel, Field
from typing import Optional

class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str
    published: bool = True
    rating: Optional[int] = Field(default=None, ge=0, le=5)

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    
    class Config:
        from_attributes = True  # Allows ORM objects
```

**Using Schemas in Routes:**
```python
@app.post("/posts", response_model=PostResponse, status_code=201)
def create_post(post: PostCreate):
    # post is validated automatically
    new_post = {
        "id": len(posts) + 1,
        **post.dict()
    }
    posts.append(new_post)
    return new_post
```

**Response Model Benefits:**
```python
# Only returns fields defined in PostResponse
# Filters out sensitive data automatically
@app.get("/posts/{id}", response_model=PostResponse)
def get_post(id: int):
    return find_post(id)
```

## My Notes

- Pydantic validates data automatically
- FastAPI uses schemas for API docs
- Response models prevent data leaks
- Field() allows custom validation
- Type hints = automatic documentation
- Cleaner than manual validation

---

**Status:** ✅ Complete  
**Next:** Part 5 - Database Integration
