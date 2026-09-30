from data import create_sample_data
from tracker import add_waste, display_all_waste
from reports import category_report, location_report, daily_report, total_waste_report


def show_menu():
    print("\n========== UNIVERSITY WASTE TRACKER ==========")
    print("1. Add waste record")
    print("2. View all waste records")
    print("3. Total waste report")
    print("4. Category-wise report")
    print("5. Location-wise report")
    print("6. Date-wise report")
    print("7. Exit")
    print("==============================================")


def main():
    records = create_sample_data()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_waste(records)
        elif choice == "2":
            display_all_waste(records)
        elif choice == "3":
            total_waste_report(records)
        elif choice == "4":
            category_report(records)
        elif choice == "5":
            location_report(records)
        elif choice == "6":
            daily_report(records)
        elif choice == "7":
            print("Thank you for using University Waste Tracker.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()
