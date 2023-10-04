from flask import Flask, request

app = Flask(__name__)

# custom middleware
@app.before_request
def log_request_info():
    print(f"URL: {request.url}")

@app.after_request
def add_custom_header(response):
    response.headers['X-Custom-Header'] = 'Hello, Middleware!'
    return response

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

'''
out put is something like this :

    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    
    # When you make a request to the root URL "/"
    Request received for URL: http://127.0.0.1:5000/
    127.0.0.1 - - [Timestamp] "GET / HTTP/1.1" 200 -
    
    # The request is handled, and the response is sent with the custom header
    # "X-Custom-Header" added by the after_request middleware
    127.0.0.1 - - [Timestamp] "GET / HTTP/1.1" 200 -


'''

