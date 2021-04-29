melon_cost = 1.00

def customer_data(file_path):
    """function takes in a file path and returns customer information

    reads file path and returns whether a customer has over or underpaid
    for their melons"""
    print('Melon Report')
    data_report = open(file_path) #opens input file

    for line in data_report:
        words = line.split('|') #splits words at the '|' symbol

        customer_name = words[1] #sets customer name as second column as file
        customer_melons = float(words[2]) #sets amount of melons bought as third column and as a decimal number
        customer_paid = float(words[3]) #sets amount customer paid as fourth column and as a decimal number
        customer_expected = customer_melons * melon_cost 
        #sets amount customer expected to pay as the number of melons bought multiplied by the melon's cost
        
        if customer_expected > customer_paid:
            print(f"{customer_name} *UNDERPAID!* paid: ${customer_paid:.2f}, expected ${customer_expected:.2f}")
            #if statement checks if the expected amount is more than amount customer paid
        elif customer_expected < customer_paid:
            print(f"{customer_name}OVERPAID! paid: ${customer_paid:.2f}, expected ${customer_expected:.2f}")
            #elif statement checks if the expected amount is less than amount customer paid
        elif customer_expected == customer_paid:
            print(f"{customer_name} paid correctly! paid: ${customer_paid:.2f}")
            #elif statement checks if the expected amount equals amount customer paid

customer_data("customer-orders.txt")
