# Parent class 1
class TeamMember(object):                   
   def __init__(self, name, uid): 
      self.name = name 
      self.uid = uid 
# Parent class 2
class Worker(object):                 
   def __init__(self, pay, jobtitle): 
      self.pay = pay 
      self.jobtitle = jobtitle 
# Deriving a child class from the two parent classes
class TeamLeader(TeamMember, Worker):         
   def __init__(self, name, uid, pay, jobtitle, exp): 
      self.exp = exp 
      TeamMember.__init__(self, name, uid) 
      Worker.__init__(self, pay, jobtitle)
      print("Name: {}\nJob Title: {}\nPay: {}\nExp: {} years".format(self.name, self.jobtitle, self.pay, self.exp))

teamLeader = TeamLeader('Nia', 101, 50000, 'Project Head', 3)