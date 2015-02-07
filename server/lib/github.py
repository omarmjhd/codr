import json
import urllib
import config
import tornado.httpclient as httpclient
from tornado.httputil import url_concat
import base64
from random import randint

def _make_req(url):
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
    return _make_req(url)

def get_repos(token):
    url = url_concat(config.gh_ep_url + '/user/repos', {'access_token' : token})
    print(url)
    return _make_req(url)

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

def get_code_snippet(name, token):
    """ Returns a string of the person's code """
    repo_url = url_concat(
        config.gh_ep_url + '/users/' + name + '/repos',
        {'access_token' : token}
    )
    print('---REPO URL----')
    print(repo_url)
    repos = _make_req(repo_url)
    target_repo = repos[randint(0, len(repos) - 1)]
    base_string = '/repos/' + target_repo['full_name']
    commit_string = base_string + '/commits'
    commit_url = url_concat(
        config.gh_ep_url + commit_string,
        {'access_token' : token}
    )
    commits = _make_req(commit_url)
    sha = commits[0]['sha']
    tree_string = base_string + '/git/trees/' + str(sha) + '?recursive=1'
    tree_url = url_concat(
        config.gh_ep_url + tree_string,
        {'access_token' : token}
    )
    tree= _make_req(tree_url)
    struct = tree['tree']

    i = len(struct) - 1         # Iterate down to try to avoid README.md
    while i >= 0 and struct[i]['type'] != 'blob' :
        i -= 1

    if i < 0: # true iff user has no src code in his/her repos
        return ""

    src_file = struct[i]['url'] # user has some source data
    file_url = url_concat(src_file, {'access_token' : token})
    contents = _make_req(file_url)
    return base64.standard_b64decode(contents['content'])


def get_issues(token):
    url = url_concat(config.gh_ep_url + '/user/issues', {'access_token' : token})
    json = _make_req(url) # gets a list of all issues currently assigned to the user
    if json:
        return True
    else:
        return False
