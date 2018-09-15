import sys

ENTER = "Enter"
LEAVE = "Leave"
CHANGE = "Change"

class Record(object):
    def __init__(self, action, uid):
        self.__action = action
        self.__uid = uid

    @staticmethod
    def parse(data):
        splitted = data.split(' ')
        if splitted[0] == ENTER || splitted[0] == CHANGE:
            return splitted
        
        splitted.append(None)
        return splitted

    def message(self, user_dict):
        if action == ENTER:
            return "%s entered"
        if action == LEAVE:
            return "%s left"

def solution(raw_record):
    record = list()
    user_dict = dict()

    for row in raw_record:
        action, uid, name = Record.parse(row)
        
        if action == ENTER or action == LEAVE:
            record.append(Record(action, uid))
        if action == ENTER or action == CHANGE:
            user_dict[uid] = name

    messages = list()
    for r in record:
        messages.append(record.message(user_dict))
    
    return messages
