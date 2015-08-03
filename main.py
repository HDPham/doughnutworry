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

jinja_environment = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        index_template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(index_template.render())

class FinderHandler(webapp2.RequestHandler):
    def get(self):
        finder_template = jinja_environment.get_template('templates/finder.html')
        self.response.out.write(finder_template.render())

class MakerHandler(webapp2.RequestHandler):
    def get(self):
        maker_template = jinja_environment.get_template('templates/maker.html')
        self.response.out.write(maker_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/finder', FinderHandler),
    ('/maker', MakerHandler)
], debug=True)
