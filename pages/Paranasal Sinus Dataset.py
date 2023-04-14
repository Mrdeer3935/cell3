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


        if option =="GSE179269" :
            # st.success("## Infos\n"
            #         "##### First author: Tsuguhisa Nakayama\n"
            #         "##### Date: 1-Dec-2021\n"
            #         "##### DOI: [10.1016/j.jaci.2021.11.017](https://jingyan.baidu.com/article/b0b63dbfe018fc0b49307027.html)\n"
            #         "##### Journal: The Journal of allergy and clinical immunology\n"
            #         "##### Title: Inflammatory molecular endotypes of nasal polyps derived from White and Japanese populations\n"
            #         "##### Sample: CRSwNP(n=19); Health(n=7)\n"
            #         "##### Study description: Inflammatory molecular endotypes of nasal polyps derived from Caucasian and Japanese populations.\n"
            #         "##### Accession processed data: [GSE179269](https://https.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE179269)\n")


            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
    <h2 style="text-align: center;">INFOS</h2>
    <ul style="list-style: none; text-align: left;">
    <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Tsuguhisa Nakayama</span></li>
    <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">1-Dec-2021</span></li>
    <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://linkinghub.elsevier.com/retrieve/pii/S0091-6749(21)01821-2"; style="color: black; font-weight: bold; font-size: 20px">10.1016/j.jaci.2021.11.017</a></li>
    <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">The Journal of allergy and clinical immunology</span></li>
    <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">Inflammatory molecular endotypes of nasal polyps derived from White and Japanese populations</span></li>
    <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">CRSwNP(n=19); Health(n=7)</span></li>
    <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Inflammatory molecular endotypes of nasal polyps derived from Caucasian and Japanese populations.</span></li>
    <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://https.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE179269"; style="color: black; font-weight: bold; font-size: 20px">GSE179269</a></li>
    </ul>
</div>

""",unsafe_allow_html=True)

        if option == "GSE196169":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                              <h2 style="text-align: center;">INFOS</h2>
                              <ul style="list-style: none; text-align: left;">
                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Christine Bangert
        </span></li>
                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">28-Mar-2022
        </span></li>
                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.frontiersin.org/articles/10.3389/fimmu.2022.850494/full"; style="color: black; font-weight: bold; font-size: 20px">10.3389/fimmu.2022.850494
        </a></li>
                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Frontiers in immunology
        </span></li>
                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">Comprehensive Analysis of Nasal Polyps Reveals a More Pronounced Type 2 Transcriptomic Profile of Epithelial Cells and Mast Cells in Aspirin-Exacerbated Respiratory Disease
        </span></li>
                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">AERD(n=10); CRSwNP(n=9)
        </span></li>
                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px"><br>Objective: We sought to obtain detailed information about transcriptional differences in epithelial cells and immune cell subsets present in polyps of aspirin-exacerbated respiratory disease and chronic rhinosinusitis with nasal polyps.
<br>Methods: After enrichment for various immune subsets by flow cytometric sorting of polyp-derived cells, we performed transcriptomic profiling by employing single-cell RNA sequencing of all patients.
<br>Results: Transcriptomic profiling revealed that epithelial and mast cells not only complement one another in terms of gene expression associated with the 15-lipoxygenase pathway, but also show a clear type 2 associated inflammatory phenotype as identified by the upregulation of POSTN, CCL26 and IL13 in patients with aspirin-exacerbated respiratory disease.
</span></li>
                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE196169"; style="color: black; font-weight: bold; font-size: 20px">GSE196169</a></li>
                                </ul>
                            </div>""", unsafe_allow_html=True)

        if option == "GSE202100":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                      <h2 style="text-align: center;">INFOS</h2>
                                      <ul style="list-style: none; text-align: left;">
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Maya E Kotas
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">28-Jul-2022
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://insight.jci.org/articles/view/159832"; style="color: black; font-weight: bold; font-size: 20px">10.1172/jci.insight.159832
                </a></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">JCI insight
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">IL-13-programmed airway tuft cells produce PGE2, which promotes CFTR-dependent mucociliary function
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">CRSwNP(n=5)
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Allergic nasal polyposis is a chronic type 2 inflammatory condition of the upper respiratory tract. We characterize nasal polyps from 5 subjects using single-cell RNA-sequencing, identifying “allergic” tuft cells, characterized by increased expression of the prostaglandin synthetic pathway, in association with a PGE2-activated gene signature.
        </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE202100"; style="color: black; font-weight: bold; font-size: 20px">GSE202100</a></li>
                                        </ul>
                                    </div>""", unsafe_allow_html=True)

    with dbGap:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('phs002333'
             ,))

        if option == "phs002333":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
              <h2 style="text-align: center;">INFOS</h2>
              <ul style="list-style: none; text-align: left;">
                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Daniel F Dwyer</span></li>
                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">26-Feb-2021</span></li>
                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.science.org/doi/10.1126/sciimmunol.abb7221?url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org&rfr_dat=cr_pub++0pubmed&"; style="color: black; font-weight: bold; font-size: 20px">10.1126/sciimmunol.abb7221</a></li>
                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Science immunology</span></li>
                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">Human airway mast cells proliferate and acquire distinct inflammation-driven phenotypes during type 2 inflammation</span></li>
                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">AERD(n=3); CRSwNP(n=3)</span></li>
                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single-cell RNA sequencing (scRNA-seq) using the SeqWell V1 platform on sinus mast cells flow cytometrically sorted from the nasal polyps of patients with chronic rhinosinsusitis (CRS) with nasal polyps (CRSwNP) and aspirin-exacerbated respiratory disease (AERD).
</span></li>
                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002333.v1.p1"; style="color: black; font-weight: bold; font-size: 20px">phs002333</a></li>
                </ul>
            </div>

            """, unsafe_allow_html=True)

    with CNCB:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('HRA000772'
             ,))

        if option == "HRA000772":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                      <h2 style="text-align: center;">INFOS</h2>
                      <ul style="list-style: none; text-align: left;">
                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Weiqing Wang
</span></li>
                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">22-Sep-2022
</span></li>
                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.nature.com/articles/s41590-022-01312-0"; style="color: black; font-weight: bold; font-size: 20px">10.1038/s41590-022-01312-0
</a></li>
                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Nature immunology
</span></li>
                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single-cell profiling identifies mechanisms of inflammatory heterogeneity in chronic rhinosinusitis
</span></li>
                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">CRSsNP(n=5); CRSwNP(n=11); Health(n=5)
</span></li>
                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">We performed single-cell RNA-sequencing to portrait the cellular landscape, including immune cells, epithelial cells, and stromal cells of nasal mucosa from health and three CRS subtypes(CRSsNP, neCRSwNP and eCRSwNP).
</span></li>
                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://ngdc.cncb.ac.cn/gsa-human/browse/HRA000772"; style="color: black; font-weight: bold; font-size: 20px">HRA000772</a></li>
                        </ul>
                    </div>

                    """, unsafe_allow_html=True)


