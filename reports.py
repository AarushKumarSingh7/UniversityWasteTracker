from algorithms import summation, find_maximum, count_items
from algorithms import remove_duplicates, partition_records
from data import CATEGORIES, LOCATIONS


def total_waste_report(records):
    quantities = []

    for record in records:
        quantities.append(record["quantity"])

    total = summation(quantities)
    maximum = find_maximum(quantities)

    print("\n---------- TOTAL WASTE REPORT ----------")
    print("Number of records:", len(records))
    print("Total waste:", total, "kg")
    print("Largest single record:", maximum, "kg")


def category_report(records):
    print("\n---------- CATEGORY-WISE REPORT ----------")

    categories_present = []

    for record in records:
        categories_present.append(record["category"])

    categories_present = remove_duplicates(categories_present)

    for category in CATEGORIES:
        category_records = partition_records(records, category)
        quantity_list = []

        for record in category_records:
            quantity_list.append(record["quantity"])

        total = summation(quantity_list)
        count = count_items(categories_present, category)

        if total > 0:
            print(category, "->", total, "kg", "| Records:", len(category_records))
        elif count == 0:
            print(category, "-> 0 kg | Records: 0")


def location_report(records):
    print("\n---------- LOCATION-WISE REPORT ----------")

    for location in LOCATIONS:
        total = 0
        count = 0

        for record in records:
            if record["location"] == location:
                total = total + record["quantity"]
                count = count + 1

        print(location, "->", total, "kg", "| Records:", count)


def daily_report(records):
    print("\n---------- DATE-WISE REPORT ----------")

    dates = []

    for record in records:
        dates.append(record["date"])

    dates = remove_duplicates(dates)

    for date in dates:
        total = 0

        for record in records:
            if record["date"] == date:
                total = total + record["quantity"]

        print(date, "->", total, "kg")
