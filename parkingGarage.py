class parking_garage():
    def __init__(self):
        self.tickets=10
        self.parking_spaces=10
        self.current_ticket={}
    def take_ticket(self):
        self.parking_spaces-=1
        self.tickets-=1
        return self.tickets
    def pay_for_parking(self):
        ticket=input("Please pay now")
        if ticket is not None:
            print("ticket has been paid get out, you have 15 minutes")
            self.current_ticket[ticket]="paid"
    def leave_garage(self, ticket):
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
ticket = pg.take_ticket()
ticket2 = pg.take_ticket()
pg.pay_for_parking()
pg.leave_garage(ticket)
pg.leave_garage(ticket2)