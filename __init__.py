from mycroft import MycroftSkill, intent_file_handler
#import rospy
#from std_msgs.msg import String


#pub = rospy.Publisher('/syscommand',String,queue_size=10)
#def publish(pub, str):
#	pub.publish(str)

#rospy.init_node("listenerCleanRoom")

class CleanRoom(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('room.clean.intent')
    def handle_room_clean(self, message):
        self.speak_dialog('room.clean')
	print("Send Clean Room Command to Robot")


def create_skill():
    return CleanRoom()

