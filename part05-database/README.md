# Part 5: Adding a Database - SQLAlchemy

## Video Info
**Duration:** ~30 min  
**Completed:** February 2, 2026 ✅

## What I Built

Database integration with SQLAlchemy ORM for persistent data storage.

## Running This Code
```bash
cd part05-database
uvicorn main:app --reload
# Visit: http://localhost:8000/docs
```

## Key Learnings

- ✅ SQLAlchemy ORM setup
- ✅ Database models (tables)
- ✅ Database connection/session
- ✅ CRUD operations with database
- ✅ Database migrations concept
- ✅ Dependency injection for DB session
- ✅ Separating models from schemas

## Code Highlights

**Database Setup:**
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

**Database Model:**
```python
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
```

**Dependency Injection:**
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
```

**CRUD Operations:**
```python
# Create
db.add(new_post)
db.commit()

# Read
db.query(Post).filter(Post.id == id).first()
db.query(Post).all()

# Update
post.title = "New Title"
db.commit()

# Delete
db.delete(post)
db.commit()
```

## Project Structure
```
part05-database/
├── main.py          # FastAPI app
├── database.py      # DB connection
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
└── blog.db          # SQLite database
```

## My Notes

- Models (DB) vs Schemas (API) separation is crucial
- Dependency injection = clean database sessions
- SQLAlchemy handles SQL for us
- Sessions must be closed properly
- `db.refresh()` gets updated data from DB
- Great foundation for real applications

---

**Status:** ✅ Complete  
**Next:** Part 6 - CRUD Operations
