import streamlit as st
import pandas as pd

st.title("📄 CSV Viewer with Sidebar Filters (Min. 5 Columns)")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if df.shape[1] < 5:
        st.error("The uploaded CSV must contain at least 5 columns.")
    else:
        # Sidebar options
        st.sidebar.header("🔧 Options")

        # Checkbox to show raw data
        show_data = st.sidebar.checkbox("Show raw data")

        # Column selector in sidebar
        column_to_filter = st.sidebar.selectbox("Filter by column:", df.columns)

        # Value selector for filtering
        unique_values = df[column_to_filter].dropna().unique()
        selected_value = st.sidebar.selectbox(f"Select value from '{column_to_filter}'", unique_values)

        # Create tabs for organizing content
        tab1, tab2 = st.tabs(["Raw Data", "Filtered Data"])

        with tab1:
            if show_data:
                st.subheader("📊 Raw Data")
                st.dataframe(df)

        with tab2:
            st.subheader("🔎 Filtered Data")
            filtered_df = df[df[column_to_filter] == selected_value]
            st.dataframe(filtered_df)

else:
    st.info("Please upload a CSV file to begin.")