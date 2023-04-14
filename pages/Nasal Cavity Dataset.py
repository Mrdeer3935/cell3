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

        #hc.info_card(title='Some heading GOOD', content='All''\n good!', bar_value=100,key=1)

        if option == "EGAD00001005714":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                      <h2 style="text-align: center;">INFOS</h2>
                                      <ul style="list-style: none; text-align: left;">
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Marie Deprez
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">28-Jul-2020
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.atsjournals.org/doi/10.1164/rccm.201911-2199OC?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed"; style="color: black; font-weight: bold; font-size: 20px">10.1164/rccm.201911-2199OC
                </a></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">American journal of respiratory and critical care medicine
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">A single-cell atlas of the human healthy airways
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">Health(n=7)
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single cell atlas of human airways from 10 healthy volunteers by 10X Genomics 3’ RNA-seq profiling. 77,969 cells were collected by bronchoscopy at 35 distinct locations, from the nose to the 12th division of the airway tree, either by forceps (46,791 cells), or brush biopsies (31,178 cells).
        </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://ega-archive.org/datasets/EGAD00001005714"; style="color: black; font-weight: bold; font-size: 20px">EGAD00001005714</a></li>
                                        </ul>
                                    </div>""", unsafe_allow_html=True)
        if option == "EGAD00001008560":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                      <h2 style="text-align: center;">INFOS</h2>
                                      <ul style="list-style: none; text-align: left;">
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Riikka Lampinen
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">15-Feb-2022
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.mdpi.com/2073-4409/11/4/676"; style="color: black; font-weight: bold; font-size: 20px">10.3390/cells11040676
                </a></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Cells
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single-Cell RNA-Seq Analysis of Olfactory Mucosal Cells of Alzheimer’s Disease Patients
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">AD(n=12); Health(n=11)
                </span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">The sample AD_Library_1, AD_Library_2 and Control_Library were run on a Chromium Chip B with the Chromium Single Cell 3′ Library & Gel Bead Kit v3 kit (10x Genomics, CA, USA) . The 3’ gene expression libraries were sequenced at an approximate depth of 50,000 reads per cell using the NovaSeq 6000 S1 (Illumina, San Diego, CA, USA) flow cells. Cell Ranger v.3.0.2 was used to analyze the raw base call files. FASTQ files and raw gene-barcode matrices were generated and aligned human genome GRCh37 (hg19). The samples were integrated in R v.4.0.3 and generated Seurat objects, two related to AD samples and one to control samples, were analyzed using the Seurat package v.4.0.3 to perform downstream analysis, clustering of the cells and differential expression.
</span></li>
                                        <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://ega-archive.org/datasets/EGAD00001008560"; style="color: black; font-weight: bold; font-size: 20px">EGAD00001008560</a></li>
                                        </ul>
                                    </div>""", unsafe_allow_html=True)

        if option == "EGAD00001008159":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Catherine F Hatton
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">7-Dec-2021
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.nature.com/articles/s41467-021-27318-0"; style="color: black; font-weight: bold; font-size: 20px">10.1038/s41467-021-27318-0
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Nature communications
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">Delayed induction of type I and III interferons mediates nasal epithelial cell permissiveness to SARS-CoV-2
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">SARS-CoV2(n=24)
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single cell RNA sequence generated from human primary nasal epithelium differentiated at air-liquid interface. This dataset comprises tissue from two donors, with cultures either unexposed or exposed to SARS-CoV2. Libraries were prepared using the 10X Genomics pipeline as per manufacturer's instructions.
                </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://ega-archive.org/datasets/EGAD00001008159"; style="color: black; font-weight: bold; font-size: 20px">EGAD00001008159</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)


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

        if option == "GSE184117":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Allison D Oliva
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">6-Jan-2022
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.jci.org/articles/view/155506"; style="color: black; font-weight: bold; font-size: 20px">10.1172/JCI155506
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">The Journal of clinical investigation
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">Aging-related olfactory loss is associated with olfactory stem cell transcriptional alterations in humans
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">Presbyosmia(n=6); Health(n=1)
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single cell 3' RNAseq of olfactory epithelium from 6 adult human patients (3 normosmic subjects, based on psychophysical olfactory assessment, with SIT scores 34 – 37; 3 presbyosmic subjects, SIT scores 11 - 29 and age >65 years) using the 10X Genomics Chromium platform and sequenced on Illumina Nextseq 500.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/geo/query/acc.cgi?acc=GSE184117"; style="color: black; font-weight: bold; font-size: 20px">GSE184117</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE182475":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Akshamal M Gamage
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">18-Jan-2022
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://journals.asm.org/doi/10.1128/mbio.03436-21?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed"; style="color: black; font-weight: bold; font-size: 20px">10.1128/mbio.03436-21
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">mBio
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold; font-size: 20px">Human Nasal Epithelial Cells Sustain Persistent SARS-CoV-2 Infection In Vitro, despite Eliciting a Prolonged Antiviral Response
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">SARS-CoV-2(n=2); Health(n=1)
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single Cell Sequencing of SARS-CoV2 Infected Human Nasal Epithelial Cells
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE182475"; style="color: black; font-weight: bold; font-size: 20px">GSE182475</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE139522":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Rhea Choi
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">10-Oct-2020
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://onlinelibrary.wiley.com/doi/10.1002/lio2.472"; style="color: black; font-weight: bold; font-size: 20px">10.1002/lio2.472
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Laryngoscope investigative otolaryngology
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">On the in vivo origin of human nasal mesenchymal stem cell cultures
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">Adult patients(n=2)
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single cell 3' RNAseq of olfactory epithelium from 2 patients and respiratory epithelium from 2 patients using the 10X Genomics Chromium platform and sequenced on Illumina Nextseq 500.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE139522"; style="color: black; font-weight: bold; font-size: 20px">GSE139522</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE121600":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Sandra Ruiz García
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">23-Oct-2019
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://journals.biologists.com/dev/article/146/20/dev177428/224374/Novel-dynamics-of-human-mucociliary"; style="color: black; font-weight: bold; font-size: 20px">10.1242/dev.177428
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Development (Cambridge, England)
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Novel dynamics of human mucociliary differentiation revealed by single-cell RNA sequencing of nasal epithelial cultures
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">Health(n=3)
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single-cell RNA-seq of airway epithelial cells from various origins: human in vitro time course differentiation, human bronchial biopsy, human nasal brushing, human nasal turbinate, mouse in vitro differentiation and pig trachea.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121600"; style="color: black; font-weight: bold; font-size: 20px">GSE121600</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE191061":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Alekh Paranjapye
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">18-May-2022
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://linkinghub.elsevier.com/retrieve/pii/S0171-9335(22)00034-6"; style="color: black; font-weight: bold; font-size: 20px">10.1016/j.ejcb.2022.151231
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">European journal of cell biology
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Cell function and identity revealed by comparative scRNA-seq analysis in human nasal, bronchial and epididymis epithelia
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">CF(n=3); Health(n=2)                  
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Cell function and identity revealed by comparative scRNA-seq analysis in human nasal, bronchial and epididymis epithelia.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE191061"; style="color: black; font-weight: bold; font-size: 20px">GSE191061</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE155113":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Ji Hoon Ahn
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">1-Jul-2021
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.jci.org/articles/view/148517"; style="color: black; font-weight: bold; font-size: 20px">10.1172/JCI148517
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">The Journal of clinical investigation
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Nasal ciliated cellsare primary targets for SARS-CoV-2 replication in the early stage of COVID-19
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">Pituitary adenoma(n=1)                  
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Understanding on pathogenesis of COVID-19 is rapidly growing, but primary target cells of SARS-CoV-2 infection is still not known. Here, we performed single cell RNA sequencing on human nasal mucosa tissue to investigate the expression patterns of host cell entry factors of SARS-CoV-2.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE155113"; style="color: black; font-weight: bold; font-size: 20px">GSE155113</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE171488":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Ji Hoon Ahn
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">1-Jul-2021
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.jci.org/articles/view/148517"; style="color: black; font-weight: bold; font-size: 20px">10.1172/JCI148517
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">The Journal of clinical investigation
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Nasal ciliated cellsare primary targets for SARS-CoV-2 replication in the early stage of COVID-19
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">Health(n=2)                 
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Understanding on pathogenesis of COVID-19 is rapidly growing, but primary target cells of SARS-CoV-2 infection is still not known. Here, we performed single cell RNA sequencing on human nasal swab from healthy donors to investigate the expression patterns of host cell entry factors of SARS-CoV-2.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171488"; style="color: black; font-weight: bold; font-size: 20px">GSE171488</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE164547":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Ji Hoon Ahn
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">1-Jul-2021
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.jci.org/articles/view/148517"; style="color: black; font-weight: bold; font-size: 20px">10.1172/JCI148517
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">The Journal of clinical investigation
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Nasal ciliated cellsare primary targets for SARS-CoV-2 replication in the early stage of COVID-19
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">COVID-19(n=6)                 
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Understanding on pathogenesis of COVID-19 is rapidly growing, but primary target cells of SARS-CoV-2 infection is still not known. Here, we performed single cell RNA sequencing on human nasal swab from COVID-19 patient to investigate the expression patterns of host cell entry factors of SARS-CoV-2.
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE164547"; style="color: black; font-weight: bold; font-size: 20px">GSE164547</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE162864":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Konner Winkley
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">5-Aug-2021
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.nature.com/articles/s41598-021-95532-3"; style="color: black; font-weight: bold; font-size: 20px">10.1038/s41598-021-95532-3
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Scientific reports
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">Immune cell residency in the nasal mucosa may partially explain respiratory disease severity across the age range
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">Influenza B(n=2); Health(n=21)                
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single-cell RNA-sequencing of the nasal mucosa across the lifespan
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162864"; style="color: black; font-weight: bold; font-size: 20px">GSE162864</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)

        if option == "GSE103518":
            st.markdown("""<div style="background-color: #4169E1; width: 100%; padding: 20px; border-radius: 20px;">
                                              <h2 style="text-align: center;">INFOS</h2>
                                              <ul style="list-style: none; text-align: left;">
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">First author: </strong><span style="color: white; font-weight: bold; font-size: 20px">Diego R Revinski
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Date: </strong><span style="color: white; font-weight: bold; font-size: 20px">7-Nov-2018
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">DOI: </strong><a href="https://www.nature.com/articles/s41467-018-06768-z"; style="color: black; font-weight: bold; font-size: 20px">10.1038/s41467-018-06768-z
                        </a></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Journal: </strong><span style="color: white; font-weight: bold; font-size: 20px">Nature Comunications
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Title: </strong><span style="color: white; font-weight: bold;font-size: 20px">CDC20B is required for deuterosome-mediated centriole production in multiciliated cells
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Sample: </strong><span style="color: white; font-weight: bold; font-size: 20px">Nasal obstruction(n=1)                
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Study description: </strong><span style="color: white; font-weight: bold; font-size: 20px">Single-cell RNA-seq of human airway epithelial cells
                        </span></li>
                                                <li><strong style="color: black; font-weight: bold; font-size: 20px;">Accession processed data: </strong><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103518"; style="color: black; font-weight: bold; font-size: 20px">GSE103518</a></li>
                                                </ul>
                                            </div>""", unsafe_allow_html=True)
