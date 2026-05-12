from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Session, create_engine, Relationship, select
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
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

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str
    created_at: datetime = Field(default_factory=datetime.now)
    tags: list["Tag"] = Relationship(back_populates="notes")


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

    notes: list[Note] = Relationship(back_populates="tags")

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str] = []


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

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str] = []


class Note(BaseModel):
    id: int
    title: str
    category: str
    content: str
    tags: list[str] = []
    created_at: str

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None

@app.patch("/notes/{note_id}")
def partial_update_note(note_id: int, note_update: NoteUpdate) -> Note:

    notes_db, _ = load_notes()

    for i, note in enumerate(notes_db):

        if note.id == note_id:

            updated_data = note.dict()

            if note_update.title is not None:
                updated_data["title"] = note_update.title

            if note_update.content is not None:
                updated_data["content"] = note_update.content

            if note_update.category is not None:
                updated_data["category"] = note_update.category

            if note_update.tags is not None:
                updated_data["tags"] = note_update.tags

            updated_note = Note(**updated_data)

            notes_db[i] = updated_note

            save_notes(notes_db)

            return updated_note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )

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
    
    global note_id_counter

    new_note = Note(
        id=note_id_counter,
        title=note.title,
        content=note.content,
        category=note.category,
        tags=note.tags,
        created_at=datetime.now(timezone.utc).isoformat()
    )

    notes_db.append(new_note)
    save_notes(notes_db)

    return new_note   

@app.get("/notes/category/{category}")
def get_notes_by_category(category: str):

    notes_db, _ = load_notes()

    filtered_notes = []

    for note in notes_db:
        if note.category == category:
            filtered_notes.append(note)

    return filtered_notes
    

NOTES_FILE = Path("data/notes.json")

def load_notes():
    """Load notes from JSON file and return notes list and next ID counter"""
    notes_db = []
    note_id_counter = 1
    
    if NOTES_FILE.exists():
        with open(NOTES_FILE, 'r') as f:
            data = json.load(f)
            notes_db = [Note(**note) for note in data]
            
            if notes_db:
                note_id_counter = max(note.id for note in notes_db) + 1
    
    return notes_db, note_id_counter
NOTES_FILE = Path("data/notes.json")

def load_notes():
    """Load notes from JSON file and return notes list and next ID counter"""
    notes_db = []
    note_id_counter = 1
    
    if NOTES_FILE.exists():
        with open(NOTES_FILE, 'r') as f:
            data = json.load(f)
            notes_db = [Note(**note) for note in data]
            

            if notes_db:
                note_id_counter = max(note.id for note in notes_db) + 1
    
    return notes_db, note_id_counter

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
    return {
        "semester": semester,
        "min_ects": min_ects,
        "search": search
    }
from sqlmodel import select, or_, col

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
                col(Note.title).ilike(f"%{search_lower}%"),
                col(Note.content).ilike(f"%{search_lower}%")
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
            ...
        )
        for note in tag.notes
    ]

@app.get("/notes/stats")
def get_note_stats():

    notes_db, _ = load_notes()

    return {
        "total_notes": len(notes_db),
        "unique_tags_count": len(
    set(
        tag
        for note in notes_db
        for tag in note.tags
    )
)
    }
@app.get("/categories")
def list_categories() -> list[str]:
    """Get all unique categories from all notes"""
    notes_db, _ = load_notes()
    
    pass
@app.get("/categories/{category_name}/notes")
def get_notes_by_category(category_name: str) -> list[Note]:
    """Get all notes in a specific category"""
    notes_db, _ = load_notes()
    
    pass


def get_session():
    with Session(engine) as session:
        yield session


SQLModel.metadata.create_all(engine)

@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):

    with Session(engine) as session:

        tag_objects = []

        for tag_name in note.tags:

            statement = select(Tag).where(Tag.name == tag_name)
            existing_tag = session.exec(statement).first()

            if existing_tag:
                tag_objects.append(existing_tag)

            else:
                new_tag = Tag(name=tag_name)
                session.add(new_tag)
                tag_objects.append(new_tag)

        db_note = Note(
            title=note.title,
            content=note.content,
            category=note.category,
            tags=tag_objects
        )

        session.add(db_note)

        session.commit()

        session.refresh(db_note)

        return db_note
    