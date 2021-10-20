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

# File Uploading
- include enctype = "multipart/form-data" isnide <form> tag
- method will be POST
- input type will be file
- 'from werkzeug.utils import secure_filename' in python file
- for getting the file, use f= request.files['file']
- for saving the file, use f.save(secure_filename(f.filename))

# Flask Extensions
- Flask Mail: it provides SMTP interface to Flask application
- Flask WTF: it adds rendering and validation of WTForms
- Flask SQLAlchemy: it adds SQLAlchemy support to Flask application. it it maps the Database to the python program
- Flask Sijax: Interface for SIjax - Python/jQuery library that makes AJAX easy to use in web applications

## Flask Mail:
- A web based application is often required to send mail to the users. Flask-Mail provides this support.
- installation procedure: 
    - pip install Flask-Mail
    - Or, git clone https://github.com/mattupstate/flask-mail.git
    - cd flask-mail
    - python setup.py install
- Configuring Flask-Mail
    - MAIL_SERVER: Name/IP address of email server
    - MAIL_PORT: Port number of server used
    - MAIL_USE_TLS: Enable/disable Transport Security Layer encryption
    - MAIL_USE_SSL: Enable/disable SSL encryption
    - MAIL_DEBUG: Debug support
    - MAIL_USERNAME: Username and password of sender
    - MAIL_PASSWORD: ||
    - MAIL_DEFAULT_SENDER: sets default sender
    - MAIL_MAX_EMAILS: Sets maximum mails to be sent
    - MAIL_SUPPRESS_SEND: Sending suppressed if app.testing set to true
    - MAIL_ASCII_ATTACHMENTS: If true, attached filenames converted to ASCII
### Mail Class:
- it manages email messaging requirements. The class constructor takes following form: flask-mail.Mail(app=None)
- Mail class methods:
    - send(): sends contents of message class objects
    - connect(): opens connection with mail host
    - send_message(): sends message objects
### Message Class:
- it encapsulates an email message. Message class constructor has several parameters:
- flask_mail.Message(subject, recipients, body, html, sender, cc, bcc, reply-to, date, charset, extra_headers, mail_options, rcpt_options)
- Message clas methods:
    - attach(): adds an attachment to message. The method takes following parameters:
        - filename: name of file to attach
        - content_type: MIME type of file
        - data: raw file data
        - disposition: content disposition, if any
    - add_recipient(): adds another recipient to message

### 
Parameters:	
- subject – email subject header
- recipients – list of email addresses
- body – plain text message
- html – HTML message
- sender – email sender address, or MAIL_DEFAULT_SENDER by default
- cc – CC list
- bcc – BCC list
- attachments – list of Attachment instances
- reply_to – reply-to address
- date – send date
- charset – message character set
- extra_headers – A dictionary of additional headers for the message
- mail_options – A list of ESMTP options to be used in MAIL FROM command
- rcpt_options – A list of ESMTP options to be used in RCPT commands

* if we want to use gmail smtp, then we should cofigure a setting through this link: https://www.google.com/settings/security/lesssecurityapps (the the google mail service doesn't allow mails to be sent by any third party appsication)
* By default the setting is Turn off, we need it to Turn on

## Flask WTF
- Features
    - Integration with WTForms.
    - Secure Form with CSRF token.
    - Global CSRF protection.
    - reCAPTCHA support.
    - File upload that works with Flask-Upload
- installation procedure:
    - pip install flask-WTF
    - Or, git clone https://github.com/wtforms/flask-wtf
    - pip install -e ./flask-wtf
- WTForms pacage contains validator class. The commonly used validators are:
    - DataRequired
    - Email
    - IPAdress
    - Length
    - NumberRange
    - URL

# Flask SQLAlchemy
- It is an ORM in python
- installation procedure:
    - pip install flask-sqlalchemy
- The ORM's "handle" to the database is the Session
- session object methods
    - db.session.add(model obj): inserts a record into mapped table
    - db.session.delete(model obj): deletes record from table
    - model.query.all(): retrieves all records from table (select * from table)
    - model.query.filter(condition): we can apply filter to retrieved record
    - Students.query.filter_by(city=='Dhaka').all()

