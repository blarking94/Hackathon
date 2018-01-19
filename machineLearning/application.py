from wsgiref.simple_server import make_server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object (see PEP 333).
def hello_world_app(environ, start_response):

    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    if method == 'POST':
        if path.startswith('/test'):
            try:
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
            except (TypeError, ValueError):
                request_body = "0"
            try:
                response_body = str(request_body)
            except:
                response_body = "error"
            status = '200 OK'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            return [b"Hello World Post"]
    else:
        status = '200 OK'  # HTTP Status
        headers = [('Content-type', 'text/plain')]  # HTTP Headers
        start_response(status, headers)

        # The returned object is going to be printed
        return [b"Hello World"]





    #status = '200 OK'  # HTTP Status
    #headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers
    #start_response(status, headers)

    # The returned object is going to be printed
    #return [b"Hello World"]

with make_server('', 8002, hello_world_app) as httpd:
    print("Serving on port 8002...")

    # Serve until process is killed
    httpd.serve_forever()
