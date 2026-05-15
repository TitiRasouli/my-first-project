import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Notes Frontend")

# -----------------------
# Show Notes
# -----------------------

st.header("All Notes")

response = requests.get(f"{BASE_URL}/notes")

if response.status_code == 200:
    notes = response.json()

    for note in notes:
        with st.expander(note["title"]):
            st.write(f"Content: {note['content']}")
            st.write(f"Category: {note['category']}")
            st.write(f"Tags: {note['tags']}")
else:
    st.error("Could not load notes")


# -----------------------
# Create Note
# -----------------------

st.header("Create New Note")

with st.form("new_note_form"):

    title = st.text_input("Title")
    content = st.text_area("Content")
    category = st.text_input("Category")
    tags = st.text_input("Tags (comma separated)")

    submitted = st.form_submit_button("Create Note")

    if submitted:

        tags_list = [tag.strip() for tag in tags.split(",") if tag.strip()]

        payload = {
            "title": title,
            "content": content,
            "category": category,
            "tags": tags_list
        }

        create_response = requests.post(
            f"{BASE_URL}/notes",
            json=payload
        )

        if create_response.status_code == 201:
            st.success("Note created successfully ✅")
            st.rerun()

        else:
            st.error("Failed to create note")
            st.write(create_response.text)