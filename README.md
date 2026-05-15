## My First Project 🚀

A full-stack Notes Application built with:

* FastAPI
* SQLModel
* SQLite
* Streamlit
* Pytest
* Git & GitHub

This project was developed step-by-step during the first 7 days of an Applied Programming course.


## Project Overview

The goal of this project was to learn modern Python backend and frontend development by building a complete Notes Application from scratch.

The application includes:

* REST API backend
* SQLite database
* Automated testing
* Frontend with Streamlit
* Full CRUD functionality
* Filtering and statistics
* Git/GitHub workflow


## Technologies Used

| Technology | Purpose |
|---|---|
| FastAPI | Backend API framework |
| SQLModel | Database ORM |
| SQLite | Local database |
| Streamlit | Frontend UI |
| Pytest | Automated testing |
| Requests | API communication |
| Uvicorn | ASGI server |
| Git | Version control |
| GitHub | Remote repository hosting |

## Day-by-Day Progress


# Day 1 — Python Project Setup

Topics Learned

* Python project structure
* Virtual environments
* Using uv
* Installing dependencies
* Running Python files
* Basic Git setup

# Main Accomplishments

* Created the project repository
* Initialized virtual environment
* Installed project dependencies
* Learned how Python packages work
* Connected project to GitHub

## Important Commands

```bash
uv init
uv add fastapi
uv add sqlmodel
uv add uvicorn
```

## Day 2 — FastAPI Basics

# Topics Learned

* FastAPI fundamentals
* API endpoints
* HTTP methods
* JSON responses
* Swagger documentation

# Main Accomplishments

* Built first FastAPI application
* Created:
    * GET endpoint
    * POST endpoint
* Learned automatic API docs generation

## Example Endpoint

```python
@app.get("/")
def root():
    return {"message": "Hello World"}
```

# Important Concepts

* Request/response cycle
* JSON serialization
* API routing
* HTTP status codes


## Day 3 — Data Models & Validation

# Topics Learned

* Pydantic models
* Input validation
* Request schemas
* Response models
* Type hints

# Main Accomplishments

* Created structured request models
* Added validation for incoming data
* Improved API consistency
* Learned schema-based development

## Example Model

```python
class NoteCreate(BaseModel):
    title: str
    content: str
```

# Important Concepts

* Data validation
* Strong typing
* Request parsing
* API contracts

## Day 4 — Database Integration

# Topics Learned

* SQLModel
* SQLite databases
* ORM basics
* Sessions
* Database persistence

# Main Accomplishments

* Connected FastAPI to SQLite
* Created database models
* Learned session management
* Saved and retrieved data from database

## Example Database Model

```python
class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
```

# Important Concepts

* ORM mapping
* Database sessions
* Persistent storage
* CRUD database operations


## Day 5 — CRUD Operations

# Topics Learned

* CRUD architecture
* PUT vs PATCH
* DELETE endpoints
* Resource handling
* Error handling

# Main Accomplishments

Implemented complete CRUD functionality:

* Create notes
* Read notes
* Update notes
* Delete notes

## Example Endpoints

```python
@app.post("/notes")
@app.get("/notes")
@app.put("/notes/{note_id}")
@app.patch("/notes/{note_id}")
@app.delete("/notes/{note_id}")
``` 

# Important Concepts

* REST API design
* Resource management
* API consistency
* HTTP semantics



## Day 6 — Advanced Notes API & Testing

# Topics Learned

* Automated testing
* Pytest
* Advanced filtering
* API debugging
* Statistics endpoints
* Tag systems

# Main Accomplishments

Advanced Features

Implemented:

* Category filtering
* Tag filtering
* Search functionality
* Date filtering
* Combined filters
* Statistics endpoints
* Categories endpoints
* Tags endpoints

# Tags System

Implemented:

* Tag normalization
* Duplicate removal
* Case-insensitive lookup
* Empty tags support

# Statistics

Built endpoints for:

* Total notes
* Unique tags count
* Notes grouped by category
* Top tags

# Automated Testing

* Passed all 70 tests successfully

## Example Test Command

```bash
uv run pytest test_notes_api.py -v -x
```

# Major Challenges

* 500 Internal Server Errors
* SQLite schema mismatches
* Route conflicts
* Validation issues
* Syntax and indentation problems
* Statistics calculation bugs
* Tag handling bugs
* Git cleanup problems

# Major Lessons

* Backend debugging
* Reading Python tracebacks
* API testing strategies
* Systematic debugging workflows


## Day 7 — Frontend with Streamlit

# Topics Learned

* Frontend development basics
* Streamlit
* API integration
* Full-stack architecture
* UI interaction

# Main Accomplishments

Streamlit Frontend

Built a frontend application that:

* Displays all notes
* Shows note details
* Creates new notes
* Connects directly to FastAPI backend

# Features

* Dynamic note rendering
* Expandable note sections
* Forms for note creation
* Real-time UI updates

# Frontend Technologies

* Streamlit
* requests
* HTTP API integration

## Example Streamlit Code

```python
import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

response = requests.get(f"{BASE_URL}/notes")
notes = response.json()
```

# Major Challenges

* Streamlit file issues
* Port conflicts
* Background FastAPI processes
* Frontend/backend connection debugging
* Empty UI rendering
* Process management problems

# Major Lessons

* Full-stack application flow
* Frontend/backend integration
* Local development workflows
* Managing multiple servers
* Interactive frontend design


## Automated Testing

The backend includes comprehensive automated tests.

### Run Tests

```bash
uv run pytest test_notes_api.py -v
```

# Test Coverage Includes

* CRUD operations
* Validation
* Filtering
* Tags
* Statistics
* Error handling
* PATCH and PUT behavior
* Date filtering



### API Endpoints
## Notes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/notes` | Get all notes |
| POST | `/notes` | Create note |
| GET | `/notes/{id}` | Get single note |
| PUT | `/notes/{id}` | Replace note |
| PATCH | `/notes/{id}` | Partial update |
| DELETE | `/notes/{id}` | Delete note |

## Tags

| Method | Endpoint |
|---|---|
| GET | `/tags` |
| GET | `/tags/{tag}/notes` |

## Categories

| Method | Endpoint |
|---|---|
| GET | `/categories` |
| GET | `/categories/{category}/notes` |

## Statistics

| Method | Endpoint |
|---|---|
| GET | `/notes/stats` |


## Running the Project

### 1. Clone Repository

```bash
git clone <repo-url>
cd my-first-project
```

2. Install Dependencies
```bash
uv sync
```

3. Run FastAPI Backend

```bash
uv run uvicorn main:app --reload
```

# Backend URL:
```text
http://127.0.0.1:8000
```
# Swagger Docs:
```text
http://127.0.0.1:8000/docs
```


# 4. Run Streamlit Frontend
```bash
uv run streamlit run frontend.py
```
# Frontend URL:
```text
http://localhost:8501
```


## Project Structure

## Project Structure

```text
my-first-project/
│
├── main.py
├── frontend.py
├── test_notes_api.py
├── pyproject.toml
├── uv.lock
├── .gitignore
├── notes.db
└── README.md
```



## Key Concepts Learned

Backend Development

* REST APIs
* FastAPI
* Validation
* ORM usage
* Database management
* CRUD architecture
* Error handling
* Automated testing

# Frontend Development

* Streamlit
* Forms
* Interactive UIs
* API integration
* Session flow

# Full-Stack Development

* Frontend/backend communication
* HTTP requests
* Local development workflows
* Process management
* Full-stack debugging

# Software Engineering

* Git workflows
* Repository management
* Debugging strategies
* Incremental development
* Testing-first thinking



## Challenges Faced During Development

# Some major challenges encountered during the first 7 days:

* 500 Internal Server Errors
* SQLite migration problems
* Missing database columns
* FastAPI route conflicts
* Validation failures
* Indentation and syntax errors
* Broken response structures
* Tag filtering bugs
* Statistics calculation issues
* Streamlit integration problems
* Port conflicts
* Hung processes
* Git tracking unwanted files

These challenges helped develop strong debugging and problem-solving skills.
 

###############     Final Outcome After 7 Days.  #######################

By the end of Day 7, the project successfully included:

- [x] FastAPI backend
- [x] SQLite database
- [x] SQLModel ORM integration
- [x] Full CRUD functionality
- [x] Advanced filtering system
- [x] Statistics endpoints
- [x] Tags and categories system
- [x] Automated testing (70 tests passed)
- [x] Streamlit frontend
- [x] Full-stack integration
- [x] GitHub deployment workflow

## Future Improvements

Planned future improvements:

* Authentication
* User accounts
* Better frontend styling
* Docker support
* Deployment to cloud
* Search improvements
* Pagination
* Note editing in frontend
* Delete functionality in frontend
* Dark mode UI
* Better database architecture


# Author

## 👨‍💻 Author

Tahereh Rasouli

Applied Programming Course – 2026


## Conclusion

This project represents the first major milestone in learning modern Python full-stack development.

Over 7 days, the project evolved from a simple Python setup into a complete full-stack application with:

* Backend APIs
* Database persistence
* Automated tests
* Interactive frontend
* Real API integration
* GitHub workflow

The project provided practical experience in:

* Software engineering
* API design
* Debugging
* Testing
* Frontend/backend integration
* Full-stack development workflows

🚀