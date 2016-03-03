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
