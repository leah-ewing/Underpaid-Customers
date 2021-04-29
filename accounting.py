melon_cost = 1.00

def customer_data(file_path):
    """function takes in a file path and returns in customer information

    reads file path and returns whether a customer has over or underpaid
    for their melons"""
    data_report = open(file_path)
    for line in data_report:
        line = line.rstrip()
        words = line.split('|') #splits words at the '|' symbol

        customer_name = words[1]
        customer_melons = words[2]
        customer_paid = words[3]

    customer_expected = int(customer_melons) * int(melon_cost)
    if customer_expected != customer_paid:
        print("{} paid ${}, expected ${}".format(customer_name, customer_melons, customer_paid))

customer_data("customer-orders.txt")
