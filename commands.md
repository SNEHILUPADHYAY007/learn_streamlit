# Streamlit Commands: Usage & Context

## st.title()
- Displays a large title at the top of your app, typically for branding or main heading[web:1][web:5].
- Syntax: `st.title("My App Title")`
- Use this to set the main page title. Preferably called once for clarity[web:1][web:11].

## st.header()
- Shows a section header, appropriate for dividing app content into subsections[web:5][web:7].
- Syntax: `st.header("Section Name")`
- Useful for breaking your app into organized segments below the main title[web:7].

## st.write()
- Streamlit's Swiss-army knife for output: auto-formats text, numbers, tables, charts, and more[web:6][web:8][web:11].
- Syntax: `st.write(object)`
- Adapts formatting to the object type, great for rapid prototyping and versatile output[web:6][web:8].

## Magic Commands
- Any literal or variable on its own line (not inside a function) is auto-rendered using `st.write()`[web:10][web:20].
- Example:
    ```
    "Hello, World!"        # Renders as markdown text
    my_dataframe           # Renders as a table
    ```
- Keeps code concise; for more control, use explicit commands like `st.write()`[web:20].

## st.table()
- Displays tabular data in a static, readable format[web:8].
- Syntax: `st.table(data)`
- Best for small or non-interactive datasets, no filtering or sorting features[web:8].

## st.dataframe()
- Renders tabular data interactively, allowing user-driven sorting, filtering, column resizing, etc.[web:8].
- Syntax: `st.dataframe(df)`
- Essential for larger datasets or when you want users to explore data dynamically[web:8].

---

