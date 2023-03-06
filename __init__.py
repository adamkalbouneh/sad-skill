from mycroft import MycroftSkill, intent_file_handler


class Sad(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sad.intent')
    def handle_sad(self, message):
        self.speak_dialog('sad')


def create_skill():
    return Sad()

