import streamlit as st

"""
    TITLE, HEADERS, SUBHEADERS, TEXT, MARKDOWN, LATEX, WRITE
"""
# title accepts 3 arguments
# @arg1:- text
# @arg2:- anchor tag:- helpful in routing type of thing:- str or false
# @arg3:- helper tag:- extra information about that text:- str
st.title("Hello Snehil!!! :green-background[hahaha] :smile:", anchor = "google.com", help = "Hahahaha")

# header accepts 4 arguments
# first 3 are same, @arg4:- divider:- provides a divider after the text. Accepts bool or "color"
st.header("My name is :green-background[:blue[snehil]] :orange[!!!]", divider="rainbow")

# subheader accepts 4 arguments
# first 3 are same, @arg4:- divider:- provides a divider after the text. Accepts bool or "color"
# HEADER > SUBHEADER(in terms of displaying text size)
st.subheader("My name is :green-background[:blue[snehil]] :orange[!!!]", divider="rainbow")

# text accepts 2 args.
# @arg1:- text
# @arg2:- helper tag:- extra information about that text:- str
st.text("Snehil is AWSM!!!")

# markdown accepts 3args.
# @arg1:- text
# @arg2:- unsafe_allow_html:- <htmls> can be passed inside of it or bool.
# @arg3:- helper tag:- extra information about that text:- str

st.markdown("""  *HAHAHAH!*
## My name is :blue[Snehil]
**damn boy**
<a href="#">Check</a>                                    
""",True)

# Using Plain HTML inside Markdown.
html = """
    <input type="email" placeholder="Hahaha">
"""
st.markdown(html,True)

# latex accepts 2 args.
# @arg1:- text
# @arg2:- helper tag:- extra information about that text:- str
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# write accepts 2 args.
# *args:- any number of arg will be treated differently(based on what you've passed).  
# @arg2:- unsafe_allow_html:- <htmls> can be passed inside of it or bool.
st.write("hahah","nanannn",":green[mamamamama]")
st.write(st,sum)
