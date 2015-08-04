#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import json
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import urlfetch


jinja_environment = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True)


class UserModel(ndb.Model):
    currentUser = ndb.StringProperty()
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    text = ndb.TextProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        index_template = jinja_environment.get_template('templates/index.html')
        self.response.write(index_template.render())

        user = users.get_current_user()
        if user:
            self.response.write(user)
            user = UserModel(currentUser = user.user_id(), text = 'hey')
            user.put()
            self.response.write('<html><body><a href="%s">sign out</a></body></html>' % users.create_logout_url('/'))
        else:
            self.redirect(users.create_login_url(self.request.uri))

class FinderHandler(webapp2.RequestHandler):
    def get(self):
        finder_template = jinja_environment.get_template('templates/finder.html')
        self.response.write(finder_template.render())
    def post(self):
        self.response.write(self.request.get('location'))
        # google_maps_data_source = urlfetch.fetch('https://maps.googleapis.com/maps/api/js?v=3.exp')
        # google_maps_content = google_maps_data_source.content
        # parsed_google_maps_dictionary = json.loads(google_maps_content)

class SelectDonutHandler(webapp2.RequestHandler):
    def post(self):
        

class MakerHandler(webapp2.RequestHandler):
    def get(self):
        maker_template = jinja_environment.get_template('templates/maker.html')
        self.response.write(maker_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/finder', FinderHandler),
    ('/maker', MakerHandler)
], debug=True)
