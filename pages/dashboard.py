import dash
import pandas as pd
from component.card import get_card_component
import plotly.express as px
import plotly.graph_objects as go

from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from constants import AGES, COLOR_DISCRETE_SEQUENCE, GENDERS, PRICE_RANGE_ORDER, PRODUCT_CATEGORY_FILTER_OPTION, PURCHASE_TIME_GROUPING_OPTION, SINGLE_GRAPH_COLOR
from utils import get_approval_duration, get_ontime_delivery, get_order_item_product_info, get_order_time_info

dash.register_page(__name__, path='/')
pd.options.mode.chained_assignment = None

sellers_df = pd.read_csv('data/Fecom Inc Sellers List.csv', delimiter=';')
customers_df = pd.read_csv('data/Fecom Inc_Customer_List.csv', delimiter=';')
raw_orders_df = pd.read_csv('data/Fecom Inc Orders.csv', delimiter=';')
products_df = pd.read_csv('data/Fecom Inc Products.csv', delimiter=';')
order_items_df = pd.read_csv('data/Fecom Inc Order Items.csv', delimiter=';')
orader_payments_df = pd.read_csv('data/Fecom Inc Order Payments.csv', delimiter=';')
order_reviews_df = pd.read_csv('data/Fecom_Inc_Order_Reviews_No_Emojis.csv', delimiter=';')
customer_location_df = pd.read_csv('data/Fecom Inc Geolocations.csv', delimiter=';')

# get order user, location, review and payment info
customer_location_df = pd.merge(customers_df, customer_location_df[['Geo_Postal_Code', 'Geo_Lat', 'Geo_Lon', 'Geolocation_City']], left_on='Customer_Postal_Code',right_on='Geo_Postal_Code', how='left')
orders_df = pd.merge(raw_orders_df, customer_location_df[['Customer_Trx_ID', 'Geo_Postal_Code', 'Geo_Lat', 'Geo_Lon', 'Age', 'Gender', 'First_Order_Date', 'Customer_Country', 'Customer_City', 'Geolocation_City']], on='Customer_Trx_ID', how='left')
orders_df = pd.merge(orders_df, orader_payments_df[['Order_ID', 'Payment_Type']], on='Order_ID', how='left')
orders_df = pd.merge(orders_df, order_reviews_df[['Order_ID', 'Review_Score']], on='Order_ID', how='left')
orders_with_time_info_df = get_order_time_info(orders_df)
orders_by_date = orders_with_time_info_df.groupby(['date']).size().reset_index(name='counts')

# approval duration
order_approval_duration = get_approval_duration(orders_df)

# on-time delivery
order_by_delivery_accuracy = get_ontime_delivery(orders_df)

# customer location
customer_by_location = orders_df.groupby(['Customer_Country']).size().reset_index(name='counts').sort_values(by=['counts'], ascending=False).head(5)
customer_by_city = orders_df.groupby(['Geo_Lon', 'Geo_Lat', 'Geolocation_City']).size().reset_index(name='counts')
customer_by_city['Geo_Lon'] = pd.to_numeric(customer_by_city['Geo_Lon'].str.replace(',', '.', regex=False), errors='coerce')
customer_by_city['Geo_Lat'] = pd.to_numeric(customer_by_city['Geo_Lat'].str.replace(',', '.', regex=False),errors='coerce')

customer_geo_location_fig = go.Figure(data=go.Scattergeo(
    lon=customer_by_city['Geo_Lon'],
    lat=customer_by_city['Geo_Lat'],
    text = customer_by_city['Geolocation_City'],
    mode='markers',
    marker_color=customer_by_city['counts']
))

customer_geo_location_fig.update_layout(geo_scope='europe',height=500, margin={"r":0,"t":0,"l":0,"b":0})

# customer age and gender
customer_by_gender = orders_df.groupby(['Gender']).size().reset_index(name='counts')
customer_by_age = orders_df.groupby(['Age']).size().reset_index(name='counts').sort_values(by=['Age'])

# order review
order_score_review = orders_df.groupby(['Review_Score']).size().reset_index(name='counts').sort_values(by=['Review_Score'])
order_score_review['Review_Score'] = order_score_review['Review_Score'].astype(str)

# order_seller
order_seller_df = pd.merge(order_items_df, sellers_df[['Seller_ID', 'Seller_Name']], on='Seller_ID', how='left')
order_seller_df = order_seller_df.groupby(['Seller_Name']).size().reset_index(name='counts').sort_values(by=['counts'], ascending=False).head(10)

# customer first order date
order_by_payment_type = orders_df.groupby(['Payment_Type']).size().reset_index(name='counts')

layout = html.Div(children=[

    # summary
    dbc.Row([
        get_card_component('Total Orders', '{:,}'.format(len(orders_df.index))),
        get_card_component('Total Order Items', '{:,}'.format(len(order_items_df.index))),
        get_card_component('Avg Order/Day', '{:,}'.format(round(orders_by_date['counts'].mean()))),
        get_card_component('Total Money Spent', '{:,}'.format(round(order_items_df['Price'].sum()))),
        get_card_component('Total Seller', '{:,}'.format(len(sellers_df.index))),
        get_card_component('Total Customers', '{:,}'.format(len(customers_df.index))),
        
    ]),

    # ORDER SECTION


    # Top 10 Product Category
    dbc.Row(
        dbc.Col([
            html.H4("Top 5 Product Category"),
            html.Div(
                dbc.RadioItems(
                    id="category-radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-dark",
                    labelCheckedClassName="active",
                    options=PRODUCT_CATEGORY_FILTER_OPTION,
                    value='overall',
                ),
                className ="radio-group",
                style = {'margin-top': '20px'}
            ),
            dcc.Graph(figure={}, id='top-5-category-barchart')
        ]),
    ),
    # Other Product Category
    dbc.Row([
        dbc.Col([
            html.H4("Product Price"),
            dcc.Graph(figure={}, id="price-range-barchart")
        ]),
        dbc.Col([
            html.H4("Product Category"),
            dcc.Graph(figure={}, id="product-category-barchart")
        ]),
    ]),

    # Order Purchase Time
    dbc.Row(
        dbc.Col([
            html.H4("Purchase Time"),
            html.Div(
                dbc.RadioItems(
                    id="order-purchase-time-radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-dark",
                    labelCheckedClassName="active",
                    options=PURCHASE_TIME_GROUPING_OPTION,
                    value='date',
                ),
                className ="radio-group",
                style = {'margin-top': '20px'}
            ),
            dcc.Graph(figure={}, id="order-purchase-time-linechart")
        ])
    ),

    dbc.Row([
        dbc.Col([
            html.H4("Age"),
            dcc.Graph(figure=px.line(customer_by_age, x='Age', y='counts', color_discrete_sequence=COLOR_DISCRETE_SEQUENCE))
        ]),
        dbc.Col([
            html.H4("Gender"),
            dcc.Graph(figure=px.pie(customer_by_gender, names='Gender', values='counts', color='Gender', color_discrete_sequence=COLOR_DISCRETE_SEQUENCE, hole=.3))
        ]),
    ]),

    # Customer 
    dbc.Row([
        dbc.Col([
            html.H4("Top 5 Country"),
            dcc.Graph(figure=px.bar(customer_by_location, x='Customer_Country', y='counts', color='Customer_Country',color_discrete_sequence=COLOR_DISCRETE_SEQUENCE))
        ]),
        dbc.Col([
            html.H4("Top 5 City"),
            dcc.Graph(figure=px.bar(customer_by_city.sort_values(by=['counts'], ascending=False).head(5), x='Geolocation_City', y='counts', color='Geolocation_City',color_discrete_sequence=COLOR_DISCRETE_SEQUENCE))
        ]),
        dbc.Col([
            html.H4("Geo Location"),
            dcc.Graph(figure=customer_geo_location_fig)
        ]),
    ]),


    # Order Approval Duration and On-Time Delivery
    dbc.Row([
        dbc.Col([
            html.H4("Approval Duration"),
            dcc.Graph(figure=px.bar(order_approval_duration, x='duration', y='counts', color='duration', color_discrete_sequence=COLOR_DISCRETE_SEQUENCE))
        ]),
        dbc.Col([
            html.H4("On-Time Order Delivery"),
            dcc.Graph(figure=px.pie(order_by_delivery_accuracy, names='is_arrive_ontime', values='counts', color='is_arrive_ontime', color_discrete_sequence=COLOR_DISCRETE_SEQUENCE, hole=.3))
        ]),
    ]),

    # Top Seller and Score Review
    dbc.Row([
        dbc.Col([
            html.H4("Score Review"),
            dcc.Graph(figure=px.bar(order_score_review, x='Review_Score', y='counts', color='Review_Score', color_discrete_sequence=COLOR_DISCRETE_SEQUENCE))
        ]),
        dbc.Col([
            html.H4("Payment Type"),
            dcc.Graph(figure=px.pie(order_by_payment_type, names='Payment_Type', values='counts', color='Payment_Type', color_discrete_sequence=COLOR_DISCRETE_SEQUENCE, hole=.3))
        ]),
    ]),

    
])

# Order Purchase Time Callback
@callback(
    Output("order-purchase-time-linechart", "figure"), 
    Input("order-purchase-time-radios", "value")
)
def update_order_purchase_time_linechart(value):
    orders_by_purchase_time = orders_with_time_info_df.groupby([value]).size().reset_index(name='counts')

    if value == 'day_name':
        orders_by_purchase_time = orders_with_time_info_df.groupby(['day_name', 'day_of_week']).size().reset_index(name='counts').sort_values(by=['day_of_week'])

    figure=px.line(orders_by_purchase_time, x=value, y='counts', color_discrete_sequence=[SINGLE_GRAPH_COLOR])
    
    return figure

# Top 10 Category and Price Callback
@callback(
    Output("top-5-category-barchart", "figure"), 
    Output("price-range-barchart", "figure"), 
    Output("product-category-barchart", "figure"), 
    Input("category-radios", "value")
)
def update_top_category_barchart(value):
    # get order product category and customer info
    order_item_products_df = get_order_item_product_info(order_items_df, products_df, orders_df)

    if value != 'overall':
        if value in list(GENDERS.keys()):
            order_item_products_df = order_item_products_df[order_item_products_df['Gender'] == GENDERS[value]['key']]
        elif value in list(AGES.keys()):
            order_item_products_df = order_item_products_df[(order_item_products_df['Age'] >= AGES[value]['min']) & (order_item_products_df['Age'] <= AGES[value]['max'])]

    order_by_product_category = order_item_products_df.groupby(['Product_Category_Name']).size().reset_index(name='counts')

    # product price range
    order_by_price_range = order_item_products_df.groupby(['price_range']).size().reset_index(name='counts')
    order_by_price_range['price_range'] = pd.Categorical(order_by_price_range['price_range'], categories=PRICE_RANGE_ORDER, ordered=True)

    top_5_product_category = order_by_product_category.sort_values(by=['counts'], ascending=False).head(5)
    other_product_category = order_by_product_category.sort_values(by=['counts'], ascending=False)[5:]
    total_null_product_category = len(order_item_products_df[order_item_products_df['Product_Category_Name'].isnull()].index)

    product_category_percentage = pd.DataFrame({
        'Name': ['Top 5', 'Other Category', 'Empty Value'],
        'Total': [top_5_product_category['counts'].sum(), other_product_category['counts'].sum(), total_null_product_category]
    })

    top_5_figure = px.bar(top_5_product_category, x='Product_Category_Name', y='counts', color='Product_Category_Name', color_discrete_sequence=COLOR_DISCRETE_SEQUENCE)
    price_range_figure = px.bar(order_by_price_range.sort_values('price_range'), x='price_range', y='counts', color='price_range',color_discrete_sequence=COLOR_DISCRETE_SEQUENCE)
    product_category_figure = px.pie(product_category_percentage, names='Name', values='Total', color='Name', color_discrete_sequence=COLOR_DISCRETE_SEQUENCE, hole=.3)

    return top_5_figure, price_range_figure, product_category_figure