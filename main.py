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
            self.response.write(template.render({'aboutme' : 'ABOUT ME', 'home' : 'Home', 'research' : 'Research', 'login':'Maps', 'title': 'About Yang', 'active1' : 'no', 'active2': 'no', 'active3':'active', 'active4': 'no'}))
        elif self.request.path == '/research.html':   
            template = JINJA_ENVIRONMENT.get_template('templates/research.html')
            self.response.write(template.render({'research' : 'RESEARCH', 'aboutme' : 'About Me', 'home' : 'Home', 'login':"Maps", 'title': 'Research','active1' : 'no', 'active2': 'active', 'active3':'no', 'active4': 'no'}))
        elif self.request.path == '/feedback.html':   
            template = JINJA_ENVIRONMENT.get_template('templates/feedback.html')
            self.response.write(template.render({'research' : 'Research', 'aboutme' : 'About Me', 'home' : 'Home', 'login':"Maps", 'title': 'Feedback'}))
        elif self.request.path == '/login.html':  
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'login': 'MAPS', 'title': 'Maps Page', 'home': 'Home', 'aboutme' : 'About Me', 'research' : 'Research','active1' : 'no', 'active2': 'no', 'active3':'no', 'active4': 'active'}))
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'home': 'HOME', 'aboutme' : 'About Me', 'research' : 'Research', 'login':'Maps', 'title': 'Home','active1' : 'active', 'active2': 'no', 'active3':'no', 'active4': 'no'}))

 
           
#depending on what url is inputed, display this page.
app = webapp2.WSGIApplication([   
    ('/.*', IndexHandler)
], debug=True)
