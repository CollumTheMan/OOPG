# Lines Collum Did : 1-5, 11-17, 28-30
# Lines Jaqueline Did : 6-11,17-24,30-33
class parking_garage():
    def __init__(self):
        self.tickets=10
        self.parking_spaces=10
        self.current_ticket={}
    def take_ticket(self):
        self.parking_spaces-=1
        self.tickets-=1
        self.current_ticket[str(self.tickets)]="unpaid"
        print("You have ticket ", self.tickets)
        return self.tickets
    def pay_for_parking(self):
        ticket=input("Please pay now, what is your ticket number?")
        ticket_status=None
        if str(ticket) in self.current_ticket:
            ticket_status = self.current_ticket[str(ticket)]
        else:
            print("not a valid ticket")
            return
        if ticket_status == "unpaid":
            print("ticket has been paid get out, you have 15 minutes")
            self.current_ticket[ticket]="paid"
        else:
            print("ticket has been paid")
    def leave_garage(self):
        ticket = input("what is your ticket")
        paid=None
        if str(ticket) in self.current_ticket:
            paid=self.current_ticket[str(ticket)]
        if paid == "paid":
            print("Thank you bye")
        else:
            ticket=input("please pay now")
            self.current_ticket[ticket]="paid"
            print("thanks bye")
        self.parking_spaces+=1
        self.tickets+=1
pg = parking_garage()
while True:
    ticket = None
    prompt = input("Welcome to The Dope Cool Awesome Garage, would you like to Take a ticket(T), Pay for parking(P), Leave The Dope Cool Awesome Garage(L) or Quit(Q)?")

    if prompt == "T":
        ticket = pg.take_ticket()
    elif prompt == "P":
        pg.pay_for_parking()
    elif prompt == "L":
        pg.leave_garage()
    elif prompt == "Q":
        break