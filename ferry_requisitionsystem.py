ticket_number = 20000

all_bookings = []

# The code below is used from the ( PART A- resit )  
class BookingSystem():
    def __init__(self):
        global ticket_number
        ticket_number += 1

        self.form_of_id = input("Form of ID (Passport, driver’s license): ")
        self.id_number = input("Enter ID number: ")
        self.name = input("Enter your name: ")
        self.ticket_id = ticket_number
        self.service_price = 0
        self.status = "Pending"
        self.approval_ref = ""

    
# providing the customer data..
    def customer_info(self):
        print("\n Customer Info ")
        print("Customer Name:", self.name)
        print("ID Type:", self.form_of_id)
        print("ID Number:", self.id_number)

# allowing the user to add services and their prices
    def ferry_service_details(self):
        print("\nFerry Services ")
        total = 0
        while True:
            service = input("Enter the service name (or type 'done'): ")
            if service.lower() == 'done':
                break
            try:
                price = float(input(f"Enter price for {service}: $"))
                total += price
            except ValueError:
                print("Invalid price. Please enter a number.")
        self.service_price = total
        return total

# Making the decesion of  booking approval status
    def booking_approval(self):
        if self.service_price < 500:
            self.status = "Not approved"
        elif self.service_price >= 500:
            self.status = "Pending"

        else:
            self.status = "Approved"
        self.approval_ref = self.id_number[:4]

    
# for final output results printing out all the booking details..
    def display_booking_info(self):
        print("\n Printing Booking : ")
        print("Form of ID:", self.form_of_id)
        print("ID Number:", self.id_number)
        print("Passenger Name:", self.name)
        print("Ticket ID:", self.ticket_id)
        print("Total: $", self.service_price)
        print("Status:", self.status)
        print("Approval Ref:", self.approval_ref)

# Creating loop for 5 bookings 
for i in range(5):
    print(f"\nBooking {i+1}")
    booking = BookingSystem()
    booking.customer_info()
    booking.ferry_service_details()
    booking.booking_approval()
    all_bookings.append(booking)

for b in all_bookings:
    b.display_booking_info()

# Show the booking summary....
print("\nBooking Statistics")
print("Total bookings:", len(all_bookings))

approved = 0
pending = 0
not_approved = 0


# Going through the each booking and update counters based on their status which is Approved / Pending or Not approved
for b in all_bookings:
    if b.status == "Approved":
        approved += 1
    elif b.status == "Pending":
        pending += 1
    elif b.status == "Not approved":
        not_approved += 1
        
#  Showing how many were Approved, Pending, or Not approved from the given data

print("Approved:", approved)
print("Pending:", pending)
print("Not approved:", not_approved)
