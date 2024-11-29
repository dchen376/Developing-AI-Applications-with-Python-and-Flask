from flask import Flask, jsonify #'flask' module name, and "Flask" is class name.

# Create a Flask application instance, passing in the name of the current module
app = Flask(__name__) # which represents the web app.
"""The argument __name__ tells Flask
 how to locate resources like templates and 
static files relative to the location of the current module."""
# __name__ is system-defined identifier, global variable in every module


# Define a route for the root URL ("/")
"""A route is a URL pattern that is mapped to a specific function, which gets executed 
when the user accesses that URL in their browser."""

@app.route("/") # the function defined immediately after it should be called when the user accesses the root URL (i.e., /) of the web application.
def index():
    # Function that handles requests to the root URL
    return {}

