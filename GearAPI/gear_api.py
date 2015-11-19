"""GEAR Backend API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""
"""
FOR PUSHING TO THE SERVER:
Don't forget to upload your changes to github!

Test Locally!
dev_appserver.py --port=8080 GearAPI/
In the command prompt:
    appcfg.py update --no_cookies app.yaml
        ^app-directory is the name of our app's directory
    Then check here:
    http://backendgear-1121.appspot.com/_ah/api/explorer

    Then create a library bundle for android:
    endpointscfg.py get_client_lib java -bs gradle gear_api.GearApi

    Then import this module into android studio and GO
"""

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from google.appengine.ext import vendor
vendor.add('lib')
vendor.add('lib/nltk')

import textblob_de
import email_util

package = 'GearBackend'

class Definition(messages.Message):
    """Definition of a word"""
    message = messages.StringField(1)

class RecommendedStory(messages.Message):
    """Recommendation that stores a story"""
    message = messages.StringField(1)

class StoriesCollection(messages.Message):
    """Collection of stories"""
    items = messages.MessageField(RecommendedStory, 1, repeated=True)



STORED_STORIES = StoriesCollection(items = [
    RecommendedStory(message="aschenputtel"),
    RecommendedStory(message="cinderella"),
    RecommendedStory(message="froschkoenig"),
    RecommendedStory(message="haensel_und_gretel"),
    RecommendedStory(message="hans_im_glueck"),
    RecommendedStory(message="rapunzel"),
])



class UserUpdate(messages.Message):
    article_name = messages.StringField(1, required=True)
    article_rating = messages.IntegerField(2, required=True)

@endpoints.api(name='gear', version='v2')
class GearApi(remote.Service):
    """GearBackend API v1."""
    @endpoints.method(message_types.VoidMessage, StoriesCollection, path='recommendedstory', http_method='GET', name='stories.listStory')
    def stories_list(self, unused_request):
        return STORED_STORIES

    DEFINE_RESOURCE = endpoints.ResourceContainer(Definition)#, word=messages.StringField(1, required=True))
    @endpoints.method(DEFINE_RESOURCE, Definition, path='gearapi/multiply',http_method='POST',name='gearapi.define')
    def define(self,request):
        responseBlob = textblob_de.TextBlobDE(request.message)
        responseText = str(responseBlob.translate(to="en"))
        email_util.send_data(responseText)
        return Definition(message=responseText)


APPLICATION = endpoints.api_server([GearApi])
