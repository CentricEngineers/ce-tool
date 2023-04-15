from ce_tool import validation


def parse_url_params(params: str) -> dict:
    """ parse url params into dict """
    return dict(arg_pair.split('=') for arg_pair in params[1:].split('&'))


def get_access_level(url_params: str, tool_id: str) -> validation.AccessLevel:
    """ Example: url_params='?a=test&b=pass' """
    url_vars = parse_url_params(url_params)
    user_id = url_vars['u']  # `u` varname is set by centricengineers.com
    return validation.validate_user(user_id, tool_id)



