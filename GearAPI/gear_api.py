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
import json
import string
import cPickle as pickle


import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


from google.appengine.ext import vendor

vendor.add('lib')
vendor.add('lib/nltk')

import textblob
import textblob_de
import email_util


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# TODO
# add article directory here as well
# articles must match up with articles in front-end app
vendor.add('articles')


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

class JsonData(messages.Message):
    """A JSON string containing data to save via email"""
    message = messages.StringField(1)


## TODO
class Dictionary(messages.Message):
    """A JSON string containing a dictionary of words for the articles"""
    message = messages.StringField(1)

class ArticleName(messages.Message):
    """Name of an article in both backend and frontend articles directory"""
    message = messages.StringField(1)


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

    ARTICLE_NAME_RESOURCE = endpoints.ResourceContainer(ArticleName)
    @endpoints.method(ARTICLE_NAME_RESOURCE, Dictionary, path='dictionary', http_method='POST', name='stories.getDictionary')
    def get_dictionary(self, request):
        # TODO
        article_name = str(request.message)

        dictionary = {}
        with open('articles/' + article_name, 'r') as f:
            text = f.read().encode('utf-8')
            for word_maybe_punctuation in text.split()[0:5]:
                exclude = set(string.punctuation)
                word = ''.join(ch for ch in word_maybe_punctuation if ch not in exclude)
                

                if word not in dictionary:
                    print 'word not in dictionary: ', word    
                    blob = textblob_de.TextBlobDE(word, parser=textblob_de.PatternParser(pprint=True, lemmata=True))
                    try: 
                        print 'tried translating'
                        translation = str(blob.translate(from_lang="de", to="en"))
                        print 'translation is ', translation
                        dictionary[w] = translation
                    except textblob.exceptions.NotTranslated:
                        pass

        json_dictionary = json.dumps(dictionary)

        return Dictionary(message=json_dictionary)

    DEFINE_RESOURCE = endpoints.ResourceContainer(Definition)
    @endpoints.method(DEFINE_RESOURCE, Definition, path='gearapi/define',http_method='POST',name='gearapi.define')
    def define(self,request):
        # Old translation mechanism -- used TextBlob & Google Translate -- no longer words
        # responseBlob = textblob_de.TextBlobDE(request.message, 
            # parser=textblob_de.PatternParser(pprint=True, lemmata=True))
        # responseText = str(responseBlob.translate(from_lang="de", to="en"))
        # responseText += "++" + str(responseBlob.words.lemmatize()[0])

        # New method uses file german_english.txt that is preprocessed
        # by dictionary.py to create the file dictionary.p
        dictionary = pickle.load(open("dictionary.p", "rb"))        
        responseText = dictionary.get(request.message, "No translation available")

        return Definition(message=responseText)

    JSONDATA_RESOURCE = endpoints.ResourceContainer(JsonData)
    @endpoints.method(JSONDATA_RESOURCE, JsonData, path='gearapi/json',http_method='POST',name='gearapi.sendJsonData')
    def send_json_data(self, request):
        json_string = str(request.message)
        email_util.email_data(json_string)

        # --> 
        # do we want to make this return a status of the email instead,
        # e.g. "Successful email transmission" upon success?
        return JsonData(message=json_string)




APPLICATION = endpoints.api_server([GearApi])
