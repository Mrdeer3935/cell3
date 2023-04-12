import streamlit as st
from hydralit import HydraApp
from Browse import BrowseAPP
from Home import HomeAPP
#from View import ViewAPP
from Help import HelpAPP

#make it look nice from the start
st.set_page_config(page_title='XX SingleCell RNAseq Database',
                   page_icon=':nose:',layout='wide',initial_sidebar_state='collapsed',)

if __name__ == '__main__':

    over_theme = {'txc_inactive': 'white', 'menu_background': 'black',
                  'txc_active': 'balck',} # 'option_active': 'blue'
    # font_fmt = {'font-class': 'h2', 'font-size': '150%'}

    app = HydraApp(
        #title='XX SingleCell RNAseq Database',
        hide_streamlit_markers=False,
        # add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        # use_banner_images=[None,"logo.png" , {
        #     'header': "<h1 style='text-align:center;padding: 0px 0px;color:black;font-size:300%;'>XX SingleCell RNAseq Database</h1><br>"},
        #                    None, None],
        use_banner_images=["banner.png"],
        banner_spacing=[100],
        #banner_spacing=[10, 3, 30, 3, 10],
        use_navbar=True,
        navbar_sticky=True,
        navbar_animation=True,
        navbar_theme=over_theme)

    app.add_app("Home", icon="🏠", app=HomeAPP(),is_home=True)
    app.add_app("Browse", icon="🔍", app=BrowseAPP())
    # app.add_app("View", icon="✅", app=ViewAPP())
    app.add_app("Help", icon="❔", app=HelpAPP())


    app.run()

