# Intro to Streamlit

**Why Streamlit?**
- Dont have to learn HTML, CSS, JS etc
- JS ecosystem is evolving a lot
- Another Front-end team
  - May lead to communication gap
  - Availability issue.

**Why not use other Python based libs?**
- Flask and Django - **LOWER INTERACTIVITY**
- Streamlit 
    - **Rapid Prototyping(___Simplified working model___), Interactivity is high**
    - Fast to detect changes automatically.

**Building Blocks of a Streamlit APP**
```
    <!-- Command to run sample web app by st team -->
    streamlit hello
```
![Building Block of ST app][building_block_st]

# Building Simple Web page Application

**Text on a Page**
- Show Text:-
    - st.write()
    - Magic commands

- Show Data:-
    - st.table()
    - st.dataframe()

**Charts and Multimedia**

Helpful commands and 3rd party libs with Streamlit
![Adding More Content to ST][adding_more_content]

- Behind the scenes the argument passed in the chart fns are converted to DFs.
- st.image() doesn't require PIL import now.

**Adding Widgets to the ST app**
![Widgets][adding_widgets]
![More Widgets][more_widgets]

**Caching**
![Caching][caching]
-@st.cache_data(max_entries=2, ttl=60)
-max_entries = 2, means at most two entries can be hold.
-ttl = 60, means upto 60ms cache data can be stored, bcoz app data may increase if we keep adding cache data to the memory.

**LifeCycle of ST app**
**Note**- Interacting with Charts etc doesn't load the whole page.
![Lifecycle][lifecycle_of_st]

# Advanced Features of Streamlit

**Session state**
-All types of DS supported to store the session_state variable

```
    <!-- Creating the session state variable for later use -->
    if 'number' not in st.session_state:
        st.session_state['number'] = 1

    <!-- Later state of the app can be managed using session_state var -->
    if st.button("Increase number by 1"):
        st.session_state['number'] += 1
    if st.button("Decrease number by 1"):
        st.session_state['number'] -= 1

    st.write(st.session_state['number'])
```

**Placeholder**
![Placeholder][placeholder]

**Containers and Columns**
- Containers
    - Elements added to container will not be replaced as that in Placeholders
    - ``` con = st.container() ```
- Columns:- used to organize the content horizontaly.

![Organization of a Page][organize_a_page]

# Extending ST APP
![components][components]
![custom_components][custom_components]
![community][community_links]
![configuration][config_settings]

- Priority of the configuration_options if from left to right. 
- Global config file(least priority), command line(highest priority)
![configuration_options][configuration_ways]

# Deploying ST app to production
![developer_options][developer_options]
![heroku][heroku_app]



<!-- All Image Path for re-usability-->
[building_block_st]: ./notes_helper_images/building_block_st.png
[adding_more_content]: ./notes_helper_images/adding_more_content.png
[adding_widgets]: ./notes_helper_images/adding_widgets.png
[more_widgets]: ./notes_helper_images/more_widgets.png
[caching]: ./notes_helper_images/caching.png
[lifecycle_of_st]: ./notes_helper_images/lifecycle_of_st.png
[placeholder]: ./notes_helper_images/placeholders.png
[organize_a_page]: ./notes_helper_images/organization_of_page.png
[components]: ./notes_helper_images/static_birn_compo.png
[custom_components]: ./notes_helper_images/custome_comp.png
[community_links]: ./notes_helper_images/community.png
[config_settings]: ./notes_helper_images/config_settings.png
[configuration_ways]: ./notes_helper_images/configuration_way.png
[developer_options]: ./notes_helper_images/developer_options.png
[heroku_app]: ./notes_helper_images/heroku.png