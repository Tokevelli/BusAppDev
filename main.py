#lists the menu options
def show_menu():
    print("\n=== Sentinel Security Services ===")
    print("1. View All Incidents")
    print("2. Report New Incident")
    print("3. Close an Incident")
    print("4. View Incident Statistics")
    print("5. Run 30-Day Simulation")
    print("6. Display Charts")
    print("7. Save and Exit")

#while loop that keeps the menu running while user makes selections until 7 is selected
def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "7":
            print("Exiting Sentinel Security Services.")
            break

        elif choice == "1":
            view_incidents()

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


# Sample security incidents
incidents = {
    101: {
        "client": "Bitterroot Family Dental",
        "type": "Phishing",
        "severity": "Medium",
        "status": "Open"
    },
    102: {
        "client": "Clark Fork Accounting",
        "type": "Malware",
        "severity": "High",
        "status": "Closed"
    },
    103: {
        "client": "Missoula Outdoor Supply",
        "type": "Suspicious Login",
        "severity": "Low",
        "status": "Open"
    }
}


# Displays all recorded security incidents.
def view_incidents():
    print("\n=== Recorded Security Incidents ===")

    for incident_id in incidents:
        incident = incidents[incident_id]

        print("\nIncident ID:", incident_id)
        print("Client:", incident["client"])
        print("Type:", incident["type"])
        print("Severity:", incident["severity"])
        print("Status:", incident["status"])


main()

