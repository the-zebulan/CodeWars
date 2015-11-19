def strip_url_params(url, params=()):
    try:
        u, p = url.split('?')
        params = set(params)  # parameter keys
        unique_params = []    # unique whole parameters (in order)
        for param in p.split('&'):
            k, _ = param.split('=')
            if k not in params:
                unique_params.append(param)
            params.add(k)
        if unique_params:
            return '{}?{}'.format(u, '&'.join(unique_params))
    except ValueError:
        pass
    return url


assert strip_url_params('www.codewars.com?a=1&b=2&a=1&b=3') \
    == 'www.codewars.com?a=1&b=2'
assert strip_url_params('www.codewars.com?a=1&b=2&a=1&b=3', ['b']) \
    == 'www.codewars.com?a=1'
assert strip_url_params('www.codewars.com?a=1&b=2&a=2') \
    == 'www.codewars.com?a=1&b=2'
assert strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) \
    == 'www.codewars.com?a=1'
assert strip_url_params('www.codewars.com', ['b']) == 'www.codewars.com'
