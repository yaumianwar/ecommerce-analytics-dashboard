# graph color setup
COLOR_DISCRETE_SEQUENCE = ['#0a9396','#94d2bd','#e9d8a6','#ee9b00', '#ca6702', '#bb3e03', '#ae2012']
SINGLE_GRAPH_COLOR = '#0a9396'

# graph filter/grouping option
PRODUCT_CATEGORY_FILTER_OPTION = [
    {'label': 'Overall', 'value': 'overall'},
    {'label': 'Female', 'value': 'female'},
    {'label': 'Male', 'value': 'male'},
    {'label': '< 20 Years', 'value': 'under_20'},
    {'label': '20-30 Years', 'value': '20-30'},
    {'label': '31-40 Years', 'value': '31-40'},
    {'label': '> 40 Years', 'value': 'above_40'},
]
PURCHASE_TIME_GROUPING_OPTION = [
    {'label': 'Date', 'value': 'date'},
    {'label': 'Month and Year', 'value': 'month_year'},
    {'label': 'Day', 'value': 'day_name'},
    {'label': 'Hour', 'value': 'hour'},
]

#filter mapping
GENDERS = {
    'male': {'key': 'Male'},
    'female': {'key': 'Female'}
} 
AGES = {
    'under_20': {'min': 0, 'max': 19},
    '20-30': {'min': 20, 'max': 30},
    '31-40': {'min': 31, 'max': 40},
    'above_40': {'min': 41, 'max': 100}
}

PRICE_RANGE_ORDER = ['< 100', '100-199', '200-500', '> 500']