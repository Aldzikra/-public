class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger =[]
        
    def add_passenger(self,name):
        if self.open_seats() == 0:
            return False            
        self.passenger.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passenger)
    
Flight = Flight(3)

person = ["Harry","Jimmy","Jenna","Benjamin"]
for people in person:
    success = Flight.add_passenger(person)
    if success:
            print(f"Added {people} to flight successfully")
    else:   
            print(f"no more available seats for {people}")          