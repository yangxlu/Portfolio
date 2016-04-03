import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET") 
        if self.request.path == '/aboutme.html':   
            template = JINJA_ENVIRONMENT.get_template('templates/aboutme.html')
            self.response.write(template.render({'aboutme' : 'ABOUT ME', 'home' : 'Home', 'research' : 'Research', 'login':'Login'}))
        elif self.request.path == '/research.html':   
            template = JINJA_ENVIRONMENT.get_template('templates/research.html')
            self.response.write(template.render({'research' : 'RESEARCH', 'aboutme' : 'About Me', 'home' : 'Home', 'login':"Login"}))
        elif self.request.path == '/feedback.html':   
            template = JINJA_ENVIRONMENT.get_template('templates/feedback.html')
            self.response.write(template.render({'research' : 'Research', 'aboutme' : 'About Me', 'home' : 'Home', 'login':"Login"}))
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'home': 'HOME', 'aboutme' : 'About Me', 'research' : 'Research', 'login':'Login'}))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'login': 'LOGIN', 'title': 'Login Page', 'home': 'Home', 'aboutme' : 'About Me', 'research' : 'Research'}))
    def post(self):
        nameGuess = self.request.get("name")
        passGuess = self.request.get("pw")
        logging.info("Username:" + nameGuess)
        logging.info("Password:" + passGuess)
        if (nameGuess == 'Colleen' and passGuess == 'pass'):
            template = JINJA_ENVIRONMENT.get_template('templates/loginsuccess.html')
            self.response.write(template.render({'home': 'Home','family':'Family', 'food': 'Food', 'login': 'LOGIN', 'title': ' Login Success!'}))
            logging.info("Correct Credentials")
        else: 
            self.response.write("Bad Credentials. Please try again.")
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'home': 'Home','family':'Family', 'food': 'Food', 'login': 'LOGIN', 'title': 'Login Page'}))
            logging.info("Wrong Credentials")
           
#depending on what url is inputed, display this page.
app = webapp2.WSGIApplication([
    ('/login.html', LoginHandler),
    ('/.*', IndexHandler)
], debug=True)
