import streamlit as st

# Sidebar Options
st.sidebar.title("⚙️ Display Options")
show_dw_vs_dl = st.sidebar.checkbox("Include DW vs Data Lake", True)
show_best_practices = st.sidebar.checkbox("Include Best Practices", True)
show_trends = st.sidebar.checkbox("Include Trends", True)

# Page Title
st.title("📊 Data Warehousing & Enterprise Data Management")

# Tabs for top-level navigation
tabs = ["Data Warehousing", "Enterprise Data Management"]
if show_dw_vs_dl:
    tabs.append("DW vs Data Lake")
if show_best_practices:
    tabs.append("Best Practices")
if show_trends:
    tabs.append("Trends")

tab1, tab2, *optional_tabs = st.tabs(tabs)

# Tab 1: Data Warehousing
with tab1:
    with st.expander("🔍 What is Data Warehousing?"):
        st.write("""
            Centralized storage for integrated, historical data used for reporting and analytics.

            **Key Features**:
            - Combines multiple sources
            - Supports time-based analysis
            - Optimized for querying
            - Uses ETL (Extract, Transform, Load)
        """)

    with st.expander("🏗️ Architecture Overview"):
        st.write("""
            **Layers**:
            - Data Sources (e.g., ERP, CRM)
            - ETL Layer (Talend, Informatica)
            - Data Warehouse (fact/dimension tables)
            - Data Marts (Sales, Finance)
            - OLAP Cubes for aggregation
        """)

# Tab 2: Enterprise Data Management (EDM)
with tab2:
    with st.expander("📑 What is EDM?"):
        st.write("""
            Enterprise Data Management ensures that data is accurate, consistent, and available organization-wide.

            **Core Areas**:
            - Governance & compliance
            - Integration across sources
            - Master Data Management (MDM)
            - Data quality & protection
        """)

    with st.expander("🛠️ EDM Tools"):
        st.write("""
            - **Governance**: Collibra, Alation
            - **Integration**: MuleSoft, IBM DataStage
            - **MDM**: SAP MDG, Informatica MDM
        """)

# Optional Tabs from sidebar
tab_map = {name: tab for name, tab in zip(tabs[2:], optional_tabs)}

if "DW vs Data Lake" in tab_map:
    with tab_map["DW vs Data Lake"]:
        with st.expander("📊 Comparison: DW vs Data Lake"):
            st.write("""
                **Warehouse**: Clean, structured, analytics-ready  
                **Lake**: Raw, unstructured, flexible

                **Differences**:
                - DW is optimized for BI; DL is suited for big data & ML
                - DW = Snowflake, BigQuery; DL = Amazon S3, Azure Data Lake
            """)

if "Best Practices" in tab_map:
    with tab_map["Best Practices"]:
        with st.expander("📌 Recommended Practices"):
            st.write("""
                - Clean & validate data early
                - Design for growth and performance
                - Define roles & rules (data governance)
                - Use indexing/partitioning to speed up queries
            """)

if "Trends" in tab_map:
    with tab_map["Trends"]:
        with st.expander("🔮 Emerging Trends"):
            st.write("""
                - Cloud-native data warehousing (e.g., Snowflake)
                - Real-time analytics (Kafka, Flink)
                - Data mesh architectures
                - AI for data classification & cleaning
            """)
