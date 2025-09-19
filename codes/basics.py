import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import time
from helper import display_text, display_charts, display_widgets, display_more_widgets, display_caching

# Add title to the app
st.title("Sales Data!")
q1_sales = {
    "January": 1500,
    "February": 2000,
    "March": 1700
}
q2_sales = {
    "April": 1800,
    "May": 2200,
    "June": 2100
}
# Creating the session state variable for later use
if 'number' not in st.session_state:
    st.session_state['number'] = 1

section = st.sidebar.radio("Which Section?", 
                           ("Text", 
                            "Charts", 
                            "Widgets", 
                            "More Widgets", 
                            "Caching", 
                            "Session_state",
                            "Placeholder",
                            "Containers and Columns",
                            "Custom Components"
                            ))

if section == "Text":
    display_text(q1_sales, q2_sales)

elif section == "Charts":
    display_charts(q1_sales, q2_sales)

elif section == "Widgets":
    display_widgets(q1_sales, q2_sales)

elif section == "More Widgets":
    display_more_widgets(q1_sales, q2_sales)

elif section == "Caching":
    input = st.number_input("Insert a number", 1, 10, step=1)
    data = display_caching(input)
    st.write(data)

elif section == "Session_state":

    if st.button("Increase number by 1"):
        st.session_state['number'] += 1
    if st.button("Decrease number by 1"):
        st.session_state['number'] -= 1

    st.write(st.session_state['number'])

elif section == "Placeholder":
    placeholder = st.empty()
    for i in range(1, 11):
        placeholder.write(f"Iteration {i}")
        time.sleep(0.5)
    placeholder.write("Done!")

    pl = st.empty()
    for i in range(1, 12):
        pl.write(f"Iteration {i}")
        time.sleep(0.5)
    pl.write("Pl2 Done!")

elif section == "Containers and Columns":
    con = st.container()
    con.write("This is inside the container")

    for i in range(1,10):
        con.write(i)
        time.sleep(0.5)

    # Columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Column 1")
        st.write("This is column 1")    
    with col2:
        st.header("Column 2")
        st.write("This is column 2")
    with col3:
        st.header("Column 3")
        st.write("This is column 3")

elif section == "Custom Components":
    name = "snehil"
    components.html(f""" 
    <div onclick="alert('Hello {name}!')">
        <h2 style="color: blue;">Hello {name}!</h2>
        <p>This is a custom component.</p>
    </div>
    """)
