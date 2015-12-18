import urllib.parse

from wsgiref.simple_server import make_server
from wsgiref.util import application_uri

def calc(environ, start_response):

    request_method = environ['REQUEST_METHOD']

    if request_method == 'GET':
        return form(environ, start_response)
    elif request_method == 'POST':
        return _calc(environ, start_response)

form_body = """<html>
<form method="POST" action="{url}">
<input type="text" name="value" />
<input type="text" name="value" />
<input type="submit" value="Add" />
</form>
</html>
"""

def form(environ, start_response):
    start_response("200 OK",
                   [("Content-type", "text/html;charset=utf-8")])
    url = application_uri(environ)
    return [form_body.format(url=url).encode('utf-8')]

calc_body = """
<html>
<dl>
<dt>values:</dt>
<dd> {values}</dd>
<dt>result</dt>
<dd> {result}</dd>
</html>
"""

def _calc(environ, start_response):
    start_response("200 OK",
                   [("Content-type", "text/html;charset=utf-8")])
    content_length = int(environ.get('CONTENT_LENGTH', -1))
    params = urllib.parse.parse_qs(environ['wsgi.input'].read(content_length))
    print(params)
    values = [int(v) for v in params[b'value']]
    result = sum(values)

    return [calc_body.format(values=",".join(str(v) for v in values),
                                 result=result).encode('utf-8')]
