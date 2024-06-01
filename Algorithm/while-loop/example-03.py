def process_payment(amount):
    card_number = input("Please submit your card number: ")
    expiry_date = input("Please submit the expiry date:")
    cvv = input("Enter CVV")
    if len(card_number) == 5 and expiry_date and cvv:
        return True
    else:
        return False

def make_payment():
    while True:
        amount = float(input("Enter the amount to be paid: €"))
        if process_payment(amount):
            print("Payment successful")
            break
        else:
            print("Payment failed. Try again.")
        choice = input("Do you want to cancel the payment? ")
        if choice == "Yes":
            print("Payment cancelled.")
            break