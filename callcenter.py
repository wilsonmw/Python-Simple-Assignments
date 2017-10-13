class CallCenter(object):
    def __init__(self):
        self.callList = []
        self.queue = 0

    def add(self, call):
        self.callList.append({"Caller ID":str(call.callid), "Name": call.name, "Number": str(call.number), "Time": str(call.time), "Reason":call.reason})
        self.queue += 1
        return self

    def remove(self, call):
        self.callList.pop(0)
        self.queue -=1
        return self

    def info(self):
        for i in range(0,len(self.callList)):
            print self.callList[i]["Name"], self.callList[i]["Number"]
        print self.queue





class Call(object):
    def __init__(self, callid, name, number, reason):
        self.callid = callid
        self.name = name
        self.number = number
        import datetime
        self.time = datetime.datetime.now().time()
        self.reason = reason

    def display(self):
        print "Customer ID: " + str(self.callid)
        print "Name: " + self.name
        print "Phone Number: " + str(self.number)
        print "Call Time: " + str(self.time)
        print "Reason for Call: " + self.reason
        return self



center = CallCenter()
call1 = Call(2, "Bob", "206-555-1234", "Wants to cancel service")
call2 = Call(3, "Charlie", "425-333-1234", "Pay Bill")
call3 = Call(4, "Sally", "206-778-1737", "Yell at Customer Service Reps")


center.add(call1)
center.add(call2)
center.add(call3)
center.info()
center.remove(call2)
center.info()

        