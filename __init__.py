from mycroft import MycroftSkill, intent_file_handler


class CleanRoom(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('room.clean.intent')
    def handle_room_clean(self, message):
        self.speak_dialog('room.clean')


def create_skill():
    return CleanRoom()

