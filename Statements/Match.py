def http_error(status):
    match status:
        case 400 | 401:
            return "Bad request"
        case 404 or 405:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"