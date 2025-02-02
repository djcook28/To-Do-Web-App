import streamlit as st
import func

def add_to_do():
    new_to_do = st.session_state['new to do']
    to_dos.append(new_to_do + '\n')
    func.save_to_do_list(to_dos)
    #resets the text_input box to blank
    st.session_state['new to do'] = ''

st.title('To Do App')

to_dos = func.get_to_dos()
for index, to_do in enumerate(to_dos):
    #If key is not defined the list value will be used as the key for the checkbox
    # if there are multiple items in the list that are the same this will result
    # in an error.  Using the index as the key allows for duplication of to do items
    checkbox = st.checkbox(to_do, key=index)
    if checkbox == True:
        to_dos.pop(index)
        func.save_to_do_list(to_dos)
        del st.session_state[index]
        st.rerun()

st.text_input(label='', placeholder="Enter a to do here: ",  key='new to do')
st.button(label='Add', on_click=add_to_do)