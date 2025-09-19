import streamlit as st
import pandas as pd
import time

# Function to display text content

def display_text(q1_sales, q2_sales):
    st.header("Q1 Results!")
    st.write(q1_sales)

    st.header("Q2 Results!")
    st.write(q2_sales)

    df = pd.DataFrame(list(q2_sales.items()), columns=["Month", "Sales"])
    st.header("Table View")
    st.table(df)
    st.header("DataFrame View")
    st.dataframe(df)

# Function to display charts content

def display_charts(q1_sales, q2_sales):
    st.line_chart(q1_sales)
    st.area_chart(q2_sales)

    st.bar_chart([q1_sales, q2_sales])

    st.image(image="./notes_helper_images/building_block_st.png", caption="Building Blocks of Streamlit")

# Function to display widgets content

def display_widgets(q1_sales, q2_sales):
    # Buttons Widgets
    if st.button("Q1 Sales"):
        st.table(q1_sales)
    else:
        st.table(q2_sales)  

    # Checkbox Widgets
    if st.checkbox("Show Q1 Sales Data"):
        st.table(q1_sales)
    else:
        st.table(q2_sales)

    # Radio Button Widgets
    option = st.radio("Select Quarter", ("Q1", "Q2"))
    if option == "Q1":
        st.table(q1_sales)
    else:
        st.table(q2_sales)

# Function to display more widgets content

def display_more_widgets(q1_sales, q2_sales):
    # Selectbox Widgets
    option = st.selectbox("Select Quarter", ("Q1", "Q2"))
    if option == "Q1":
        st.table(q1_sales)
    else:
        st.table(q2_sales)

    # Slider widget
    st.write(st.slider("Select a value", 1,4,(1,2)))

    # Multi-select widget
    st.write(st.multiselect("Select Quarter", ("Q1", "Q2", "Q3", "Q4"), default=["Q1", "Q2"]))

    # Number input widget
    st.write(st.number_input("Insert a number", 1, 10, step=1))

# Function to display caching content

@st.cache_data(max_entries=2, ttl=120)
def display_caching(ip):
    if ip:
        ip += 100
        time.sleep(3)
    return ip
