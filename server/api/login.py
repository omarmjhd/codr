import tornado.web
import tornado.httpclient as httpclient
import config
import urllib
from lib import github

class Handler(tornado.web.RequestHandler):

    def post(self):
        # code provided by github
        code = self.get_argument('code')
        post_args = {'code': code,
                     'client_id': config.gh_id,
                     'client_secret': config.gh_secret}

        # request some shit from github
        http_client = httpclient.HTTPClient()
        try:
            response = json.loads(http_client.fetch(
                config.gh_ex_url,
                method='POST',
                body=urllib.urlencode(post_args),
                headers={'Accept':'application/json'}
            ))

            print(response)
        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            pass
        except Exception as e:
            # Other errors are possible, such as IOError.
            pass


    def get(self):
        # code provided by github
        code = self.get_argument('code')
        post_args = {'code': code,
                     'client_id': config.gh_id,
                     'client_secret': config.gh_secret}

        print(code)
        # request some shit from github
        http_client = httpclient.HTTPClient()
        try:
            response = json.loads(http_client.fetch(
                config.gh_ex_url,
                method='POST',
                body=urllib.urlencode(post_args),
                headers={'Accept':'application/json'}
            ))

            print(response)
        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            print('http error')
            pass
        except Exception as e:
            # Other errors are possible, such as IOError.
            print(e)
            pass


