import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import pandas as pd
import numpy as np
import hydralit_components as hc

st.set_page_config(page_title='Nasopharynx  Dataset',
                   page_icon=':nose:',layout='wide',initial_sidebar_state='collapsed',)

col1,col2,col3 = st.columns((1,3,1))
with col2:

    st.header("Appendix B: Nasopharynx  Dataset")
    SCP, GEO, CNCB = st.tabs(['Single Cell Portal', 'GEO','CNCB'])

    with SCP:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('xxxx'))


        st.markdown("# MORE INFORTION"
                    "数据下载链接等")
        hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good', bar_value=100,key=1)


    with GEO:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ("GSE150430",))

        hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good', bar_value=100,key=2)

    with CNCB:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('HRA000087',))

        hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good', bar_value=100,key=3)

