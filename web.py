import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    st.session_state["new_todo"] = ""
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("Things to do...")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", label_visibility="hidden",
              placeholder="Add a new to do...",
              on_change=add_todo, key="new_todo")