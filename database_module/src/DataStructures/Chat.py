# -------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Chat Class -------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @intializes
#           Type: String
#           Description: receiver (User ID)
#           Type: String
#           Description: Date and Time
#           Type: DateTime
#           Description: message
#           Type: String
class Chat:

    def __init__(self, receiver, time, message):
        self.__receiver = receiver
        self.__time = time
        self.__message = message

    def getReceiver(self):
        return self.__receiver

    def getDateTime(self):
        return self.__time

    def getMessage(self):
        return self.__message
