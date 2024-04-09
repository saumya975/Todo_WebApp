import streamlit as st
import todoFunctions
todos=todoFunctions.get_todos()
def add_todo():
    todo =st.session_state['new_todo'].title()+"\n"
    todos.append(todo)
    todoFunctions.write_todos(todos)
    st.session_state['new_todo']=""
st.title("My Todo App")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox :
        todos.pop(index)
        todoFunctions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Enter a todo..",key='new_todo',on_change=add_todo)