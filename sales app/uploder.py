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

# Sidebar filters
        branch_filter = st.sidebar.multiselect("Select Branch", df['BRANCH'].unique())
        crop_filter = st.sidebar.multiselect("Select Crop", df['CROP'].unique())

        # Filter data based on user selections
        filtered_df = df[df['BRANCH'].isin(branch_filter) & df['CROP'].isin(crop_filter)]

        # Dashboard components
        # Daily view
        st.subheader("Daily Sales")
        # Add code to display daily sales data
         # Table displaying daily sales data
        daily_sales_table = filtered_df.set_index('DATE')[['BRANCH', 'CROP', 'TOTALS']].sort_index(ascending=True)
        st.write(daily_sales_table)

        # Visualization
        st.subheader("Visualization - Daily Sales")
        # Line chart showing daily sales data
        fig = px.line(daily_sales_table, x=daily_sales_table.index, y='TOTALS', color='BRANCH', title='Daily Sales Over Time')
        fig.update_layout(xaxis_title='Date', yaxis_title='Sales', legend_title='Branch')
        st.plotly_chart(fig)


        # Weekly view
        st.subheader("Weekly Sales")
        # Add code to display weekly sales data

        # Monthly view
        st.subheader("Monthly Sales")
        # Add code to display monthly sales data

        # Quarterly view
        st.subheader("Quarterly Sales")
        # Add code to display quarterly sales data

        # Annual view
        st.subheader("Annual Sales")
        # Add code to display annual sales data

        # Visualization
        st.subheader("Visualization")
        # Example: Line chart showing total sales over time
        fig = px.line(filtered_df, x='MONTH', y='TOTALS', color='BRANCH', title='Total Sales Over Time')
        st.plotly_chart(fig)

        # Aggregate Metrics
        st.subheader("Aggregate Metrics")
        # Example: Calculate total sales by branch and display as a table
        total_sales_by_branch = filtered_df.groupby('BRANCH')['TOTALS'].sum().reset_index()
        st.write(total_sales_by_branch)

        # Export Functionality
        st.subheader("Export Data")
        export_format = st.selectbox("Select export format", ["CSV", "Excel"])
        if st.button("Export Data"):
            if export_format == "CSV":
                csv_data = filtered_df.to_csv(index=False)
                st.download_button(label="Download CSV", data=csv_data, file_name="filtered_data.csv", mime="text/csv")
            elif export_format == "Excel":
                excel_data = filtered_df.to_excel(index=False)
                st.download_button(label="Download Excel", data=excel_data, file_name="filtered_data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
    main()
