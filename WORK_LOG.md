# Work Log

**Tahereh Rasouli:** 

Instructions: Fill out one log for each course day. Content to consider: Course Sessions + Assignment

## Template:

---

## 1. ✅ What did I accomplish?

_Reflect on the activities, exercises, and work you completed today._

**Guiding questions:**
- What topics or concepts did you work with?
- What exercises or projects did you complete?
- What tools or technologies did you use?
- What did you learn or practice?

---


## 2. 🚧 What challenges did I face?

_Describe any difficulties, obstacles, or confusing moments you encountered._

**Guiding questions:**
- What was difficult to understand?
- Where did you get stuck?
- What errors or problems did you face?
- What felt frustrating or confusing?

---


## 3. 💡 How did I overcome them?

_Explain how you overcame the challenges or what help you needed._

**Guiding questions:**
- What strategies did you try?
- Who or what helped you (instructor, classmates, documentation)?
- What did you learn from solving the problem?
- What questions do you still have?

---


## Week 1

### Day 1

#### 1. ✅ What did I accomplish?
### Day 1

#### 1. What did I accomplish?

Today I learned the basics of FastAPI and created my first API project using Python.

At the beginning, I had very little knowledge about APIs and FastAPI, but I gradually understood the concepts through practice and repetition.

I installed FastAPI, uv, and uvicorn and learned how to run a local development server.

I created several GET endpoints such as:

- `/`
- `/status`
- `/about`
- `/square/{number}`
- `/double/{number}`

I also practiced working with path parameters and returning JSON responses.

Additionally, I learned how to use Swagger UI (`/docs`) to test API endpoints directly in the browser.

Technologies and tools used today:

- Python
- FastAPI
- uv
- uvicorn
- VS Code
- Git & GitHub

I practiced:

- Creating routes
- Running development servers
- Understanding API responses
- Using Git commands like commit and push

Because I was still learning the basics, I ran and rebuilt the project multiple times to better understand the workflow and structure.

---


#### 2. What challenges did I face?

Since I had limited prior knowledge, many concepts were confusing at first.

I faced several technical and logical issues while building the project.

Some challenges included:

- Indentation errors in Python
- Problems running the FastAPI development server
- Confusion between `main.py` and `main_2.py`
- Missing return statements inside functions
- Internal Server Error (500)
- Connection refused errors during testing
- Git branch issues (`master` vs `main`)
- Problems with uv installation and environment setup
- Difficulty understanding path parameters and endpoint structures

I also accidentally deleted or overwrote parts of the code several times and had to recreate sections of the project repeatedly.

---


#### 3. How did I overcome them?

I solved the problems step by step by reading the error messages carefully and testing different solutions.

I used:

- FastAPI documentation
- Swagger UI
- VS Code terminal
- Git commands
- Trial and error
- Repetition and practice

Because I was new to many concepts, repeating the project multiple times helped me understand the structure better and improve my confidence.

I learned that:

- Python indentation is extremely important
- Small syntax mistakes can stop the server completely
- Debugging is an important part of development
- Reading terminal errors carefully helps identify problems faster

By the end of the session, I successfully ran the FastAPI server, tested multiple endpoints, and gained a much better understanding of how APIs work.

---

### Day 2

#### 1. ✅ What did I accomplish?

Today I continued building the Notes API project and learned much more about backend development with FastAPI.

I improved my understanding of:

- FastAPI project structure
- Request and response handling
- JSON storage
- Pydantic models
- API debugging
- Data persistence concepts

I worked on building and improving several API endpoints including:

- `POST /notes`
- `GET /notes`
- `GET /notes/{note_id}`

I also learned how notes are temporarily stored in memory using:

```python
notes_db = []
```

and how API behavior changes after server reloads.

I practiced:

* Creating notes
* Retrieving notes
* Working with path parameters
* Testing APIs with Swagger UI
* Understanding JSON request bodies
* Debugging backend logic

I also learned how backend data flows between:

* Client
* FastAPI server
* JSON storage

Technologies and tools used today:

* Python
* FastAPI
* Pydantic
* JSON
* uv
* uvicorn
* Swagger UI
* VS Code
* Git & GitHub

---

#### 2.    What challenges did I face?

During Day 2, I faced many technical and conceptual challenges while continuing to build the backend project.

Main challenges included:

* Limited theoretical understanding of backend development concepts
* Difficulty understanding FastAPI project structure
* Confusion between main.py and main_2.py
* Problems with Python indentation
* Missing or undefined classes such as NoteCreate
* Errors caused by incorrect import statements
* Issues using timezone.utc
* Internal Server Errors (500)
* Problems with JSON serialization and saving data
* Difficulty understanding how request bodies work
* Confusion between dictionaries and Pydantic models
* Problems creating and using load_notes() and save_notes()
* API routes not appearing correctly in Swagger UI
* Mistakes in endpoint definitions
* Trouble understanding path parameters and response models
* Errors while running the FastAPI development server
* Issues with uv and package installation
* Git and branch management confusion (master vs main)
* Accidentally deleting or overwriting parts of the code
* Rebuilding the project multiple times to understand the workflow better
* Connection errors during API testing
* Learning how persistence works with JSON files
* Difficulty debugging terminal errors at first
* Understanding how data flows between client, API, and JSON storage took extra practice

Specific problems I encountered included:

##### Problem 1 — GET `/notes/{note_id}` returning 404

Even after creating notes successfully, the endpoint returned:

```text
404 Not Found
```

The issue happened because the application used temporary in-memory storage:

```python
notes_db = []
```

Whenever the server restarted or reloaded, all stored notes disappeared.

Additionally, the `load_notes()` function was missing, which caused:

```text
NameError: name 'load_notes' is not defined
```

##### Problem 2 — POST `/notes` returning 422

The API returned:

```text
422 Unprocessable Content
```
The issue was caused by invalid JSON syntax in the request body.

A trailing comma was accidentally added:

```json
{
  "title": "Shopping List",
  "content": "Milk, Eggs, Bread",
}
```

JSON does not allow a comma after the final item.

---


#### 3. 💡 How did I overcome them?

I solved the problems step by step by carefully reading terminal errors and debugging each issue individually.

Main solutions included:

* Carefully reading terminal error messages and debugging step by step
* Rebuilding the project multiple times to better understand the structure and workflow
* Practicing Python fundamentals such as:
    * functions
    * variables
    * data types
    * indentation
* Learning the correct FastAPI project structure:
    * imports
    * app creation
    * models
    * helper functions
    * routes
* Fixing missing imports such as timezone
* Adding missing classes like NoteCreate and Note
* Using Swagger UI (/docs) to test endpoints and inspect responses
* Learning the difference between dictionaries and Pydantic models
* Practicing JSON-based persistence and data storage
* Fixing API route problems by checking endpoint definitions carefully
* Solving server startup issues by correcting FastAPI configuration
* Learning how to use:
    * uv
    * uvicorn
    * virtual environments
* Using Git commands to manage versions and recover progress
* Improving debugging skills by identifying errors line by line
* Learning that small syntax or indentation mistakes can stop the entire backend application

For the 404 note retrieval issue, I:

- Replaced the missing `load_notes()` usage with temporary in-memory storage

- Added:

```python
notes_db = []
note_id_counter = 1
```

- Updated the `POST /notes` endpoint to append notes into `notes_db`
- Updated `GET /notes/{note_id}` to search through `notes_db`

I also learned that notes disappear after server reloads because memory storage is temporary.

For the 422 JSON issue, I:

- Removed the trailing comma from the JSON request body
- Corrected the request structure
- Successfully verified:
  - `POST /notes`
  - `GET /notes`
  - `GET /notes/1`

After fixing the issues:

- Notes were successfully stored
- Status code `201 Created` was returned correctly
- JSON responses worked properly
- Automatic timestamps worked correctly

By the end of Day 2, I had a much stronger understanding of FastAPI, request validation, backend debugging, and how API data persistence works.

---

### Day 3

#### 1. ✅ What did I accomplish?

Today I continued improving the FastAPI backend and learned more advanced API development concepts.

Main accomplishments today included:

- Added sorting support to the `/notes` endpoint
- Implemented pagination using:
  - `skip`
  - `limit`
- Added request validation using Pydantic `Field`
- Created endpoint to delete all notes
- Added export endpoint for JSON data
- Added health check endpoint
- Improved statistics endpoint with more detailed information
- Enhanced Swagger/OpenAPI documentation

I also worked heavily on understanding:

- REST API structure
- Query parameters
- Path parameters
- Nested routes
- API validation
- Route matching behavior

Additional API improvements included:

- Better endpoint organization
- Cleaner JSON responses
- Improved testing workflow
- Better route structure for dynamic URLs

Technologies and tools used today:

- Python
- FastAPI
- Pydantic
- Swagger UI
- JSON
- uvicorn
- VS Code
- Git & GitHub

---


#### 2. 🚧 What challenges did I face?

Today I encountered several backend architecture and routing problems while expanding the API.

Main challenges included:

- Sorting and pagination logic was confusing at first
- Validation errors while testing requests
- Some endpoints returned unexpected responses
- Difficulty deciding where filtering logic should be placed
- Understanding PATCH vs PUT behavior
- Route conflicts and duplicate endpoints
- Undefined variables
- Incorrect default value types
- Endpoints returning no data because of `pass`
- Route matching confusion
- 404 errors while testing note retrieval
- 422 validation errors caused by missing request fields
- Missing helper functions like `load_notes()`

Specific problems included:

---

##### Problem 1 — Duplicate `/courses` Endpoint

I accidentally created the same endpoint twice:

```python
@app.get("/courses")

FastAPI showed:
Duplicate Operation ID

Swagger/OpenAPI became confused because two endpoints had the same route and function name.



##### Problem 2 — Undefined Variables

VS Code highlighted undefined variables such as:
filtered_courses
all_courses
because they were never created.



##### Problem 3 — Wrong Default Type

I wrote:

```python
search: str = 0
```

The variable type was `str`, but the default value was an integer.

##### Solution

I changed it to:

```python
search: str = ""



##### Problem 4 — Using `pass` Instead of Returning Data

Some endpoints contained:

```python
pass
```

which caused the API to return no useful response.

---

##### Problem 5 — Route Matching Confusion

I learned that dynamic routes like:

```text
/test/{value}
```

can also match URLs such as:

```text
/test/123
```

This caused confusion about which endpoint FastAPI would use.

---


##### Problem 6 — 404 Not Found

While testing:

```text
/notes/1
```

I received:

```text
404 Not Found
```

because no note with ID `1` existed yet.

---

##### Problem 7 — 422 Unprocessable Content

I received:

```text
422 Unprocessable Content
```

because the JSON request body did not match the required Pydantic model.

Some required fields such as:

```text
category
```

were missing.

---

##### Problem 8 — NameError

FastAPI showed errors like:

```text
NameError: load_notes is not defined
```

---


#### 3. 💡 How did I overcome them?
I solved the issues step by step through debugging, testing, and restructuring the backend carefully.

Main solutions included:

* Tested endpoints one by one using Swagger UI
* Used terminal logs and traceback messages for debugging
* Reviewed FastAPI and Pydantic documentation
* Refactored filtering and routing logic carefully
* Practiced building query parameters and endpoint structures
* Learned how FastAPI validation works internally

Specific fixes included:

---

### Fix for Duplicate Endpoints

I removed the old `/courses` endpoint and kept only one version.

Final structure:

```python
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
```

---

### Fix for Undefined Variables

Instead of returning variables that did not exist, I temporarily returned JSON data directly:

```python
return {
    "semester": semester,
    "min_ects": min_ects,
    "search": search
}
```

This allowed me to continue testing the API structure safely.

---

### Fix for Wrong Default Type

I corrected:

```python
search: str = 0
```

to:

```python
search: str = ""
```

so the type and default value matched correctly.

---

### Fix for `pass` Statements

I replaced:

```python
pass
```

with actual JSON responses.

Example:

```python
@app.get("/students/{student_id}/courses/{course_id}")
def get_student_course(student_id: int, course_id: int):

    return {
        "student_id": student_id,
        "course_id": course_id
    }
```

---

### Fix for Route Matching Problems

I learned that:

```text
Route order matters
```

Specific routes should come before dynamic routes.

Correct structure:

```python
@app.get("/test/123")
@app.get("/test/{value}")
```

---

### Fix for 404 Errors

Before testing:

```text
GET /notes/1
```

I first created a note using:

```text
POST /notes
```

After creating the note successfully, the GET request worked correctly.

---

### Fix for 422 Validation Errors

I updated the JSON request body to include all required fields.

Correct example:

```json
{
    "title": "Exam Prep",
    "content": "Study chapters 1–5",
    "category": "study"
}
```

---

### Fix for NameError Problems

I added missing helper functions and ensured they were defined before being used.

---

## What I Learned Today

During Day 3 I learned:

- REST API structure
- Path parameters
- Query parameters
- Route matching behavior
- Nested resources
- HTTP status codes
- FastAPI validation
- Swagger testing
- Importance of endpoint order
- Difference between fixed and dynamic routes
- Pagination concepts
- Sorting logic
- PATCH vs PUT behavior
- Common backend debugging techniques
- Better API architecture practices

---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?

Today I worked on FastAPI testing, pytest integration, and SQLModel migration.

I created automated tests for API endpoints using `pytest` and FastAPI `TestClient`.

I completed exercises related to:

- Creating notes
- Listing notes
- Creating courses
- Error handling
- Validation testing

I also migrated parts of the Notes API from JSON-based storage to SQLModel and SQLite.

### Tools and Technologies Used

- Python
- FastAPI
- pytest
- SQLModel
- SQLite
- VS Code
- Git & GitHub

### What I Learned or Practiced

- API testing with pytest
- Using TestClient
- Arrange–Act–Assert testing structure
- SQLModel basics
- Debugging traceback errors
- Git workflow

---

#### 2. 🚧 What Challenges Did I Face?

I faced several debugging and migration problems while combining old JSON-based logic with the new SQLModel database structure.

### Difficulties and Problems

- Duplicate endpoint definitions
- Duplicate SQLModel tables
- Validation errors
- SQLAlchemy relationship errors
- Cached pytest issues
- Conflicts between old and new code

### Errors Encountered

- `NameError`
- `ValidationError`
- `HTTPException 404`
- `NoForeignKeysError`
- `InvalidRequestError`
- `409 Conflict`

One difficult part was identifying which endpoints were still using the old `notes_db` logic.

---

#### 3. 💡 How Did I Overcome Them?

I solved the issues step by step by debugging each error carefully and testing after every change.

### Strategies Used

- Reading pytest tracebacks
- Using VS Code global search
- Removing duplicated code
- Refactoring endpoints gradually
- Running tests after each fix

### What Helped Me

- ChatGPT debugging assistance
- FastAPI documentation
- SQLModel documentation
- pytest error messages

### What I Learned from Solving the Problems

- How pytest works internally
- How FastAPI testing is structured
- How to debug SQLModel and Pydantic issues
- Importance of separating old and new application logic

### Questions or Future Improvements

- Better SQLModel relationships
- More advanced API tests
- PATCH endpoint improvements
- Authentication support
 
---

### Day 5

#### 1. ✅ What did I accomplish?

## Topic: Pydantic Validation & FastAPI API Hardening

Today I worked extensively on improving validation and data quality in my FastAPI Notes API project using Pydantic v2.

The main focus of the day was learning how proper validation should be implemented directly inside Pydantic models instead of writing defensive checks inside API endpoints.

I improved the `NoteCreate` model by adding strict validation rules with `Field(...)`. I added:
- minimum and maximum length validation for `title`
- minimum and maximum length validation for `content`
- regex-based validation for `category`
- validation limits for the number of tags

I also configured the model with:

```python
model_config = ConfigDict(
    str_strip_whitespace=True,
    extra="forbid"
)
This automatically strips whitespace from incoming strings and rejects unknown fields in API requests.

Another major task today was implementing custom validators.

I used @field_validator to validate and normalize individual fields:

* converting category names to lowercase
* validating allowed categories
* cleaning tag values
* stripping whitespace from tags
* removing duplicate tags
* rejecting empty tags
* rejecting tags that are too short

I also implemented a @model_validator(mode="after") cross-field validation rule.

This validation checks:

* if the category is "work"
* then the note must include the "work" tag

This helped me understand the difference between field-level validation and model-level validation.

I also improved the Tag SQLModel model by adding:

* regex validation
* lowercase normalization
* minimum and maximum length validation

Another important part of today’s work was debugging and fixing runtime problems.

I fixed multiple issues related to:

* timezone imports
* incorrect Field(...) usage
* conflicts between Pydantic Field and SQLModel Field
* deprecated Pydantic configuration warnings
* datetime serialization issues

I manually tested many API requests using FastAPI Swagger Docs (/docs) and verified both valid and invalid cases.

I also updated and fixed the pytest test suite to match the new stricter validation behavior.

At first, multiple tests failed because the validation rules became stricter. I debugged each failing test individually and updated the payloads accordingly.

### Final pytest Result

```bash
uv run pytest
```

```text
5 passed
```

Finally, I committed and pushed all project changes to GitHub successfully.

### Technologies and Tools Used Today

- Python
- FastAPI
- Pydantic v2
- SQLModel
- SQLite
- pytest
- Swagger Docs (`/docs`)
- Git & GitHub
- VS Code

---

#### 2. 🚧 What Challenges Did I Face?

Today I faced several technical challenges while integrating strict validation into the FastAPI application.

One of the biggest challenges was understanding the difference between:

- endpoint validation
- field validation
- model validation
- database-level validation

At the beginning, it was not always clear where certain logic should belong.

Another challenge was the conflict between:

- `Field` from Pydantic
- `Field` from SQLModel

This caused runtime errors such as:

```text
TypeError: Field() got an unexpected keyword argument 'pattern'
```

I also encountered multiple validation-related errors:

- HTTP 422 responses
- failing pytest tests
- import issues
- datetime serialization warnings
- deprecated Pydantic configuration warnings

Another difficult part was implementing cross-field validation correctly using:

```python
@model_validator(mode="after")
```

because this validation depends on multiple fields at the same time.

I also had to debug why certain requests failed even though the JSON looked correct.

Several tests failed because the old test data no longer matched the new stricter validation rules.


---

#### 3. 💡 How Did I Overcome Them?

I solved these problems step by step by carefully reading error messages, testing API requests manually, and debugging validation behavior directly inside the models.

To fix the `Field` conflicts, I separated the imports correctly and used:

- Pydantic `Field` for validation models
- SQLModel `Field` for database models

I fixed the deprecated Pydantic configuration warning by replacing the old `class Config` usage with:

```python
model_config = ConfigDict(...)
```

I also fixed datetime warnings by removing unnecessary `.isoformat()` conversions and using proper `datetime` objects.

To debug validation problems, I repeatedly tested the API through Swagger Docs and inspected HTTP `422` responses carefully.

When pytest tests failed, I updated the test payloads to follow the new validation rules and reran the tests until all of them passed successfully.

By the end of the day, I had a much better understanding of:

- Pydantic v2 validation
- FastAPI request validation
- model validators
- field validators
- API hardening
- debugging validation errors
- writing stricter backend logic

Today’s work significantly improved both the quality and reliability of my Notes API project.


---

### Day 6

#### 1. ✅ What Did I Accomplish?

Today I completed a fully functional Notes API project using FastAPI, SQLModel, and SQLite.

### Main Accomplishments

- Built a complete REST API for notes management

- Implemented full CRUD functionality:
  - Create notes
  - Read notes
  - Update notes
  - Delete notes

- Added advanced filtering features:
  - Filter notes by category
  - Filter notes by tags
  - Search notes by title and content
  - Combine multiple filters together
  - Filter notes by date ranges
  - Filter notes created before or after a specific date

- Implemented PATCH and PUT endpoints correctly

- Added validation for invalid requests and dates

### Statistics Endpoints

Implemented endpoints for:

- Total notes count
- Unique tags count
- Notes grouped by category
- Top tags endpoint

### Tags Functionality

Implemented:

- Tag normalization
- Lowercasing tags
- Removing duplicate tags
- Empty tags support
- Case-insensitive tag lookup

### Additional Endpoints

Added endpoints for:

- `/tags`
- `/categories`
- `/notes/stats`
- `/tags/{tag}/notes`
- `/categories/{category}/notes`

### Automated Testing

- Successfully passed all automated tests
- `70 tests passed`

### Git & GitHub Workflow

Successfully used Git and GitHub:

- Added `.gitignore`
- Removed cache files
- Created commits
- Pushed the project to GitHub

---

#### 2. 🚧 What Challenges Did I Face?

Today I faced many backend development and debugging challenges.

### API and Backend Problems

- Multiple `500 Internal Server Errors`
- `404 Not Found` errors
- `405 Method Not Allowed` errors
- FastAPI route conflicts
- API not reachable issues
- Uvicorn server startup failures
- Port already in use errors

### Database and SQLModel Problems

- SQLite schema mismatch errors
- Database migration problems after adding new fields
- `"table note has no column named tags"`
- Problems rebuilding the database
- Relationship and tags handling issues

### Validation and Response Problems

- Missing tags in API responses
- Incorrect response structures
- `KeyError: 'tags'`
- Invalid date validation issues
- Incorrect response models
- Wrong status codes returned
- PATCH endpoint validation problems
- PUT endpoint returning `500` errors

### Python and Syntax Problems

- `IndentationError`
- `SyntaxError`
- `"return outside function"`
- `"expected an indented block after for"`
- Parentheses not closed
- Wrong indentation levels
- Variables defined outside function scope

### Logic Problems

- Statistics calculations returning wrong values
- `by_category` statistics always empty
- Tags endpoint returning empty lists
- Notes by tag endpoint returning empty results
- Filtering logic not working correctly
- Case-insensitive search problems
- PATCH not preserving existing data
- Tags not updating correctly

### Git and Project Management Problems

- Git tracking unwanted files:
  - `__pycache__`
  - `*.pyc`
  - `notes.db`

- Problems staging files correctly
- Managing `.gitignore`
- Cleaning temporary files before commit

---

#### 3. 💡 How Did I Overcome Them?

I solved the issues systematically using debugging, testing, and incremental improvements.

### Debugging Strategy

- Read traceback messages carefully

- Used pytest continuously:

```bash
uv run pytest test_notes_api.py -v -x
```

- Solved one failing test at a time
- Used server logs to identify exact backend failures
- Restarted Uvicorn after important changes

---

### Backend Fixes

- Added missing endpoints
- Corrected FastAPI decorators
- Fixed `response_model` definitions
- Added proper `HTTPException` handling
- Fixed PATCH and PUT logic
- Added missing route handlers

---

### Database Fixes

- Rebuilt SQLite database after schema changes
- Removed old `notes.db` when schema became outdated
- Fixed tags field handling
- Corrected SQLModel interactions

---

### Code Structure Improvements

- Fixed indentation issues
- Moved misplaced return statements
- Corrected variable scopes
- Fixed loops and conditional blocks
- Improved endpoint organization

---

### API Logic Improvements

- Added proper filtering logic
- Implemented date validation with `datetime` typing
- Fixed statistics calculations
- Corrected category aggregation
- Implemented tag normalization
- Added case-insensitive search and filtering

---

### Git Improvements

- Added proper `.gitignore`
- Removed cache files from repository
- Cleaned tracked temporary files
- Created clean commits
- Successfully pushed the final project to GitHub


---

#### 4. 📚 What Did I Learn Today?

Today I learned many practical backend development concepts:

- Building APIs with FastAPI
- Using SQLModel with SQLite
- REST API design principles
- API validation and error handling
- PATCH vs PUT behavior
- Database schema management
- Automated API testing with pytest
- Debugging backend applications
- Reading Python tracebacks
- Managing Git repositories professionally
- Using `.gitignore` effectively
- Structuring backend projects properly

This was one of the most difficult and educational development days so far.

---

## Week 3

### Day 7

#### 1. ✅ What Did I Accomplish?

Today I learned the basics of frontend development using Streamlit and connected it to my existing FastAPI Notes API project.

### Main Accomplishments

- Installed and configured Streamlit
- Created my first Streamlit application
- Learned how Streamlit automatically updates the UI
- Built a frontend for the Notes API

### Frontend Features Implemented

- Display all notes from the backend API
- Show note details using expandable sections
- Display:
  - title
  - content
  - category
  - tags

- Connected the Streamlit frontend to the FastAPI backend using `requests`
- Successfully retrieved live data from the API
- Created a form for creating new notes
- Sent `POST` requests from the frontend to the backend
- Automatically refreshed the frontend after creating notes

### Streamlit Components Learned

- `st.title()`
- `st.header()`
- `st.write()`
- `st.expander()`
- `st.form()`
- `st.text_input()`
- `st.text_area()`
- `st.form_submit_button()`
- `st.success()`
- `st.error()`
- `st.rerun()`

### Running Multiple Services

Successfully ran:

- FastAPI backend
- Streamlit frontend

simultaneously.

### Full-Stack Application

Built my first real full-stack application using:

- FastAPI backend
- SQLite database
- Streamlit frontend
- API integration

### Final Results

- Successfully tested frontend-backend communication
- Successfully pushed the frontend project updates to GitHub

---

#### 2. 🚧 What Challenges Did I Face?

Today I faced several frontend and integration challenges.

### Streamlit Problems


- Streamlit file not found errors
- Accidentally creating a file named:

```text
touch frontend.py
```

instead of:

```text
frontend.py
```

- Streamlit app not reloading correctly
- Browser showing empty pages
- Streamlit process stopping unexpectedly

### FastAPI and Backend Problems

- FastAPI server conflicts
- Address already in use errors
- Hung Uvicorn processes
- API endpoint not reachable
- Backend process running in the background incorrectly
- Swagger/docs not loading initially

### Integration Problems

- Frontend showing an empty notes list
- Frontend not displaying API data
- Streamlit not receiving notes from the backend
- Browser refresh issues
- Communication problems between frontend and backend

### Terminal and Process Problems

- Multiple terminals becoming confusing
- Accidentally stopping the wrong process
- `Ctrl + C` interrupt issues
- Killing old processes manually using:

```bash
lsof -i :8000
kill -9 PID
```

### General Debugging Problems

- Understanding which service was failing:
  - Streamlit
  - FastAPI
  - Browser
  - API connection

- Debugging frontend/backend integration step by step

---

#### 3. 💡 How Did I Overcome Them?

I solved the problems systematically by debugging each layer independently.

### Frontend Solutions

- Correctly renamed `frontend.py`
- Restarted Streamlit properly
- Refreshed the browser after backend changes
- Used Streamlit forms and rerun functionality correctly

### Backend Solutions

- Detected running processes with:

```bash
lsof -i :8000
```

- Killed broken FastAPI processes
- Restarted Uvicorn cleanly
- Verified API endpoints using Swagger UI
- Tested API responses before debugging the frontend

### Integration Solutions

- Tested the API manually through:

```text
/docs
```

- Verified JSON responses from the backend
- Confirmed notes existed in the database
- Connected `requests.get()` and `requests.post()` correctly
- Refreshed Streamlit after creating notes

### Process Management Improvements

- Learned how to run:
  - FastAPI in one terminal
  - Streamlit in another terminal

- Improved my understanding of the local development workflow

### Debugging Improvements

- Debugged problems layer by layer:
  1. Backend
  2. API endpoint
  3. Frontend
  4. Browser rendering

- Used terminal logs and error messages effectively

---

#### 4. 📚 What Did I Learn Today?

Today I learned many important frontend and full-stack development concepts.

### Main Learning Outcomes

- Basics of frontend development
- Building GUIs with Streamlit
- Connecting frontend to backend APIs
- Sending HTTP requests from frontend applications
- Full-stack application architecture
- Running multiple development servers simultaneously
- Managing local development environments
- Debugging frontend/backend integration
- Working with Streamlit session flow
- Using forms and dynamic UI updates
- Testing APIs before frontend integration
- Managing processes and ports in local development

### Major Milestone

Most importantly, today I built my first real full-stack application using Python only.

This was a major milestone in my development journey.






---