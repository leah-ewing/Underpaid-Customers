melon_cost = 1.00

def customer_data(file_path):
    """function takes in a file path and returns in customer information

    reads file path and returns whether a customer has over or underpaid
    for their melons"""
    print('Melon Report')
    data_report = open(file_path) #opens input file

    for line in data_report:
        line = line.rstrip()
        words = line.split('|') #splits words at the '|' symbol

        customer_name = words[1] #sets customer name as second column in file
        customer_melons = float(words[2]) #sets melon bought count as third column
        customer_paid = float(words[3]) #sets customer paid amount as fourth column

    customer_expected = customer_melons * melon_cost 
    if customer_expected != customer_paid:  
        print(f"{customer_name} paid ${customer_melons:.2f}, expected ${melon_cost:.2f}")

customer_data("customer-orders.txt")
