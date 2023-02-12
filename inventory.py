#========The beginning of the class==========

class Shoe:
    # Initializes instance variables for country, code, product, cost, and quantity
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Returns cost of the shoe
    def get_cost(self):
        return self.cost

    # Returns quantity of the shoe
    def get_quantity(self):
        return self.quantity

    # String representation of the Shoe object
    def __str__(self):
        return f"{self.code} - {self.product} ({self.country}) - cost: {self.cost}, quantity: {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
# Function to read shoe data from a file 'inventory.txt'
def read_shoes_data():
    try:
        with open("inventory.txt") as file:
            next(file) # skip first line as it may contain header information
            for line in file:
                # split the line by comma and assign values to respective variables
                country, code, product, cost, quantity = line.strip().split(",")
                # convert cost and quantity from string to float and int, respectively
                cost = float(cost)
                quantity = int(quantity)
                # create a Shoe object and append to shoe_list
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        # Handle FileNotFoundError if the file 'inventory.txt' is not found
        print("The file 'inventory.txt' could not be found.")
    except Exception as e:
        # Handle any other exception that may occur while reading the file
        print(f"An error occurred while reading the file: {e}")

# Function to capture new shoe data from user input
def capture_shoes():
    # Prompt user for shoe data
    country = input("Enter country of origin: ")
    code = input("Enter product code: ")
    product = input("Enter product name: ")
    cost = float(input("Enter product cost: "))
    quantity = int(input("Enter quantity: "))
    # Create a Shoe object and append to shoe_list
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

# Function to view all shoes in the shoe_list
def view_all():
    for shoe in shoe_list:
        print(shoe)

# Function to restock a shoe with the least quantity
def re_stock():
    # Find the index of shoe with the least quantity
    min_index = 0
    min_quantity = shoe_list[0].get_quantity()
    for i, shoe in enumerate(shoe_list):
        if shoe.get_quantity() < min_quantity:
            min_index = i
            min_quantity = shoe.get_quantity()
    # Prompt user for additional quantity and add it to the shoe
    shoe = shoe_list[min_index]
    add = int(input(f'''
Re-stock {shoe.product} ({shoe.code})? Current quantity: {shoe.quantity}. 
Enter additional quantity: (If you don't want to add stock just enter 0) '''))
    shoe.quantity += add

# Function to search for a shoe with a given code
def search_shoe(code):
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return None

# Function to calculate value (cost * quantity) of each shoe
def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} ({shoe.code}) - value: {value}")

# Function to find the product with the highest quantity and list for sale
def highest_qty():
    # Initialize max_index to 0 and set max_quantity to the quantity of the first shoe in the shoe_list
    max_index = 0
    max_quantity = shoe_list[0].get_quantity()
    # Iterate through the shoes in shoe_list
    for i, shoe in enumerate(shoe_list):
        # If the current shoe's quantity is greater than the current max_quantity,
        # Set the current index to max_index and the current quantity to max_quantity
        if shoe.get_quantity() > max_quantity:
            max_index = i
            max_quantity = shoe.get_quantity()

    # Get the shoe with the highest quantity from the shoe_list using the max_index
    shoe = shoe_list[max_index]
    # Print the product name, product code, and highest quantity of the shoe with the highest quantity
    print(f"{shoe.product} ({shoe.code}) has highest quantity: {shoe.quantity}")


#==========Main Menu=============
# Main function of the Shoe Inventory System
def main():
    while True:
        # Menu options
        print("\nShoe Inventory System")
        print("1. Read shoes data")
        print("2. Capture shoe")
        print("3. View all shoes")
        print("4. Re-stock shoe")
        print("5. Search for a shoe")
        print("6. Value per item")
        print("7. Highest quantity shoe")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        # User choice
        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            view_all()
        elif choice == 4:
            re_stock()
        elif choice == 5:
            code = input("Enter shoe code: ")
            shoe = search_shoe(code)
            if shoe:
                print(shoe)
            else:
                print("Shoe not found.")
        elif choice == 6:
            value_per_item()
        elif choice == 7:
            highest_qty()
        elif choice == 8:
            print('Goodbye!')
            quit()
        else:
            print("Invalid choice.")


# Call the main function
if __name__ == "__main__":
    main()
