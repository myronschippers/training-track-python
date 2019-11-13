# ----------------------------------------------------------------------
# STARTING CODE
# ----------------------------------------------------------------------

TICKET_PRICE = 10

tickets_remaining = 100

# ----------------------------------------------------------------------
# CODE ALONG WITH VIDEO
# ----------------------------------------------------------------------

# # Nearly Last Step: Run this code continually until all tickets are sold
# while tickets_remaining > 0:

#     # Output how many tickets are remaining
#     print("There are {} tickets remaining.".format(tickets_remaining))
#     # matched exactly what the instructor did on first try
    
#     # Gather the user's name and assign it to a new variable
#     # my solution
#     #username = input("What's your name? ")
#     #print("Hello, {}!".format(username))
#     # instructor solution
#     name = input("What is your name? ")
    
#     # Prompt the user by name and ask how many tickets they would like
#     num_tickets = input("How many tickets would you like, {}? ".format(name))
#     num_tickets = int(num_tickets)
    
#     # Calculate the price (number of tickets multiplied by the price) and assign it to a variable
#     amount_due = num_tickets * TICKET_PRICE
    
#     # Output the price to the screen
#     print("The total due is ${}".format(amount_due))
    
#     # Prompt user if they want to proceed, Y/N?
#     will_purchase = input("{} would you like to purchase these tickets (Y/N)? ".format(name))
    
#     # If they want to proceed
#     if will_purchase.lower() == "y":
#         # Print out "SOLD!, to confirm the purchase
#         # TODO: Gather credit card information and process it.
#         print("SOLD!")
#         # and then decrement the tickets remaining less the tickets that were purchased
#         tickets_remaining -= num_tickets
#     # Otherwise...
#     else:
#         # Thank them by name
#         print("Thank you anyways, {}.".format(name))

# # Notify the user when tickets are sold out
# print("Sorry the tickets are all sold all sold out :(")

# ----------------------------------------------------------------------
# MAKING CODE LOOP UNTIL ALL TICKETS ARE SOLD
# ----------------------------------------------------------------------

# while tickets_remaining > 0:
#     print("There are {} tickets remaining.".format(tickets_remaining))
#     name = input("What is your name? ")
#     num_tickets = input("How many tickets would you like, {}? ".format(name))
#     # Expect a ValueError to happen and handle it appropriately...
#     try:
#         num_tickets = int(num_tickets)
#         # Raise a ValueError if the requested tickets are more than the available tickets
#         if num_tickets > tickets_remaining:
#             raise ValueError("There are only {} tickets remaining. ".format(tickets_remaining))
#     except ValueError as err:
#         # Include error text in the output
#         print("Oh no, we ran into an issue. {} Please try again. ".format(err))
#     else:
#         amount_due = num_tickets * TICKET_PRICE
#         print("The total due is ${}".format(amount_due))
#         will_purchase = input("{} would you like to purchase these tickets (Y/N)? ".format(name))
#         if will_purchase.lower() == "y":
#             # TODO: Gather credit card information and process it.
#             print("SOLD!")
#             tickets_remaining -= num_tickets
#         else:
#             print("Thank you anyways, {}.".format(name))

# print("Sorry the tickets are all sold all sold out :(")

# ----------------------------------------------------------------------
# ADDING SERVICE CHARGES TO TICKET PURCHASE
# ----------------------------------------------------------------------

# Create a new constant for the 2 dollar service charge
SERVICE_CHARGE = 2

# Create calculate_price function
# - it takes number of tickets and returns num_tickets * TICKET_PRICE
def calculate_price(number_of_tickets):
    # Add the service charge to the result
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining > 0:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("How many tickets would you like, {}? ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining. ".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {} Please try again. ".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        will_purchase = input("{} would you like to purchase these tickets (Y/N)? ".format(name))
        if will_purchase.lower() == "y":
            # TODO: Gather credit card information and process it.
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}.".format(name))

print("Sorry the tickets are all sold all sold out :(")
    