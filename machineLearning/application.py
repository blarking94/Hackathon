from wsgiref.simple_server import make_server
import sys
import DNNCar

def hello_world_app(environ, start_response):

    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    if method == 'POST':
        if path.startswith('/test'):
            the_classification = ""
            try:
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                print(request_body)
                variables = request_body.decode("utf-8").split('&')
                i = 0
                values = []
                for var in variables:
                    if i is not 0 and i is not 1:
                        string = var.split("=")
                        values.append(int(string[1]))
                    else:
                        i = i + 1

                returned_classification = DNNCar.classifyNew(values)
                returned_array = returned_classification[0]
                the_classification = returned_array[0]
            except (TypeError, ValueError):
                request_body = "0"
            try:
                response_body = str(request_body)
            except:
                response_body = "error"
            status = '200 OK'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            print (the_classification)
            return [the_classification]
    else:
        response_body = b"hello world"

        status = '200 OK'

        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body)))
        ]

        start_response(status, response_headers)

        # The returned object is going to be printed
        return [response_body]

with make_server('', 8002, hello_world_app) as httpd:
    DNNCar.main()
    sys.stdout.write("Serving on Port 8002")
    print("Serving on Port 8002")


    # Serve until process is killed
    httpd.serve_forever()
