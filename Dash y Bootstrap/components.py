from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# Navbar 
def navbar():
    return(
        dbc.NavbarSimple(
            children=[
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("How it works", href='#'),
                        dbc.DropdownMenuItem("The statiscits", href='#'),
                    ],
                    nav=True,
                    in_navbar=True,
                    label='Explore'
                )
            ],
            brand = 'Dashboard',
            brand_href = '#',
            color='dark',
            dark=True
        )
    )

# Carousel
def carousel():
    return(
        dbc.Carousel(
            items=[
                {"key": "1", "src": "https://cdn.pixabay.com/photo/2018/05/14/16/54/cyber-3400789_1280.jpg"},
                {"key": "2", "src": "https://cdn.pixabay.com/photo/2018/05/14/16/54/cyber-3400789_1280.jpg"},
                {"key": "3", "src": "https://cdn.pixabay.com/photo/2018/05/14/16/54/cyber-3400789_1280.jpg"},
            ],
            controls=True,
            indicators=True,
            className='p-4'
        )
    )

# Card
def card(title):
    return(
        dbc.Card(
            [
                dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                dbc.CardBody(
                    [
                        html.H4(f"{title}", className="card-title"),
                        html.P(
                            "Some quick example text to build on the card title and "
                            "make up the bulk of the card's content.",
                            className="card-text",
                        ),
                        dbc.Button("Go somewhere", color="primary"),
                    ]
                ),
            ],
            style={"width": "18rem"},
            className='m-2'
        )

    )
