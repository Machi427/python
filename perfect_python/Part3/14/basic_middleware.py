import re
import base64

class BasicAuthMiddleware:
    def __init__(self, app, realm, authenticate):
        self.app = app
        self.realm = realm
        self.authenticate = authenticate

    def __call__(self, environ, start_response):
        auth = environ.get('HTTP_AUTHORIZATION')
        if not auth:
            return self.unauthorized(environ, start_response)

        if not auth.startswith('Basic'):
            return self.unauthorized(environ, start_response)

        m = re.match(r'Basic\s+(?P<basic_auth>\w+)', auth)
        if m is None:
            return self.unauthorized(environ, start_response)

        basic_auth = m.groupdict()['basic_auth']
        basic_auth = base64.b64decode(basic_auth)
        basic_auth = basic_auth.decode('utf-8')
        user, password = basic_auth.split(':', 1)
        if not self.authenticate(user, password):
            return self.unauthorized(environ, start_response)

        return self.app(environ, start_response)

    def unauthorized(self, environ, start_response):
        start_response("401 Unauthoirzed",
                       [('Content-type', 'text/html'),
                        ('WWW-Authenticate',
                         'Basic realm="{realm}"'.format(realm=self.realm))])

        return [b'Unauthorized']
