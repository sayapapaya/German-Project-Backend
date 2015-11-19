from google.appengine.api import mail


def send_data(message_string):
    """Sends a message string via email to our backend email address.
    """

    message = mail.EmailMessage(sender="Gear on Google App Engine",
                                subject="App data")
    message.to = "Gear Backend email<gearbackendpython@gmail.com>"

    message.body = """
        Data from the front end:
        %s""" %message_string

    message.send()