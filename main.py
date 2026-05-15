import json
from pathlib import Path
from typing import Optional, Annotated
from datetime import datetime, timezone
from icecream import ic
from fastapi import FastAPI, HTTPException, Depends
from requests import session
from sqlmodel import JSON, Column, Session
from typing import Annotated
from fastapi import Depends
from pydantic import (
    BaseModel,
    Field as PydanticField,
    field_validator,
    model_validator,
    ConfigDict,
)
from sqlalchemy import Column, JSON
from typing_extensions import Self

from sqlmodel import (
    SQLModel,
    Field,
    Session,
    create_engine,
    Relationship,
    select,
    or_,
    col,
)

from test_notes_api import note

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
    tags: list[str] = Field(default_factory=list, sa_column=Column(JSON))


class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(
        min_length=2,
        max_length=30,
        regex=r"^[a-z0-9-]+$",
        unique=True,
        index=True
    )
    @field_validator("name")
    @classmethod
    def clean_name(cls, value: str) -> str:
        return value.strip().lower()


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

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )

    title: str = PydanticField(min_length=3, max_length=100)
    content: str = PydanticField(min_length=1, max_length=10000)
    category: str = PydanticField(
        min_length=2,
        max_length=30,
        pattern=r"^[a-z]+$"
    )
    tags: list[str] = PydanticField(
        default_factory=list,
        max_length=10
    )
    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("title cannot be empty")
        return value

    @field_validator("category")
    @classmethod
    def validate_category(cls, value: str) -> str:
        value = value.lower()

        allowed = {
            "work",
            "personal",
            "school",
            "ideas",
            "general"
        }

        if value not in allowed:
            raise ValueError("invalid category")

        return value

    @field_validator("tags")
    @classmethod
    def clean_tags(cls, raw: list[str]) -> list[str]:
        cleaned: list[str] = []

        for tag in raw:
            tag = tag.strip().lower()

            if not tag:
                raise ValueError("empty tag not allowed")

            if len(tag) < 2:
                raise ValueError("tag too short")

            if tag not in cleaned:
                cleaned.append(tag)

        return cleaned

    @model_validator(mode="after")
    def validate_work_tag(self) -> Self:
        # needs BOTH category and tags
      #if self.category == "work" and "work" not in self.tags:
            #raise ValueError(
              #  "work notes must include the 'work' tag"
           # )

        return self

class NoteUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    category: str | None = None
    tags: list[str] | None = None  



def save_notes(notes):
    """Save notes to JSON file"""

    NOTES_FILE.parent.mkdir(exist_ok=True)

    with open(NOTES_FILE, "w") as f:
        json.dump(
            [note.model_dump() for note in notes],
            f,
            indent=2
        )

class NoteResponse(BaseModel):
    id: int | None
    title: str
    content: str
    category: str
    created_at: datetime
    tags: list[str] = []

    model_config = ConfigDict(from_attributes=True)

engine = create_engine("sqlite:///notes.db")

@app.post("/notes", status_code=201, response_model=NoteResponse)
def create_note(note: NoteCreate, session: SessionDep) -> Note:
    """Create a new note"""

    new_note = Note(
        title=note.title,
        content=note.content,
        category=note.category,
        tags=note.tags,
        created_at=datetime.now(timezone.utc)
    )

    session.add(new_note)
    session.commit()
    session.refresh(new_note) 

    #new_note.tags = note.tags

    return NoteResponse(
    id=new_note.id,
    title=new_note.title,
    content=new_note.content,
    category=new_note.category,
    created_at=new_note.created_at,
    tags=note.tags,
)

@app.get("/")
def root():
    return {
        "message": "Notes API",
        "status": "ok"
    }  

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
    tag: str = None,
    created_after: datetime | None = None,
    created_before: datetime | None = None,
)-> list[NoteResponse]:
    """List notes with filters"""
    
    statement = select(Note)
    if created_after:
        statement = statement.where(Note.created_at >= created_after)

    if created_before:
        statement = statement.where(Note.created_at <= created_before)

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
    
    #if tag:
        #tag_lower = tag.lower()
        #statement = statement.join(Note.tags).where(Tag.name == tag_lower)
    
    notes = session.exec(statement).all()
    if tag:
       tag_lower = tag.lower()
       notes = [
         n for n in notes
         if tag_lower in (n.tags or [])
    ]
    return [
        NoteResponse(
            id=n.id,
            title=n.title,
            content=n.content,
            category=n.category,
            tags=n.tags or [],
            created_at=n.created_at
        )
        for n in notes
    ]

@app.get("/notes/stats")
def notes_stats(session: SessionDep):
    notes = session.exec(select(Note)).all()

    all_tags = []
    for note in notes:
        all_tags.extend(note.tags or [])


    by_category = {}

    for note in notes:
        by_category[note.category] = by_category.get(
    note.category, 0
) + 1

    return {
    "total_notes": len(notes),
    "unique_tags_count": len(set(all_tags)),
    "top_tags": [],
    "by_category": by_category,
}  
@app.get("/categories")
def list_categories(session: SessionDep):
    notes = session.exec(select(Note)).all()

    categories = sorted(
        set(note.category for note in notes)
    )

    return categories

@app.get("/categories/{category}/notes", response_model=list[NoteResponse])
def notes_by_category(category: str, session: SessionDep):
    category_lower = category.lower()
    notes = session.exec(
        select(Note).where(Note.category == category_lower)
    ).all()

    return [
        NoteResponse(
            id=n.id,
            title=n.title,
            content=n.content,
            category=n.category,
            created_at=n.created_at,
            tags=n.tags or [],
        )
        for n in notes
    ]

@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, session: SessionDep) -> NoteResponse:
    note = session.get(Note, note_id)

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return NoteResponse(
        id=note.id,
        title=note.title,
        content=note.content,
        category=note.category,
        created_at=note.created_at,
        tags=note.tags or [],
    )

@app.patch("/notes/{note_id}", response_model=NoteResponse)
def patch_note(note_id: int, note_update: NoteUpdate, session: SessionDep):
    note = session.get(Note, note_id)

    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    data = note_update.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(note, key, value)

    session.add(note)
    session.commit()
    session.refresh(note)

    return NoteResponse(
        id=note.id,
        title=note.title,
        content=note.content,
        category=note.category,
        created_at=note.created_at,
        tags=note.tags or [],
    )

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
    note.tags = note_update.tags

    session.add(note)
    session.commit()
    session.refresh(note)

    return NoteResponse(
        id=note.id,
        title=note.title,
        content=note.content,
        category=note.category,
        tags=note.tags or [],
        created_at=note.created_at
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
def list_tags(session: SessionDep):
    notes = session.exec(select(Note)).all()

    all_tags = []
    for note in notes:
        all_tags.extend(note.tags or [])

    return sorted(set(all_tags))

@app.get("/tags/{tag}/notes", response_model=list[NoteResponse])
def notes_by_tag(tag: str, session: SessionDep):
    tag_lower = tag.lower()
    notes = session.exec(select(Note)).all()

    matching_notes = [
        n for n in notes
        if tag_lower in (n.tags or [])
    ]

    return [
        NoteResponse(
            id=n.id,
            title=n.title,
            content=n.content,
            category=n.category,
            created_at=n.created_at,
            tags=n.tags or [],
        )
        for n in matching_notes
    ]

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
