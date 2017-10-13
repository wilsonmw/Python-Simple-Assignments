

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.bedNumber = 0

    def admit(self, patient):
        if len(self.patients)>=self.capacity:
            print "Sorry, the hospital is full, you will have to die somewhere else."
        else:
            print "Welcome to " + self.name +", where you will probably die."
            self.bedNumber = self.bedNumber + 1
            patient.bedNumber = self.bedNumber
            self.patients.append(patient)       
            return self

    def discharge(self, patient):
        self.patients.remove(patient)
        patient.bedNumber = None
        self.bedNumber = self.bedNumber -1   
        return self


class Patient(object):
    def __init__(self, patientId, name, allergies):
        self.patientId = patientId
        self.name = name
        self.allergies = allergies
        self.bedNumber = None


patient1 = Patient(1, "Bob", "Wheat")
patient2 = Patient(2, "Sally", "Penicillin")
patient3 = Patient(5, "Jim", "Eggs")
patient4 = Patient(10, "Sue", "Peanuts")

hospital1 = Hospital("Killer County", 3)

hospital1.admit(patient1).admit(patient2).admit(patient3)
# hospital1.discharge(patient3)
# hospital1.discharge(patient1)
for i in range(0,len(hospital1.patients)):
    print hospital1.patients[i].name
