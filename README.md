# Summary
Use this package with your Centric Engineers tools to acquire user data from centricengineers.com.

# Usage
For example, in a Dash-Plotly application.

```python
import dash
from dash import dcc, html, Input, Output
from ce_tool import validator
from ce_tool.website import AccessLevel

tool_id = 'a_tool_id'

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='content'),
])


@app.callback(Output('content', 'children'),
              [Input('url', 'search')])
def display_content_based_on_access(search: str):
    validator.website.login('username', 'password')
    access_level = validator.get_access_level(search, tool_id)
    if access_level == AccessLevel.PAID:
        return html.H1("This is paid content.")
    else:
        return html.H1("This is free content.")
```