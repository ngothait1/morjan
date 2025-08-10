informationoffcustomer = []  

def printlist():
    print("1.Save a new entry", "\n", "2.Search by ID", "\n", "3.print ages average", "\n", "4.print all names", "\n", "5.print all IDs", "\n", "6.print all entries", "\n", "7.print entry by index", "\n", "8.exit", "\n")

def saveNewEntry():  
    choice = input("please Enter your choice: ")
    if choice == "1":
        while True:
            ID = input("ID: ")
            if ID == "stop":
                break
            elif ID.isdigit() == True:
                def duplication():
                    for customer in informationoffcustomer:
                        for j in customer:
                            if j == ID:
                                print("ID already exists ", "ID:", customer[0], "Name:", customer[1], "Age:", customer[2])
                                return False
                    print("ID", end=" " + "[" + str(ID) + "]" + " is saved successfully " + "\n")

                name = input("Name: ")
                age = input("Age: ")
                duplication()
                select = input("press Enter to continue")
                customer = [ID, name, age]
                informationoffcustomer.append(customer)
            else:
                print("ID must be a number")

saveNewEntry()
printlist()
choice = input("please Enter your choice: ")

def searchById():
    search = input("please enter the ID you look for: ")
    for customer in informationoffcustomer:
        if customer[0] == search:
            print("ID:", customer[0], "\nName:", customer[1], "\nAge:", customer[2])
            return
    print("Error: ID", search, " is not saved")
    searchById()

if choice == "2":
    searchById()
    select = input("press Enter to continue")
    printlist()
    choice = input("please Enter your choice: ")

elif choice == "3":
    def printAgesAverage():
        sum = 0
        if len(informationoffcustomer) == 0:
            return 0
        for customer in informationoffcustomer:
            sum += int(customer[2])
        return sum / len(informationoffcustomer)

    print("The average age is:", printAgesAverage())
    select = input("press Enter to continue")
    printlist()
    choice = input("please Enter your choice: ")

elif choice == "4":
    def printAllNames():
        customer = [customer[1] for customer in informationoffcustomer]
        for index, name in enumerate(customer):
            print(index, end="")
            print(".", name)

    printAllNames()
    select = input("press Enter to continue")
    printlist()
    choice = input("please Enter your choice: ")

elif choice == "5":
    def printAllIds():
        customer = [customer[0] for customer in informationoffcustomer]
        for index, Id in enumerate(customer):
            print(index, end="")
            print(".", Id)

    printAllIds()
    select = input("press Enter to continue")
    printlist()
    choice = input("please Enter your choice: ")

elif choice == "6":
    def printAllEntries():
        for index, customer in enumerate(informationoffcustomer):
            print(index, end="")
            print(".", customer[0], "\nName:", end=" " + customer[1] + "\n" + "Age:" + " " + customer[2] + "\n")

    printAllEntries()
    select = input("press Enter to continue")
    printlist()
    choice = input("please Enter your choice: ")

elif choice == "7":
    def printEntryByIndex():
        index = input("please Enter the index index for the entry you want to print: ")
        if index.isdigit() == True:
            index = int(index)
            if 0 <= index < len(informationoffcustomer):
                print(informationoffcustomer[index])
            else:
                print("index out of range. The Maximum index allowed is", len(informationoffcustomer))
        else:
            print("index  must be a number .", index, "is not a number")

    printEntryByIndex()
    select = input("press Enter to continue")
    printlist()
    choice = input("please Enter your choice: ")

elif choice == "8":
    while True:
        user_input = input("Are you sure you want to exit? (y/n) ")
        if user_input == "y":
            print("Goodbye")
            break
        elif user_input == "n":
            printlist()
            choice = input("please Enter your choice: ")

else:
    print("option", "[", choice, "]", "is not exist. Please try again")
    select = input("press Enter to continue")
    printlist()
    choice = input("please Enter your choice: ")
