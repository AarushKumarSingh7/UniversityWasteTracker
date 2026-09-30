from data import CATEGORIES, LOCATIONS


def get_positive_number():
    while True:
        value = input("Enter quantity in kg: ")

        if value.replace(".", "", 1).isdigit():
            quantity = float(value)
            if quantity > 0:
                return quantity

        print("Please enter a positive number.")


def get_category():
    while True:
        print("\nWaste Categories:")
        for i in range(len(CATEGORIES)):
            print(i + 1, ".", CATEGORIES[i])

        choice = input("Choose category number: ")

        if choice.isdigit():
            number = int(choice)
            if number >= 1 and number <= len(CATEGORIES):
                return CATEGORIES[number - 1]

        print("Invalid category.")


def get_location():
    while True:
        print("\nUniversity Locations:")
        for i in range(len(LOCATIONS)):
            print(i + 1, ".", LOCATIONS[i])

        choice = input("Choose location number: ")

        if choice.isdigit():
            number = int(choice)
            if number >= 1 and number <= len(LOCATIONS):
                return LOCATIONS[number - 1]

        print("Invalid location.")


def add_waste(records):
    print("\n---------- ADD WASTE RECORD ----------")
    date = input("Enter date (DD-MM-YYYY): ")
    location = get_location()
    category = get_category()
    quantity = get_positive_number()

    record = {
        "date": date,
        "location": location,
        "category": category,
        "quantity": quantity
    }

    records.append(record)
    print("Waste record added successfully.")


def display_all_waste(records):
    print("\n---------------- ALL WASTE RECORDS ----------------")

    if len(records) == 0:
        print("No records available.")
        return

    print("No.  Date          Location          Category      Kg")
    print("----------------------------------------------------")

    for i in range(len(records)):
        record = records[i]
        print(
            i + 1,
            record["date"],
            record["location"],
            record["category"],
            record["quantity"]
        )
