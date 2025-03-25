### E-Commerce Analytics Dashboard
*A real-time analytics dashboard for monitoring e-commerce performance.*

## Features ✨
- **Sales Trends**: Track orders and user activity over time.
- **User Insights**: Analyze customer demographics and behavior.
- **Product Performance**: Identify top-selling product categories.
- **Interactive Filters**: Slice data by selected condition.
- **Dashboard Insight**: Dashboard data storytelling.

## Tech Stack 🛠️
- **Python**: Core programming language.
- **Dash (Plotly)**: Framework for building the dashboard.
- **Pandas**: Data manipulation and analysis.
- **Docker**: Containerization for easy deployment.

## Data Source
The data used to create this dashboard was taken from [Kaggle Fecom Inc. e-Com Marketplace Orders Data ](https://www.kaggle.com/datasets/cemeraan/fecom-inc-e-com-marketplace-orders-data-crm). Fecom Inc. is a fictional e-commerce marketplace company based in Berlin, Germany. Between 2022 and 2024, it recorded 99,441 orders from 102,727 unique customers and tracked all commercial transactions of 3,095 sellers. The data contain several csv files which contain any information related to the Orders e.g Order Items, Seller, Customer, Payment and Geo Location, etc.

## Setup & Installation 🚀

### Prerequisites
- Python 3.8+
- Docker (optional, for containerization)

### Local Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ecommerce-analytics-dashboard.git
   cd ecommerce-analytics-dashboard
2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Modify app.py line 25-26**
   ```bash
   # Before
   if __name__ == "__main__":
     app.run_server(debug=True)
    
   # After
   if __name__ == "__main__":
     app.run(debug=True, host="0.0.0.0", port=8050)
5. **Run the app**
   ```bash
   python app.py
   ```
   Access the dashboard at http://localhost:8050

### Docker Deployment 🐳
1. **Build the Docker image**
   ```bash
   docker build -t ecommerce-dashboard .
2. **Run the container**
   ```bash
   docker run -d -p 8050:8050 --name dashboard-container ecommerce-dashboard
   ```
   Access the dashboard at http://localhost:8050
