import streamlit as st
import hydralit_components as hc
import datetime
from hydralit import HydraHeadApp
import streamlit.components.v1 as components


class HelpAPP(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):
        #-------------------existing untouched code------------------------------------------
        st.title('user guide')

        with open('visitors.html', "r", encoding='utf-8') as f:
            data = f.read()
        #components.html("", height=50)
        components.html(data, height=500, scrolling=False)