from ce_tool import website


def has_vars(params: str) -> bool:
    return '=' in params


def parse_url_params(params: str) -> dict:
    """ parse url params into dict """
    if not has_vars(params):
        return dict()
    return dict(arg_pair.split('=') for arg_pair in params[1:].split('&'))


def get_access_level(url_params: str, tool_id: str) -> website.AccessLevel:
    """ Example: url_params='?a=test&b=pass' """
    url_vars = parse_url_params(url_params)
    user_id = url_vars.get('u')  # `u` varname is set by centricengineers.com
    return website.validate_user(user_id, tool_id)



