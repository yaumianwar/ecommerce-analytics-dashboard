# About the Data

---

## Summary
The data used to create this dashboard was taken from [Kaggle Fecom Inc. e-Com Marketplace Orders Data ](https://www.kaggle.com/datasets/cemeraan/fecom-inc-e-com-marketplace-orders-data-crm). Fecom Inc. is a fictional e-commerce marketplace company based in Berlin, Germany. Between 2022 and 2024, it recorded 99,441 orders from 102,727 unique customers and tracked all commercial transactions of 3,095 sellers. The data contain several csv files which contain any information related to the Orders e.g Order Items, Seller, Customer, Payment and Geo Location, etc.

This dashboard is made using [Python Dash](https://dash.plotly.com/) and Pandas to process and manipulate the data. Dash is an open-source Python framework for building data visualization interfaces. Dash is built on top of Plotly.js, React, and Flask. A Minimal dash app contains Layout and Callback. Layout contains HTML components to configure our application view, layout, and style. We also can use additional bootstrap components to improve our application layout and style. Callback is used to make our dashboard more interactive by capturing every event on the layout component like dropdown, radio, slider, etc.

Github Repository: https://github.com/yaumianwar/ecommerce-analytics-dashboard

---

## Dashboard Overview
Welcome to the E-Commerce Dashboard! This dashboard provides a snapshot of key performance metrics to help you understand business performance at a glance.
##### Key Highlights :
+ Total Orders: **99,441** recorded with total **112,650** items and **13,591,644** euro total money spent
+ Users: **102,727** unique customers and **3,095** sellers
+ Average Order: There are around **157** orders recorded every day

##### Most Popular Product
Bed Bad Table, Healthy Beauty, Sport Leisure, Furniture Door, and Computer Accecoris is the top 5 most frequently purchased product category by customers of all ages and genders. Contributing 40.5% of total orders items. 

##### Product Price
Customers of all ages and genders tend to buy product that cost under 100 euro and contributing around 60% of the total orders items. Product that cost > 500 euro rarely purchased.

##### Purchase Trend
Around the of of 2022 until before end of November 2023, total orders are increasing with an average of around 100 orders per day. At November 24, 2023 there was a spike in orders with a total of 1.176 orders. After that, orders increased to around 200-300 orders per day.If there is an event held on that date, then the event will successfully increase the total orders. Customers seems to like make purchase at weekday especially at 10.00 AM - 09.00 PM.

#### Buyer Information
Most customers are 20-40 years old, but there is no significant difference in the number of male and female customers. Since the marketplace company is based in Berlin, Germany. Most customers come from Germany and 42% of orders come from this country. Another country (France and Netherlands) that has the largest total orders is also a neighboring country to Germany. This country can be a consideration if the company wants to expand its business.

Most customers purchase orders using credit cards and only 5% use vouchers as payment. Further analysis can be done to see whether the spike in transactions on November 24, 2023 was related to the use of vouchers or not.

#### Performance
82% of orders were approved on the same day as payment and the other 12% were approved around 1-2 day(s). Delivery accuracy also showed good performance, with 90% of orders arriving before the estimated arrival time. Some customers are satisfied with their orders by giving 4 and 5 stars. But around 15% of reviews give 1 star, which is more than those who gave 2 or 3 stars. We need to identify those ratings for better problem-handling.