from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

def tabla(df):
    #--- Eliminar columnas internas de Streamlit
    df = df.loc[:, ~df.columns.str.contains("auto_unique_id")]

    gb = GridOptionsBuilder.from_dataframe(df)

    gb.configure_grid_options(autoSizeAllColumns=True)
    gb.configure_grid_options(domLayout='normal')
    gb.configure_default_column(maxWidth=300)

    # --- Estilo general ---
    gb.configure_default_column(
        resizable=True,
        filter=True,
        sortable=True,
        cellStyle={'fontSize': '16px'}
    )

    # --- Centrar números ---
    js_centrar = JsCode("""
        function(params) {
            return {
                'textAlign': 'center',
                'fontSize': '16px'
            }
        }
    """)

    # --- Formateador para añadir el símbolo % ---
    js_porcentaje = JsCode("""
        function(params) {
            if (params.value === null || params.value === undefined) {
                return '';
            }
            return params.value.toFixed(1) + ' %';
        }
    """)

    # --- Detectar columnas numéricas (horas, carga, capacidad) ---
    columnas_numericas = [
        col for col in df.columns 
        if any(x in col.lower() for x in ["h", "carga", "capacidad"])
    ]

    for col in columnas_numericas:
        gb.configure_column(col, cellStyle=js_centrar, headerClass="header-center")

    # --- Detectar columnas de porcentaje ---
    columnas_porcentaje = [
        col for col in df.columns 
        if "%" in col or "ocup" in col.lower() or "disponibilidad" in col.lower()
    ]

    for col in columnas_porcentaje:
        gb.configure_column(
            col,
            cellStyle=js_centrar,
            headerClass="header-center",
            valueFormatter=js_porcentaje
        )

    # --- Coloración para ocupación ---
    js_color = JsCode("""
        function(params) {
            let style = { 'fontSize': '16px', 'textAlign': 'center' };

            if (params.value < 50) {
                style.backgroundColor = '#b6f2b6';
            } else if (params.value < 80) {
                style.backgroundColor = '#fff3b0';
            } else {
                style.backgroundColor = '#f7b2b0';
            }

            return style;
        }
    """)

    for col in columnas_porcentaje:
        if "ocup" in col.lower():
            gb.configure_column(col, cellStyle=js_color, headerClass="header-center")

    grid_options = gb.build()

    # --- CSS para centrar encabezados ---
    custom_css = {
        ".ag-header-cell-label": {
            "justify-content":"center !important",
            "font-size":"16px !important"
        }
    }

    AgGrid(
        df,
        gridOptions=grid_options,
        custom_css=custom_css,
        fit_columns_on_grid_load=True,
        allow_unsafe_jscode=True,
        height=200
    )
