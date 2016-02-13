"""GEAR Backend API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""
"""
FOR PUSHING TO THE SERVER:
Don't forget to upload your changes to github!

Test Locally!
dev_appserver.py --port=8080 GoogleAppEngine-Python/
In the command prompt:
    appcfg.py update --no_cookies app.yaml
        ^app-directory is the name of our app's directory
    Then check here:
    http://backendgear-1121.appspot.com/_ah/api/explorer

    Then create a library bundle for android:
    endpointscfg.py get_client_lib java -bs gradle gear_api.GearBackendApi

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

"""    
class Greeting(messages.Message):
  Greeting that stores a message.
  message = messages.StringField(1)


class GreetingCollection(messages.Message):
  Collection of Greetings.
  items = messages.MessageField(Greeting, 1, repeated=True)
"""

STORED_STORIES = StoriesCollection(items = [
    RecommendedStory(message="aschenputtel"),
    RecommendedStory(message="cinderella"),
    RecommendedStory(message="froschkoenig"),
    RecommendedStory(message="haensel_und_gretel"),
    RecommendedStory(message="hans_im_glueck"),
    RecommendedStory(message="rapunzel"),
])

"""
STORED_GREETINGS = GreetingCollection(items=[
  Greeting(message='hello world!'),
  Greeting(message='goodbye world!'),
])
"""

class UserUpdate(messages.Message):
    article_name = messages.StringField(1, required=True)
    article_rating = messages.IntegerField(2, required=True)

@endpoints.api(name='gear', version='v2')
class GearApi(remote.Service):
    """GearBackend API v1."""
    @endpoints.method(message_types.VoidMessage, StoriesCollection, path='recommendedstory', http_method='GET', name='stories.listStory')
    def stories_list(self, unused_request):
        return STORED_STORIES
    """
    @endpoints.method(message_types.VoidMessage, StoriesCollection, path='define', http_method='POST', name='stories.define')
    def define(self, request):
        return STORED_STORIES
    """
    """
  @endpoints.method(message_types.VoidMessage, GreetingCollection,
                    path='hellogreeting', http_method='GET',
                    name='greetings.listGreeting')
  def greetings_list(self, unused_request):
    return STORED_GREETINGS
    """
    DEFINE_RESOURCE = endpoints.ResourceContainer(Definition)#, word=messages.StringField(1, required=True))
    @endpoints.method(DEFINE_RESOURCE, Definition, path='gearapi/multiply',http_method='POST',name='gearapi.define')
    def define(self,request):
        return Definition(message=request.message + str(textblob_de.TextBlobDE(request.message)))
"""
  MULTIPLY_METHOD_RESOURCE = endpoints.ResourceContainer(
      Greeting,
      times=messages.IntegerField(2, variant=messages.Variant.INT32,
                                  required=True))

  @endpoints.method(MULTIPLY_METHOD_RESOURCE, Greeting,
                    path='hellogreeting/{times}', http_method='POST',
                    name='greetings.multiply')
  def greetings_multiply(self, request):
    return Greeting(message=request.message * request.times)
"""
"""
  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))

  @endpoints.method(ID_RESOURCE, Greeting,
                    path='hellogreeting/{id}', http_method='GET',
                    name='greetings.getGreeting')
  def greeting_get(self, request):
    try:
      return STORED_GREETINGS.items[request.id]
    except (IndexError, TypeError):
      raise endpoints.NotFoundException('Greeting %s not found.' %
                                        (request.id,))
"""

APPLICATION = endpoints.api_server([GearApi])
