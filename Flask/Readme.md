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