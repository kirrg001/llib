import gdata.youtube
import gdata.youtube.service
import gdata.alt.appengine
import wsgiref.handlers
import urllib
import cgi
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db

import gdata.youtube
import gdata.youtube.service
import gdata.media
import gdata.geo
import gdata.alt.appengine

import gdata.youtube
import gdata.youtube.service


class Youtube_API(webapp.RequestHandler):
    def __init__(self):
        self.youtube_scope = 'http://gdata.youtube.com'
        self.developer_key = "AI39si4wFuyUpwXK6nBWQ0yIcfoTtXP3YmhbfiM6MrVWR5DPSZrsfEOm6AcoHLM6aEW4isp3WIdSMfYW57VOso4x5B0E27TjxQ"
        self.client = gdata.youtube.service.YouTubeService()
            
    def login(self, username, pw):
        next = '{% url y_links %}'
        secure = False
        session = True

        try:
            return self.client.GenerateAuthSubURL(next, self.youtube_scope, secure, session)
        except Exception as e:
            print e