import json
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
            headers={'Accept':'application/json',
                     'User-Agent':'codr'
                    }
        ).body.decode('utf-8'))

        return response
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print(e)
    except Exception as e:
        # Other errors are possible, such as IOError.
        print(e)

def get_user(token):
    url = url_concat(config.gh_ep_url + '/user', {'access_token' : token})
    print(url)
    return _make_req(url, token)

def get_repos(token):
    url = url_concat(config.gh_ep_url + '/user/repos', {'access_token' : token})
    print(url)
    return _make_req(url, token)

def get_languages(token):
    """ Returns a dictionary of languages -> frequency """
    lang_dict = {}
    repos = get_repos(token)
    for repo in repos:
        lang = repo['language']
        if lang and lang not in lang_dict:
            lang_dict[lang] = 1
        elif lang:
            lang_dict[lang] = lang_dict[lang] + 1

    print(lang_dict)
    return lang_dict

def updated_at(token):
    user = get_user(token)
    return user['updated_at']
