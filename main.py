from curses import raw

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
import json
from pydantic import model_validator
from typing_extensions import Self
from pathlib import Path
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Session, create_engine, Relationship, select, or_, col
from datetime import datetime
from fastapi import FastAPI
from sqlmodel import select, or_, col
from typing import Annotated
from fastapi import Depends
COURSES_FILE = Path("courses.json")
engine = create_engine("sqlite:///notes.db")

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI(
    title="Note Taking API",
    description="Simple note management",
    version="1.0.0"
)

ALLOWED_CATEGORIES = {
    "work",
    "personal",
    "school",
    "ideas"
}

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str = Field(..., description="Note category")
    created_at: datetime = Field(default_factory=datetime.now)
  



class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    created_at: datetime
    tags: list[str] = []

    class Config:
        from_attributes = True

engine = create_engine("sqlite:///notes.db")

class CourseCreate(BaseModel):
    """Model for creating courses (no ID)"""
    code: str
    name: str
    semester: int
    ects: int
    lecturer: str


class Course(BaseModel):
    """Model for courses (with ID)"""
    id: int
    code: str
    name: str
    semester: int
    ects: int
    lecturer: str

ALLOWED_CATEGORIES = {
    "work",
    "personal",
    "school",
    "ideas"
}    

class NoteCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)

    content: str = Field(
        min_length=1,
        max_length=10000
    )

    category: str

    tags: list[str] = Field(
        default_factory=list,
        max_length=10
    )

    @field_validator("title")
    @classmethod
    def strip_title(cls, value: str) -> str:
     return value.strip()

    @field_validator("category")
    @classmethod
    def category_must_be_known(cls, value: str) -> str:
        value = value.strip().lower()
        if value not in ALLOWED_CATEGORIES:
            raise ValueError(
                f"category must be one of {sorted(ALLOWED_CATEGORIES)}"
            )

        return value
    
    @field_validator("tags")
    @classmethod
    def clean_tags(cls, raw: list[str]) -> list[str]:
        cleaned: list[str] = []
        seen: set[str] = set()

        for tag in raw:
            t = tag.strip().lower()

            if not t:
                raise ValueError("tags must not be empty strings")

            if t in seen:
                continue

            seen.add(t)
            cleaned.append(t)

        return cleaned
    @model_validator(mode="after")
    def work_notes_need_work_tag(self) -> Self:


         if self.category == "work" and "work" not in self.tags:
          raise ValueError(
            "work notes must include the 'work' tag"
        )

         return self

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None   



def save_notes(notes):
    """Save notes to JSON file"""

    NOTES_FILE.parent.mkdir(exist_ok=True)

    with open(NOTES_FILE, "w") as f:
        json.dump(
            [note.model_dump() for note in notes],
            f,
            indent=2
        )
@app.post("/notes", status_code=201)
def create_note(note: NoteCreate) -> Note:
    """Create a new note"""
    new_note = Note(
        title=note.title,
        content=note.content,
        category=note.category,
        tags=note.tags,
        created_at=datetime.now(timezone.utc).isoformat()
    )

    return new_note   

@app.get("/test/{value}")
def test_value(value: str):
    return {
        "value": value
    }
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {
        "course_id": course_id
    }
def load_courses():
    """Load courses from JSON file and return courses list and next ID counter"""
    courses_db = []
    course_id_counter = 1
    
    if COURSES_FILE.exists():
        with open(COURSES_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            courses_db = [Course(**course) for course in data]
            
            if courses_db:
                course_id_counter = max(c.id for c in courses_db) + 1
    
    return courses_db, course_id_counter
def save_courses(courses_db):
    """Save courses to JSON file"""

    with open(COURSES_FILE, "w", encoding="utf-8") as f:
        json.dump(
            [course.model_dump() for course in courses_db],
            f,
            indent=2
        )
  

@app.get("/courses/code/{course_code}")
def get_course_by_code(course_code: str):
    return {
        "course_code": course_code
    }
@app.get("/students/{student_id}/courses/{course_id}")
def get_student_course(student_id: int, course_id: int):

    return {
        "student_id": student_id,
        "course_id": course_id
    }   

@app.get("/courses")
def list_courses(
    semester: int = None,
    min_ects: int = 10,
    search: str = ""
):
    """List all courses with optional filters"""

    courses_db, _ = load_courses()

    filtered = courses_db

    if semester is not None:
        filtered = [c for c in filtered if c.semester == semester]

    if min_ects > 0:
        filtered = [c for c in filtered if c.ects >= min_ects]

    return filtered


@app.get("/notes")
def list_notes(
    session: SessionDep,
    category: str = None,
    search: str = None,
    tag: str = None
) -> list[NoteResponse]:
    """List notes with filters"""
    
    statement = select(Note)
    
    if category:

        statement = statement.where(Note.category == category)
    
    if search:
        search_lower = search.lower()
        statement = statement.where(
            or_(
                Note.title.ilike(f"%{search_lower}%"),
                Note.content.ilike(f"%{search_lower}%")
            )
        )
    
    if tag:
        tag_lower = tag.lower()
        statement = statement.join(Note.tags).where(Tag.name == tag_lower)
    
    notes = session.exec(statement).all()
    
    return [
        NoteResponse(
            id=n.id,
            title=n.title,
            content=n.content,
            category=n.category,
            tags=[tag.name for tag in n.tags],
            created_at=n.created_at.isoformat()
        )
        for n in notes
    ]
@app.put("/notes/{note_id}")
def update_note(
    note_id: int,
    note_update: NoteCreate,
    session: SessionDep
) -> NoteResponse:

    note = session.get(Note, note_id)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    note.title = note_update.title
    note.content = note_update.content
    note.category = note_update.category

    session.add(note)
    session.commit()
    session.refresh(note)

    return NoteResponse(
        id=note.id,
        title=note.title,
        content=note.content,
        category=note.category,
        tags=[tag.name for tag in note.tags],
        created_at=str(note.created_at)
    )
@app.delete("/notes/{note_id}", status_code=204)
def delete_note(
    note_id: int,
    session: SessionDep
):
    note = session.get(Note, note_id)
    
    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    
    session.delete(note)
    session.commit()
    
    return 
@app.get("/tags")
def list_tags(session: SessionDep) -> list[str]:
    """Get all unique tags from the Tag table"""
    statement = select(Tag)
    tags = session.exec(statement).all()
    
    return sorted([tag.name for tag in tags])

@app.get("/tags/{tag_name}/notes")
def get_notes_by_tag(tag_name: str, session: SessionDep) -> list[NoteResponse]:
    """Get all notes with specific tag"""
    tag_lower = tag_name.lower()
    statement = select(Tag).where(Tag.name == tag_lower)
    tag = session.exec(statement).first()
    
    if not tag:
        return [] 
    
    return [
        NoteResponse(
            title=note.title,
            content=note.content,
            category=note.category,
            tags=[tag.name for tag in note.tags],
            created_at=note.created_at.isoformat()
        )
        for note in tag.notes
    ]

def get_session():
    with Session(engine) as session:
        yield session


SQLModel.metadata.create_all(engine)

@app.post("/courses", status_code=201)
def create_course(course: CourseCreate) -> Course:

    courses_db, course_id_counter = load_courses()

    for existing in courses_db:
        if existing.code.upper() == course.code.upper():
            raise HTTPException(
                status_code=409,
                detail=f"Course with code '{course.code}' already exists"
            )

    new_course = Course(
        id=course_id_counter,
        **course.model_dump()
    )

    courses_db.append(new_course)
    save_courses(courses_db)

    return new_course