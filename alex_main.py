import requests_params

# if use proxies
requests_params.COMMON_REQUEST_PARAMETERS['proxies'] = {'https': 'myproxy'}
# or
requests_params.COMMON_REQUEST_PARAMETERS['proxies'] = {}

