import tornado.web
import tornado.httpclient as httpclient
import config
import urllib.parse
import json
from models import users
from lib import github

class Handler(tornado.web.RequestHandler):

    def get(self):
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
                body=urllib.parse.urlencode(post_args),
                headers={'Accept':'application/json'}
            ).body.decode('utf-8'))

            access_token = response['access_token']
            user = github.get_user(access_token)

            print(user)

            # add to db

            if 'id' in user:

                users.update_user(
                    user['id'],
                    user['name'] if 'name' in user else user['login'],
                    access_token,
                    user['avatar_url'],
                    github.get_languages(access_token),
                    user['updated_at'],
                    github.get_code_snippet(user['id'])
                )

                self.set_secure_cookie('user', str(user['id']))

                fetched_user = users.get_user(user['id'])

                print(fetched_user)

                self.redirect('/#/match')
            else:
                self.redirect('/#/error/login')

        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            print('Error', e)
        except Exception as e:
            # Other errors are possible, such as IOError.
            print('Error', e)
