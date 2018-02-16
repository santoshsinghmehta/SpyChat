from datetime import datetime       #import time.


class Spy:          #create a class

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None



spy = Spy('santosh', 'Mr.', 22, 4.7)

class ChatMessage:
  def __init__(self, message,sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me

chats=[]