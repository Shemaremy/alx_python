# In this task we will learn about PYTHON FRAMEWORK

## What to Know:

1. Web Framework
2. Flask
3. How to build a web framework with Flask
4. What is a route 
5. How to define routes in Flask
6. How to handle variables in a route
6. What is a template
7. How to create a HTML response in Flask by using a template
8. How to create a dynamic template (loops, conditions…)
9. How to display in HTML data from a MySQL database (Database Integration)
10. flash, redirect and url_for     classes imported from flask





## 1. WEB FRAMEWORK
      _____________

A web framework is a software framework designed to aid 
the development of web applications, including websites, 
web services, and web APIs. It provides a structured set of tools, 
libraries, and conventions that help developers build and organize 
code for web applications more efficiently.


## 1. FLASK
      _____

Flask is a lightweight (unheavy) web framework for Python. 
It’s designed to be simple and easy to use, 
making it suitable for developing 
web applications and APIs.

It is also a library same as sqlalchemy but the 
only difference is that sqlalchemy is for the sql
while Flask is for the web applications






## 2. HOW DO WE BUILD WEB APPLICATIONS USING FLASK
      ____________________________________________
    
     
      SIMPLE EXPLANATION ON WEB APPLICATIONS

Web applications often involve user input, 
processing data, and delivering personalized 
content. Examples include online
email services, social media platforms, 
and project management tools


Building a web application with Flask involves a series of steps. 
Here's a high-level overview:

1. **Install Flask:**
   - Use a package manager like pip to install Flask: `pip install Flask`

2. **Create a Flask Application:**
   - Write a Python script to create your Flask application. Define routes and create views to handle different parts of your web app.

3. **Create Templates:**
   - Use Flask's templating engine (Jinja2) to create HTML templates. Templates help you structure and render dynamic content.

4. **Handle Forms:**
   - If your web app involves user input, create HTML forms and handle form submissions in your Flask views.

5. **Define a Database (Optional):**
   - If your web app needs to store and retrieve data, integrate a database. Flask-SQLAlchemy is commonly used for database management.

6. **Static Files and CSS:**
   - Organize and serve static files (CSS, images, etc.) to enhance the visual appeal of your web app.

7. **Implement Authentication (Optional):**
   - If your app requires user accounts, use Flask-Login or other authentication solutions to manage user sessions.

8. **Testing and Debugging:**
   - Implement testing to ensure your web app functions correctly. Use Flask's built-in development server for debugging.

9. **Deployment:**
   - Choose a hosting platform and deploy your Flask application. Common choices include Heroku, AWS, or a traditional web server like Nginx or Apache.

10. **Scale (if needed):**
   - Depending on the growth of your web app, consider strategies for scaling, such as load balancing and optimizing database performance.

Remember to refer to the Flask documentation for detailed guidance and examples. Additionally, various Flask extensions are available to extend functionality based on your specific requirements.











## 4. WHAT IS A ROUTE
      ________________

A route refers to a mapping between a URL 
pattern and a function that should be executed 
when a request with that specific URL is received.

In other words, a route is essentially a way to 
tell your web application what to do when 
a user goes to a specific URL.

Consider this analogy: Imagine your web application
is like a restaurant, and each URL is a menu item. 
A route is like a set of instructions for 
what the kitchen (your application) 
should do or cook when a customer (user) orders 
a particular dish (visits a specific URL).

A url is an order you're giving the kitchen to
cook for you a certain meal you ordered

Simply, a route is a concept not an app nor a 
toolkit

Lets take an example.
We may ask ourselves why routes are defined after a slash
The reason is because a route is that one after a domain name
ex: remy.com/about
Here about is a route




## 5. HOW TO DEFINE ROUTES IN FLASK.
      _____________________________

Look up in the file i created called Understand_routes.py
you will see how I defined them. But the steps
are as follows:

a) Import Flask from flask
b) Create an instance named (app) of the Flask class (always instance name is app otherwise, an error)
ex:                  app = Flask(__name__)

c) Let the page name be x then it will be like @app.route(/'x').        Mostly, that codeline goes with        function under it

d) Define a function under which will return 
   a certain prompt or another thing after the url x is run


ex:

import
app = Flask(__name__)
@app.route('/')
def m()
   return ...


            

## 6. HOW TO HANDLE VARIABLES IN A ROUTE
      ----------------------------------





## 7. WHAT IS A TEMPLATE AND HOW TO USE THEM
      --------------------------------------

A template is a file or string that defines the structure 
of a web page and includes placeholders for dynamic content. 
Web frameworks like Flask or Django use templates to 
separate the presentation logic from the application logic. 
This promotes a cleaner code structure and makes it easier 
to manage and update the user interface.


In order to access a web page using an url 
in python, we follow these steps. Simply, when
we run a url which is located in a python route
it will run that html page returned by a function


a) Create a folder named templates
b) In that folder, create an html file with .html extension
c) Make a normal webpage in that html file
d) Go to your python file 
e) Import Flask and render_template classes from flask
f) In a route where your url that accesses your html page,
g) Make corresponding function return that html file like on h
h) return render_template('mypage.html')


You can check how it works on a file I created named
understand_templates.py



## 8. How to create a dynamic template (loops, conditions…)
      -----------------------------------------------------

Dynamic templates in the context of a Python web framework refer to a feature that allows developers to create HTML or other markup content dynamically by embedding variables and expressions within the template.(This means crating variables in python files to be used in html files as they store a certain values or data)

These variables and expressions are replaced with actual values stored in python filed when the template is rendered in python ( return render_template('') )


Visit file dynamic_templates.py file to know more



## 9. How to display in HTML data from a MySQL database (Database Integration)
       ----------------------------------------------------------------------

Let's take an example to let you know what you will be doin'g after knowing well this concept. Lets take an instagram website not the app.

- When you are searching people on instagram, you are retrieving usernames stored in instagram database
- When you are creating an account, you are inserting a new row of data in instagram database
- That instagram webpage is built and designed by html and css. The form concept (button, textbox,...)
- The data of them is being stored in sql, by the use of python

- By this concept, we will dive into how such two worlds (sql & html + css are joined by python using    SQLALCHEMY and FLASK)

- Remembering that SQLAlchemy will join python with sql and then FLASK to join HTML and Python. Cool, huh?


For further information, visit the file   pyhtml_dataintegration.py








10. flash, redirect and url_for     classes imported from flask
    -----------------------------------------------------------



# a. flash Function:

- It is used for sending one-time messages from one endpoint to another.
- It is used to display feedback or notifications to the user after a certain action has been performed
   (e.g., successful form submission, error messages, etc.).

- Flash messages are typically stored in the session and are only available for the next request.

Example:
-------
from flask import flash

@app.route('/submit_form', methods=['POST'])
def submit_form():

    flash('Form submitted successfully!', 'success')
    return redirect(url_for('index'))


- The program above will give you a prompt telling you the form has been successfully submitted












# b. url_for Function:
   ---------------------

- It is used to generate URLs for Flask routes.
- It helps create URLs dynamically, which is useful for maintaining flexibility and avoiding hardcoded URLs
   in your templates or code. This means to avoid writing URLs in your source codes

- It takes the name of a function (the endpoint) as an argument and generates a URL for that endpoint.

Example:
--------
from flask import url_for, redirect
a = url_for('index')


- An example, we have a form to input data. After inputting data, we want such form to reload
  back at the starting/ending point. In order so as we won't modify the code and make another similar
  router with the same url, we use url_for and redirect Functions as mentioned in file new_classes.py














# c. redirect Function:
   ---------------------

- It is used to redirect the user to a different endpoint or URL.
- It is used after processing a form submission or performing some action to redirect the user 
   to another page.

Example:
--------
from flask import redirect, url_for

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Process form data...
    return redirect(url_for('index'))


