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
    SCP, GEO, CNCB = st.tabs(['SCP', 'GEO','CNCB'])

    with SCP:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('xxxx',))


        if option == "xxxx":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Carly G K Ziegler
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">2-Sep-2021
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://linkinghub.elsevier.com/retrieve/pii/S0092-8674(21)00882-5"; style="color: black; font-weight: bold; font-size: 20px">10.1016/j.cell.2021.07.023
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Cell
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">COVID-19(n=35); Health(n=23)                
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Infection with SARS-CoV-2, the virus that causes COVID-19, can lead to severe lower respiratory illness including pneumonia and acute respiratory distress syndrome, which can result in profound morbidity and mortality. However, many infected individuals are either asymptomatic or have isolated upper respiratory symptoms, which suggests that the upper airways represent the initial site of viral infection, and that some individuals are able to largely constrain viral pathology to the nasal and oropharyngeal tissues. Which cell types in the human nasopharynx are the primary targets of SARS-CoV-2 infection, and how infection influences the cellular organization of the respiratory epithelium remains incompletely understood. Here, we present nasopharyngeal samples from a cohort of 35 individuals with COVID-19, representing a wide spectrum of disease states from ambulatory to critically ill, as well as 23 healthy and intubated patients without COVID-19. Using standard nasopharyngeal swabs, we collected viable cells and performed single-cell RNA-sequencing (scRNA-seq), simultaneously profiling both host and viral RNA. We find that following infection with SARS-CoV-2, the upper respiratory epithelium undergoes massive reorganization: secretory cells diversify and expand, and mature epithelial cells are preferentially lost. Further, we observe evidence for deuterosomal cell and immature ciliated cell expansion, potentially representing active repopulation of lost ciliated cells through coupled secretory cell differentiation. Epithelial cells from participants with mild/moderate COVID-19 show extensive induction of genes associated with anti-viral and type I interferon responses. In contrast, cells from participants with severe lower respiratory symptoms appear globally muted in their anti-viral capacity, despite substantially higher local inflammatory myeloid populations and equivalent nasal viral loads. This suggests an essential role for intrinsic, local epithelial immunity in curbing and constraining viral-induced pathology. Using a custom computational pipeline, we characterized cell-associated SARS-CoV-2 RNA and identified rare cells with RNA intermediates strongly suggestive of active replication. Both within and across individuals, we find remarkable diversity and heterogeneity among SARS-CoV-2 RNA+ host cells, including developing/immature and interferon-responsive ciliated cells, KRT13+ “hillock”-like cells, and unique subsets of secretory, goblet, and squamous cells. Finally, SARS-CoV-2 RNA+ cells, as compared to uninfected bystanders, are enriched for genes involved in susceptibility (e.g., CTSL, TMPRSS2) or response (e.g., MX1, IFITM3, EIF2AK2) to infection. Together, this work defines both protective and detrimental host responses to SARS-CoV-2, determines the direct viral targets of infection, and suggests that failed anti-viral epithelial immunity in the nasal mucosa may underlie the progression to severe COVID-19.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://singlecell.broadinstitute.org/single_cell/study/SCP1289/impaired-local-intrinsic-immunity-to-sars-cov-2-infection-in-severe-covid-19"; style="color: black; font-weight: bold; font-size: 20px">xxxx</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)


    with GEO:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ("GSE150430",))

        if option == "GSE150430":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Yu-Pei Chen
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">20-Jul-2020
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.nature.com/articles/s41422-020-0374-x"; style="color: black; font-weight: bold; font-size: 20px">10.1038/s41422-020-0374-x
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Cell research
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Single-cell transcriptomics reveals regulators underlying immune cell diversity and immune subtypes associated with prognosis in nasopharyngeal carcinoma.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">NPC(n=15); Health(n=1)                
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Nasopharyngeal carcinoma (NPC) is an aggressive malignancy with extremely skewed ethnic and geographic distributions. Increasing evidence indicates that targeting the tumour microenvironment (TME) represents a promising therapeutic approach in NPC, highlighting an urgent need to deepen the understanding of the complex NPC TME. Here, we generated single-cell transcriptome profiles for 7,581 malignant cells and 40,285 immune cells from 15 primary NPC tumours and one normal sample. We revealed malignant signatures capturing intratumoural transcriptional heterogeneity and predicting aggressiveness of malignant cells. Diverse immune cell subtypes were identified, including novel subtypes such as CLEC9A+ dendritic cells (DCs). We further revealed transcriptional regulators underlying immune cell diversity, and cell-cell interaction analyses highlighted promising immunotherapeutic targets in NPC. Moreover, we established the immune subtype-specific signatures, and demonstrated that the signatures of macrophages, plasmacytoid dendritic cells (pDCs), CLEC9A+ DCs, natural killer (NK) cells, and plasma cells were significantly associated with improved survival outcomes in NPC. Taken together, our findings represent a unique resource providing in-depth insights into the cellular heterogeneity of NPC TME and highlight potential biomarkers for anticancer treatment and risk stratification, laying a new foundation for the precision therapies in NPC.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150430"; style="color: black; font-weight: bold; font-size: 20px">GSE150430</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

    with CNCB:
        st.markdown('##### Data list:')
        option = st.selectbox(
            '',
            ('HRA000087',))

        if option == "HRA000087":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Shanzhao Jin
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">8-Sep-2020
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.nature.com/articles/s41422-020-00402-8"; style="color: black; font-weight: bold; font-size: 20px">10.1038/s41422-020-00402-8
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Cell research
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Single-cell transcriptomic analysis defines the interplay between tumor cells,viral infection, and the microenvironment in nasopharyngeal carcinoma.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">NPC(n=19); Health(n=7)               
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single-cell transcriptomic analysis defines the interplay between tumor cells, viral infection, and the microenvironment in nasopharyngeal carcinoma
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://ngdc.cncb.ac.cn/gsa-human/browse/HRA000087"; style="color: black; font-weight: bold; font-size: 20px">HRA000087</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

