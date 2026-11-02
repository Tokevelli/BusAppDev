def show_menu():
    print("\n=== Sentinel Security Services ===")
    print("1. View All Incidents")
    print("2. Report New Incident")
    print("3. Close an Incident")
    print("4. View Incident Statistics")
    print("5. Run 30-Day Simulation")
    print("6. Display Charts")
    print("7. Save and Exit")


def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "7":
            print("Exiting Sentinel Security Services.")
            break

        elif choice == "1":
            print("Coming soon")

        elif choice == "2":
            print("Coming soon")

        elif choice == "3":
            print("Coming soon")

        elif choice == "4":
            print("Coming soon")

        elif choice == "5":
            print("Coming soon")

        elif choice == "6":
            print("Coming soon")

        else:
            print("Invalid option. Please choose 1-7.")


main()

