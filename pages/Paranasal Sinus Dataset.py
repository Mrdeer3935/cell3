import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import pandas as pd
import numpy as np
import hydralit_components as hc

st.set_page_config(page_title='Paranasal Sinus Dataset',
                   page_icon=':nose:',layout='wide',initial_sidebar_state='collapsed',)

col1,col2,col3 = st.columns((1,3,1))
with col2:

    st.header("Appendix C: Paranasal Sinus Dataset")
    GEO, dbGap, CNCB = st.tabs(['GEO' , 'dbGap', 'CNCB' ])

    with GEO:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('GSE179269',
             'GSE196169',
             'GSE202100'))


        st.markdown("# MORE INFORTION"
                    "数据下载链接等")
        hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good', bar_value=100,key=1)


    with dbGap:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('phs002333'
             ,))

        hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good', bar_value=100,key=2)

    with CNCB:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('HRA000772'
             ,))

        hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good', bar_value=100,key=3)

