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

# Cookies
- A cookie data is stored on client's computer as a text file
- it's purpose is to remember nad track data pertaning to client's usage for better visitor experience and site statistics
- request object contains a cookies attribute
- it is a dictionary object of all cookie variable
- In Flask, cookies are set on response object
- make_response(): to get response object from return value of a view function
- set_cookie(key, value): it uses to store a cookie by key-value
- get(key): it is used to read a cookie, get the value

# Session
- A session data is stored on server
- Session is a time interval between clients log in and log out of a server
- Data which is needed to be held across this session, is stored in a remporary directory on server.
- Session with each client is assigned a Session ID
- Session data is stored on top of cookies
- Session data is encrypted and for  this Flask application needs a SECRET_KEY
- it is a dictionary object
- For using session, we need to do:
    - to set a secret key (app.secret_key = '.....')
    - to set a session variable: session(variable) = value
    - to release a session variable: session.pop(variable, none)
    - Flask will take the values we put into the session object and serialize then into a cookie
    - sometimes we are not getting clear error message. this time we should check the size of the cookie in our page responses compared to the size supported by web browser.

# Redirect and Abort
- it returns a response object and redirects user to another target location with specified status code
- Prototype of redirect(): Flask.redirect(location, statuscode = 302, response)
- Flask class has abort() function to early exit, with an error code
- Flask.abort(code)