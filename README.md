markdown
# Interactive Dashboard for Monitoring Annual SAIDI Data Trends

## Overview
This project provides an interactive dashboard for visualizing and analyzing the Annual SAIDI (System Average Interruption Duration Index) data from the years 2013 to 2025. The dashboard is built using Python and Dash, enabling users to explore the dataset through interactive charts and customizable filters.

### Key Features
1. **Interactive Visualization**: Users can view SAIDI trends over the years using bar charts.
2. **Data Filtering**: Allows users to filter data by specific years for targeted analysis.
3. **Data Export**: Download options for CSV and Excel formats (to be added in future versions).
4. **Responsive Design**: Accessible on both desktop and mobile devices.

### Prerequisites
- Python 3.7+
- Pandas
- Plotly
- Dash library

### Installation
1. Clone the repository:
    bash
    git clone https://github.com/yourusername/saidi-dashboard.git
    cd saidi-dashboard
    
2. Install required dependencies:
    bash
    pip install pandas plotly dash
    
3. Add the SAIDI dataset (`SAIDI.csv`) to the project directory.

### Running the Application
1. Run the Python script:
    bash
    python app.py
    
2. Open your web browser and navigate to `http://127.0.0.1:8050/` to access the dashboard.

### Usage
- Use the dropdown menu to select specific years for analysis.
- Hover over the bars in the chart to see detailed metrics for each year.
- Use the export options (to be implemented) to download the dataset for offline analysis.

### Dataset
The dataset contains the following fields:
- **SAIDI_year**: Year of the data record.
- **SAIDI_value**: System Average Interruption Duration Index in minutes per customer.

### Future Enhancements
- Add geographical filters for more detailed analysis.
- Enable data export functionality in multiple formats.
- Integrate social media sharing options for generated visualizations.
- Include additional charts for deeper insights, such as pie charts or line graphs.

### Contribution
Contributions are welcome! Please submit a pull request or open an issue to discuss potential improvements.

### License
This project is licensed under the Open Data Commons Attribution License. See the LICENSE file for details.
