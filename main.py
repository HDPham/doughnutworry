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
import logging


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
        logging.info(self.request.get("selected"))
        logging.info(self.request.get("selected2"))
        chosen = self.request.get("selected")
        chosen2 = self.request.get("selected2")
        chosen3 = self.request.get("selected3")
        # http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg
        # possibly add dictionary with values and their urls
        #cake = self.request.get_all('cake')
        dcake = {'plain' : "http://oi59.tinypic.com/28ck1np.jpg",
                'chocolate' : "http://oi59.tinypic.com/e6a73d.jpg",
                'redvelvet' : "http://oi58.tinypic.com/2db12lv.jpg",
                'lemon' : "http://oi59.tinypic.com/j6sgia.jpg",
                'pistachio' : "http://oi59.tinypic.com/ok0g8l.jpg"}
        cakeimg = dcake.get(chosen)
        dfrosting = {'vanilla' : "http://oi61.tinypic.com/fllyfp.jpg",
                    'chocolate' : "http://oi59.tinypic.com/2lk32v8.jpg",
                    'strawberry': "http://oi60.tinypic.com/o8gbbs.jpg",
                    'healthy': "http://oi62.tinypic.com/14t98qs.jpg",
                    'fun': "http://oi61.tinypic.com/2r4rhtz.jpg"}
        # url = "http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg"
        frostingimg = dfrosting.get(chosen2)
        dtopping = {'none' : "",
                    'nuts' : "http://oi60.tinypic.com/adycdl.jpg",
                    'fruit': "http://oi60.tinypic.com/2a68ai9.jpg",
                    'chocochips': "http://oi60.tinypic.com/zl8979.jpg",
                    'chocodrizzle': "http://oi58.tinypic.com/33bg940.jpg",
                    'candy': "http://oi61.tinypic.com/1qmm55.jpg"}
        # url = "http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg"
        # http://oi60.tinypic.com/zl8979.jpg
        toppingimg = dtopping.get(chosen3)
        self.response.headers['Content-Type'] = 'application/json'
        response = {"url":cakeimg,
                    "urlf": frostingimg,
                    "urlt": toppingimg,
                    # "name": "My Doughnut",
                    # "text_color": "red"
                    }
        self.response.write(json.dumps(response))


class MakerHandler(webapp2.RequestHandler):
    def get(self):
        maker_template = jinja_environment.get_template('templates/maker.html')
        self.response.write(maker_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/finder', FinderHandler),
    ('/maker', MakerHandler),
    ('/select', SelectDonutHandler)
], debug=True)
