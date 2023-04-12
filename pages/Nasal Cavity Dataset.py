import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import pandas as pd
import numpy as np
import hydralit_components as hc

st.set_page_config(page_title='Nasal Cavity Dataset',
                   page_icon=':nose:',layout='wide',initial_sidebar_state='collapsed',)

col1,col2,col3 = st.columns((1,3,1))
with col2:

    st.header("Appendix A: Nasal Cavity Dataset")
    EGA, GEO = st.tabs(['EGA', 'GEO'])

    with EGA:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('EGAD00001005714',
             'EGAD00001008560',
             'EGAD00001008159'))


        st.markdown("# MORE INFORTION"
                    "数据下载链接等")
        hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good', bar_value=100,key=1)


    with GEO:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('GSE184117',
             'GSE182475',
             'GSE139522',
             'GSE121600',
             'GSE191061',
             'GSE155113',
             'GSE171488',
             'GSE164547',
             'GSE162864',
             'GSE103518'
             ))

        hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good', bar_value=100,key=2)

