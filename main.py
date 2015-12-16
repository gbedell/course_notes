import os
import jinja2
import webapp2
from notes import concepts

from google.appengine.api import users
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), "templates")

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Comment(ndb.Model):
    # Main model for a user comment
    user_email = ndb.StringProperty()
    comment_text = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def valid_email(self, email):
        at_symbol = "@"
        period = "."
        if at_symbol and period in email:
            return email
        else: 
            self.redirect('/?error=Please fill out the email and comment sections!')

class MainPage(Handler):
    def get(self):
        # Checks for an error
        error = self.request.get('error','')
        # Queries the Comment instances from the datastore
        query = Comment.query().order(-Comment.date)
        # Populates the web page
        self.render("lessons.html", concepts = concepts, query = query, error = error)

    def post(self):
        user_email = self.request.get("email")
        comment_text = self.request.get("comment")

        if self.valid_email(user_email) and comment_text:
            submission = Comment(user_email = user_email, comment_text = comment_text)
            submission.put()
            import time
            delay = 0.1
            time.sleep(delay)
            self.redirect('/')
        else:
            self.redirect('/?error=Please fill out the email and comment sections!')

class Course5(Handler):
  def get(self):
    self.render("course5_notes.html")
    

app = webapp2.WSGIApplication([("/", MainPage), ("/course5", Course5)])
