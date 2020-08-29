
def parse_request_body(body):
    params = body.split("&")
    data = {}
    for param in params:
        field, value = param.split('=')
        data[field] = value
    return data