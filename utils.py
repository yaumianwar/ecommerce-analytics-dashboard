import pandas as pd

def approval_duration(value):
    if value == 0:
        return "same day"
    if 1 <= value <= 2:
        return "1-2 day(s)"
    elif value > 2:
        return "> 2 days"
    
def is_arrive_on_time(value):
    if value > 0:
        return "on time"
    else:
        return "not on time"
    
def get_price_range(value):
    
    if value < 100:
        return "< 100"
    elif 100 <= value < 200:
        return "100-199"
    elif 200 <= value <= 500:
        return "200-500"
    elif value > 500:
        return "> 500"


def get_order_by_time(df):
    order_by_time = df[['Order_Purchase_Timestamp']]
    order_by_time['Order_Purchase_Timestamp'] = pd.to_datetime(order_by_time['Order_Purchase_Timestamp'])
    order_by_time['hour'] = order_by_time['Order_Purchase_Timestamp'].dt.hour
    order_by_time['day_name'] = order_by_time['Order_Purchase_Timestamp'].dt.day_name() 
    order_by_time['day'] = order_by_time['Order_Purchase_Timestamp'].dt.day
    order_by_time['day_of_week'] = order_by_time['Order_Purchase_Timestamp'].dt.day_of_week
    order_by_time['date'] = order_by_time['Order_Purchase_Timestamp'].dt.date
    order_by_time['month'] = order_by_time['Order_Purchase_Timestamp'].dt.month
    order_by_time['year'] = order_by_time['Order_Purchase_Timestamp'].dt.year
    order_by_time['month_year'] = pd.to_datetime(order_by_time[['month', 'year']].assign(DAY=1))

    return order_by_time

def get_approval_duration(df):
    df['Order_Purchase_Timestamp'] = pd.to_datetime(df['Order_Purchase_Timestamp'])
    df['Order_Approved_At'] = pd.to_datetime(df['Order_Approved_At'])
    df['approval_duration'] = (df['Order_Approved_At'] - df['Order_Purchase_Timestamp']).dt.days
    order_approval_duration = df.groupby(['approval_duration']).size().reset_index(name='counts')
    order_approval_duration['duration'] = order_approval_duration['approval_duration'].map(approval_duration)

    return order_approval_duration

def get_ontime_delivery(df):
    df = df[df['Order_Delivered_Customer_Date'].notnull()]
    df['Order_Delivered_Customer_Date'] = pd.to_datetime(df['Order_Delivered_Customer_Date'])
    df['Order_Estimated_Delivery_Date'] = pd.to_datetime(df['Order_Estimated_Delivery_Date'])
    # df['time_between_delivery_estimation'] = (df['Order_Estimated_Delivery_Date'] - df['Order_Delivered_Customer_Date']).dt.days
    df.loc[:, 'time_between_delivery_estimation'] = (df['Order_Estimated_Delivery_Date'] - df['Order_Delivered_Customer_Date']).dt.days

    df['is_arrive_ontime'] = df['time_between_delivery_estimation'].map(is_arrive_on_time)
    order_by_delivery_accuracy = df.groupby(['is_arrive_ontime']).size().reset_index(name='counts')

    return order_by_delivery_accuracy

def get_order_item_product_info(order_item_df, product_df, orders_df):
    order_item_product_df = pd.merge(order_item_df, orders_df[['Order_ID','Gender', 'Age']], on='Order_ID', how='left')
    order_item_product_df = pd.merge(order_item_product_df, product_df[['Product_ID', 'Product_Category_Name']], on='Product_ID', how='left')
    order_item_product_df['price_range'] = order_item_product_df['Price'].map(get_price_range)

    return order_item_product_df