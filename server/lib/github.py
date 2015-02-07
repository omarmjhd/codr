import urllib
import config
import tornado.httpclient as httpclient
from tornado.httputil import url_concat

def _make_req(url, token):
    """Get data about the user that authorized the token."""

    # request some shit from github
    http_client = httpclient.HTTPClient()
    try:
        response = json.loads(http_client.fetch(
            url,
            method='GET',
            headers={'Accept':'application/json'}
        ))
        return response
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        pass
    except Exception as e:
        # Other errors are possible, such as IOError.
        pass

def get_user(token):
    url = url_concat(config.gh_ep_url + '/user', {'access_token' : token})
    return _make_req(url, token)

