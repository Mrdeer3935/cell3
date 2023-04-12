from hydralit import HydraHeadApp
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import plotly.graph_objects as go
import streamlit.components.v1 as components
class BrowseAPP(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):
        #-------------------existing untouched code------------------------------------------

        # 导入数据###
        @st.cache()
        def fetch_data():
            table = pd.read_csv("data.csv")
            return table

        @st.cache  # 添加缓存装饰
        def load_data():  #传入一个参数以区分哪一个数据;;还有可能要建立二十几个函数（缓存问题）
            df = pd.read_csv("gene.csv")
            return df


        df = fetch_data()

        # Infer basic colDefs from dataframe types
        gb = GridOptionsBuilder.from_dataframe(df)

        # customize gridOptions
        gb.configure_default_column(groupable=True, value=True, enableRowGroup=False, flex=1,
                                    floatingFilter=True,header_style={'fontWeight': 'bold', 'fontSize': '30px', 'textAlign': 'center'} )  # , editable=True,esizable: true,minWidth: 200,
        gb.configure_column("Id", type=[
            "setColumnFilter","setQuickFilter"])
        gb.configure_column("Year", type=[
            "setColumnFilter"])
        gb.configure_column("Title", type=[
            "setColumnFilter"])
        # gb.configure_column("Journal", type=[
        #     "setColumnFilter"])
        gb.configure_column("Platfrom", type=[
            "setColumnFilter"])
        gb.configure_column("Tissue", type=[
            "setColumnFilter"])
        gb.configure_column("Method", type=[
            "setColumnFilter"])
        # gb.configure_column("Sample Message",type=[
        #     "setColumnFilter"] )
        gb.configure_column("Enrichment Cell Types", type=[
            "setColumnFilter"])  # type=["dateColumnFilter","customDateTimeFormat"],custom_format_string='yyyy', pivot=True
        gb.configure_column("Cell Amount", type=["numericColumn", "numberColumnFilter", "customNumericFormat"],
                                               precision=0)  # type=["setColumnFilter"]


        # 高亮显示
        # cellsytle_jscode = JsCode("""
        #     function(params) {
        #         if (params.value == '2012') {
        #             return {
        #                 'color': 'white',
        #                 'backgroundColor': 'darkred'
        #             }
        #         } else {
        #             return {
        #                 'color': 'black',
        #                 'backgroundColor': 'white'
        #             }
        #         }
        #     };
        #     """)
        # gb.configure_column("year", cellStyle=cellsytle_jscode)


        gb.configure_selection('single', use_checkbox=True, )
        ###
        #gb.configure_grid_options(domLayout='normal',)  # 'autoHeight''print''' 整体表格的高度
        # gb.configure_pagination() #paginationAutoPageSize=True
        gridOptions = gb.build()

        # Display the grid
        col1, col2, col3 = st.columns((1, 15, 1))
        with col2:
            st.markdown("# Dataset List")

            grid_response = AgGrid(
                df,
                gridOptions=gridOptions,
                height=500,
                width='100%',
                fit_columns_on_grid_load=False,
                allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
                theme="alpine",  # material  alpine
                key='table1',
                data_return_mode="filtered_and_sorted",
                columns_auto_size_mode='ColumnsAutoSizeMode.FIT_CONTENTS',
                quick_filter=True,
            )
            # st.markdown(grid_response.selected_rows)
            if not grid_response.selected_rows :
                st.warning('Please select the dataset of your interest！')
                st.stop()
            else:

                selected = grid_response['selected_rows']
                show_id = selected[0]["Id"]
                # st.markdown(show_id)
        col5, col6, col7 = st.columns((1, 3, 1))

        with col6:
            st.subheader(f"Dataset ID: {show_id}")
            plot, plot2, table, violin = st.tabs(['UMAP PLOT', 'CELLCHAT PLOT','DIFFERENTIAL GENE EXPRESSION','GENE(X) EXPRESSION'])

            with plot:

                st.image("UMAP.png")

            with plot2:

                st.image("COM.png")

            with violin:
                gene_data = load_data()
                st.markdown('##### Please enter the gene you are interested in!')
                input = st.text_input(label="")
                if not input:
                    st.stop()
                if input not in gene_data.columns:
                    st.warning("This dataset does not contain the gene you entered")
                    st.stop()
                fig1 = go.Figure()  # 生成一个Figure对象

                cell_list = gene_data["orig.ident"].unique()
                print(cell_list)
                # 通过循环在对象上添加4个轨迹trace
                for cell in cell_list:
                    fig1.add_trace(go.Violin(
                        x=gene_data["orig.ident"][gene_data["orig.ident"] == cell],
                        y=gene_data[f"{input}"][gene_data["orig.ident"] == cell],
                        name=cell,
                        box_visible=True,
                        meanline_visible=True,
                    ))

                    fig1.update_layout(
                        width=893, height=664,
                        # title='Age of survivors vs. ages of non-survivors',
                        xaxis=dict(
                            title='Cell Type',
                            # tickfont=dict(size=14, family='Arial', color='black'),

                        ),
                        yaxis=dict(
                            title='Expression',
                            # tickfont=dict(size=14, family='Arial', color='black'),
                        ),
                        font=dict(size=12, family='Arial', color='black')
                    )

                st.plotly_chart(fig1)



