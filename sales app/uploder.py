import streamlit as st
import pandas as pd

def main():
    st.title("KSC Marketing - Sales Data Dashboard")

    # File upload
    uploaded_file = st.file_uploader("Upload Pulled Excel file", type="xlsx")

    if uploaded_file is not None:
        # Read data into DataFrame
        df = pd.read_excel(uploaded_file)

        # Display uploaded data
        st.write("Uploaded Data:")
        st.write(df)

if __name__ == "__main__":
    main()
