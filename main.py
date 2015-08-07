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

import jinja2
import webapp2
import logging
import os
import json
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import urlfetch


jinja_environment = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True)

# class CoordsRequest(ndb.Model):
#     lat = ndb.StringProperty(required = True)
#     lon = ndb.StringProperty(required = True)
#     timestamp = ndb.DateTimeProperty(auto_now_add = True)
#
# class AddressRequest(ndb.Model):
#     address = ndb.StringProperty(required = True)
#     timestamp = ndb.DateTimeProperty(auto_now_add = True)

class UserModel(ndb.Model):
    currentUser = ndb.StringProperty()
    username = ndb.StringProperty()
    text = ndb.TextProperty()

class Donut(ndb.Model):
    cake = ndb.StringProperty()
    topping = ndb.StringProperty()
    frosting = ndb.StringProperty()
    owner = ndb.KeyProperty(UserModel)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        index_template = jinja_environment.get_template('templates/index.html')
        self.response.write(index_template.render())

        template_vars = {'logout': users.create_logout_url('/')}
        user = users.get_current_user()
        if user:
            user = UserModel(currentUser = user.user_id(), text = 'hey')
            user.put()
        else:
            self.redirect(users.create_login_url(self.request.uri))




class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        index_template = jinja_environment.get_template('templates/signup.html')
        self.response.write(index_template.render())

class FinderHandler(webapp2.RequestHandler):
    def get(self):
        finder_template = jinja_environment.get_template('templates/finder.html')
        self.response.write(finder_template.render())
    # def post(self):
    #     self.response.write(self.request.get('location'))
        # google_maps_data_source = urlfetch.fetch('https://maps.googleapis.com/maps/api/js?v=3.exp')
        # google_maps_content = google_maps_data_source.content
        # parsed_google_maps_dictionary = json.loads(google_maps_content)

# class RecordRequestHandler(webapp2.RequestHandler):
#     def post(self):
#         logging.info(self.request)
#         if self.request.get('type') == "coords":
#             new_record = CoordsRequest(lat = self.request.get('lat'), lon = self.request.get('lon'))
#             new_record.put()
#         elif self.request.get('type') == "address":
#             new_address_record = AddressRequest(address = self.request.get('address'))
#             new_address_record.put()
#         else:
#             logging.error("Malformed Request!")

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
                'lemon' : "http://oi57.tinypic.com/2nj92bn.jpg",
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

    def post(self):
        logging.info("maker handler POST request")
        logging.info(self.request)
        chosen = self.request.get("selected")
        chosen2 = self.request.get("selected2")
        chosen3 = self.request.get("selected3")
        logging.info(chosen)
        # donut1 = Donut(cake = chosen, topping = chosen2, frosting = chosen3)
        # donut1.put()

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_environment.get_template('templates/about.html')
        self.response.write(about_template.render())

class AddHandler(webapp2.RequestHandler):
    def post(self):
        chosen = self.request.get("selected")
        chosen2 = self.request.get("selected2")
        chosen3 = self.request.get("selected3")
        # http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg
        # possibly add dictionary with values and their urls
        #cake = self.request.get_all('cake')
        user1 = UserModel(username="ThatGuy")
        user1.put()
        donut1 = Donut(cake = chosen, topping = chosen2, frosting = chosen3, owner=user1.key)
        donut1.put()

    def get(self):
        my_donuts_template = jinja_environment.get_template('templates/my_donuts.html')
        query = Donut.query()
        post_data = query.fetch()
        donut_vars = {'donuts': []}
        for i in range(0, len(post_data), 1):
            user_data = post_data[i]
            user_data_cake = user_data.cake
            user_data_topping = user_data.topping
            user_data_frosting = user_data.frosting
            # Pass the data to the template
            donut_vars['donuts'].append([user_data_cake, user_data_topping, user_data_frosting])
        logging.info(donut_vars)
        self.response.write(my_donuts_template.render(donut_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', SignUpHandler),
    ('/finder', FinderHandler),
    ('/maker', MakerHandler),
    ('/add', AddHandler),
    ('/select', SelectDonutHandler),
    ('/about', AboutHandler)
], debug=True)
