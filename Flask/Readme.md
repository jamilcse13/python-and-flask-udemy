# Flask:
- It is a Web Application Framework written in python.
- This is a WSGI standard or compliant framework. (WSGI: Web Server Gateway Interface)
- It is often referred to as a micro framework.
- It can be extended.


# Environment Setup
- install pip
- install virtualenv: it can avoid compatibality issues between different versions of libraries.
- "sudo pip install virtualenv"
- create virtual environment in the targeted location using: "virtualenv name" (ex: venv)
- install flask using: "pip install flask"
- activate virtual environment using: "source venv/bin/activate"
- flask environment is ready

# Run the Project
- @app.route('define the route.url')
- app.run(host=localhost, debug=False, port=5000) with default value
- we can modify the app.run
- if use put debug=True, then the updated code will execute without restart the server again.

# HTTP: Hypertext Transfer Protocol
- It is an application protocol for distributed, collaborate, hypermedia information systems
- It is the foundation of data communication for the World Wide Web
- It is the protocol to exchange or transfer hypertext
- The HTTP/1.0 specification defined the GET, POST and HEAD methods
- The HTTP/1.0 specification added 5 new methods: OPTIONS, PUT, DELETE, TRACE and CONNECT

# Templates
- we can render html files from python file using render_templates. for this we need store the html files inside a templates folder.
- we can render js and css files from html file usinf url_for('static', file_name='file name'). for this we need store the js and css files inside a static folder.

# Requests
- We can handle given input request parameters in python using some attributes of request onbject:
    - Form: POST and PUT method
    - args: GET method
    - values: combination of Form and args
    - cookies: contents of all cookies transmitted with the request
    - headers: the incoming request headers as a dictionary like object
    - data: contains incoming request data as string, mimetype doesn't handle by this
    - files: handle uploaded files of POST or PUT request.
    - save(): to store data
    - environ: the underlying WSGI env
    - method: which current request method is used (POST, GET etc)
    - module: the name of the current module
    - routing_exception = None: this is similar NotFound exception or something similar, if matching url is failed