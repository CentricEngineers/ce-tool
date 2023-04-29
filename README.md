# Summary
Use this package with your Centric Engineers tools to acquire user data from centricengineers.com.

# Usage

## Single Page Dash App
In a simple single page Dash-Plotly application.

```python
import dash
from dash import dcc, html, Input, Output
from ce_tool import validator
from ce_tool.website import AccessLevel

USER_PAID = False
TOOL_ID = 'a_tool_id'

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='content'),
])


@app.callback(Output('content', 'children'),
              [Input('url', 'search')])
def display_content_based_on_access(search: str):
    validator.website.login('username', 'password')
    url_vars = validator.parse_url_params(search)
    access_level = validator.get_access_level(url_vars, TOOL_ID)
    if access_level == AccessLevel.PAID:
        global USER_PAID
        USER_PAID = True
        layout = html.Div([html.H1(["Paid Content"])])
    else:
        layout = html.Div([html.H1(["Free Content"])])
    return layout
```

## Mult-Page Dash App
In a multi-page Dash-Plotly application (using pages).

### app.py
```python
import dash
from dash import html, dcc

USER_PAID = False
TOOL_ID = 'a_tool_id'
APP_TITLE = "Dash App"

app = dash.Dash(
    __name__,
    title=APP_TITLE,
    use_pages=True,  # New in Dash 2.7 - Allows us to register pages
)

app.layout = html.Div([dash.page_container])

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
```

### home.py
```python
import app
from dash import html, register_page
from ce_tool import validator
from ce_tool.website import AccessLevel


register_page(
    __name__,
    name='Home',
    path='/'
)


def layout(**url_vars):
    validator.website.login('username', 'password')
    access_level = validator.get_access_level(url_vars, app.TOOL_ID)
    if access_level == AccessLevel.PAID:
        app.USER_PAID = True
        layout = html.Div([html.H1(["Paid Content"])])
    else:
        layout = html.Div([html.H1(["Free Content"])])
    return layout
```
