import streamlit as st
import pandas as pd
import plotly.express as px

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
        weekly_sales_table = calculate_and_display_sales(filtered_df, 'WEEKLY')
        st.write(weekly_sales_table)

        # Visualization
        st.subheader("Weekly Sales Visualization")
        # Example: Line chart showing weekly sales trend
        fig = px.line(weekly_sales_table, x='Week', y='Total Sales', title='Weekly Sales Trend')
        st.plotly_chart(fig)


        # Monthly view
        st.subheader("Monthly Sales")
        monthly_sales_table = calculate_and_display_sales(filtered_df, 'MONTHLY')
        st.write(monthly_sales_table)

        # Visualization
        st.subheader("Monthly Sales Visualization")
        # Example: Line chart showing monthly sales trend
        fig = px.line(monthly_sales_table, x='Month', y='Total Sales', title='Monthly Sales Trend')
        st.plotly_chart(fig)

        # Quarterly view
        st.subheader("Quarterly Sales")
        st.subheader("Quarterly Sales")
        quarterly_sales_table = calculate_and_display_sales(filtered_df, 'QUARTERLY')
        st.write(quarterly_sales_table)

        # Visualization
        st.subheader("Quarterly Sales Visualization")
        # Example: Line chart showing quarterly sales trend
        fig = px.line(quarterly_sales_table, x='Quarter', y='Total Sales', title='Quarterly Sales Trend')
        st.plotly_chart(fig)


        # Annual view
        st.subheader("Annual Sales")
        st.subheader("Annual Sales")
        annual_sales_table = calculate_and_display_sales(filtered_df, 'ANNUAL')
        st.write(annual_sales_table)

        # Visualization
        st.subheader("Annual Sales Visualization")
        # Example: Line chart showing annual sales trend
        fig = px.line(annual_sales_table, x='Year', y='Total Sales', title='Annual Sales Trend')
        st.plotly_chart(fig)

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
def calculate_and_display_sales(df, timeframe):
    if timeframe == 'WEEKLY':
        # Example: Calculate weekly sales and display in a table
        df['Week'] = df['DATE'].dt.strftime('%U-%Y')
        weekly_sales = df.groupby('Week').sum()['TOTALS'].reset_index()
        weekly_sales.rename(columns={'TOTALS': 'Total Sales'}, inplace=True)
        return weekly_sales

def calculate_and_display_sales(df, timeframe):
    if timeframe == 'MONTHLY':
        # Example: Calculate monthly sales and display in a table
        monthly_sales = df.groupby(df['DATE'].dt.strftime('%B %Y')).sum()['TOTALS'].reset_index()
        monthly_sales.rename(columns={'TOTALS': 'Total Sales', 'DATE': 'Month'}, inplace=True)
        return monthly_sales

def calculate_and_display_sales(df, timeframe):
    if timeframe == 'QUARTERLY':
        # Example: Calculate quarterly sales and display in a table
        quarters = df['DATE'].dt.to_period('Q')
        quarterly_sales = df.groupby(quarters).sum()['TOTALS'].reset_index()
        quarterly_sales.rename(columns={'TOTALS': 'Total Sales', 'DATE': 'Quarter'}, inplace=True)
        return quarterly_sales
    
def calculate_and_display_sales(df, timeframe):
    if timeframe == 'ANNUAL':
        # Example: Calculate annual sales and display in a table
        annual_sales = df.groupby(df['DATE'].dt.year).sum()['TOTALS'].reset_index()
        annual_sales.rename(columns={'TOTALS': 'Total Sales', 'DATE': 'Year'}, inplace=True)
        return annual_sales

if __name__ == "__main__":
    main()
