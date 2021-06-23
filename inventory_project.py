# COSC1519 Introduction to Programming
# Student name: Prottay Karim
# Student number: S3822620
# Practical group:
# Friday 2:30pm (online)

def reading_old():
    """function to read the initial stock file"""
    with open('A3_3822620_stock.txt') as stock_file:
        for line in stock_file:
            line = line.rstrip()
            print(line)


def welcome():
    """function to display welcome message and show stock"""
    print("Welcome store manager 1022!\nLoading file stock.txt\n...\nAll data loaded!")
    print("Item Name, Price, Qty, Size")
    reading_old()


def choices():
    """function to print choices"""
    print("What would you like to do?")
    print('')


def all_stock():
    """function to print all updated stock"""
    print("Item Name, Price, Qty, Size")
    with open("updated_a3_s3822620_stock.txt") as all_stocks:
        view = all_stocks.read()
        print(view)


def one_stock():
    """function to show a single item"""
    item_selection = input("Input Item name: ").lower().strip()
    print("Item Name, Price, Qty, Size")
    fhand = open('updated_a3_s3822620_stock.txt')
    count = 0
    for line in fhand:
        if line.startswith(item_selection):
            print(line)


def add_item():
    """function to add a new item to file"""
    # asking for all information about the file
    item_name = input("Enter item name: ")
    price = float(input("Price of Item: "))
    qty = int(input("How many pieces are there?: "))
    size = input("Size: ")
    new_item = f"{item_name},{price},{qty},{size}"
    with open("updated_a3_s3822620_stock.txt", 'a') as file:
        file.write(new_item)


def remove():
    """funtion to remove a stock"""
    item_name = input("Name the item")
    with open("A3_3822620_stock.txt", "r") as f:
        dse = f.readlines()
    with open("updated_a3_s3822620_stock.txt", "w") as f:
        for i in dse:
            if i.strip("\n") != item_name:
                f.write(i)


def stock_value():
    """function to evaluate stock price"""
    with open("updated_a3_s3822620_stock.txt") as value:
        value = value.readlines()
        print(value)


def main():
    """function to run program"""
    welcome()
    count = True
    print("")
    choices()
    # loop to allow choices
    while count:
        # conditionals to enter choices
        try:
            choice = int(input('1. View all items\n2. Show a single item\n3. Add/Update Item\n4. Save and Exit'))
            if choice == 1:
                all_stock()
            elif choice == 2:
                one_stock()
            elif choice == 3:
                add_item()
            elif choice == 4:
                print("Saving Data...\nSave Complete!/Exiting Program")
                count = False
            else:
                print("\nEnter 1,2,3 or 4\n")
        except:
            print("\nEnter 1,2,3 or 4\n")
            continue
    print('Goodbye!')


main()
