import dash_bootstrap_components as dbc

def get_navbar():
    nav = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Dashboard", href="/")),
            dbc.NavItem(dbc.NavLink("About the Data", href="/analysis"))
        ],
        brand="E-Commerce Dashboard",
        brand_href="#",
        color="#0a9396",
        dark=True,
        class_name={"margin": "-20px -20px -20px 20px"}
    )

    return nav