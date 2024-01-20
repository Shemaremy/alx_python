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
9. How to display in HTML data from a MySQL database





## 1. WEB FRAMEWORK
      _____________

A web framework is a software framework designed to aid 
the development of web applications, including websites, 
web services, and web APIs. It provides a structured set of tools, 
libraries, and conventions that help developers build and organize 
code for web applications more efficiently.


## 1. FLASK
      _____

Flask is a lightweight web framework for Python. 
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











## 5. WHAT IS A ROUTE
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




## 6. HOW TO DEFINE ROUTES IN FLASK.
      _____________________________

Look up in the file i created called Understand_routes.py
you will see how I defined them. But the steps
are as follows:








