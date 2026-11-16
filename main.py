from datetime import date
import csv


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
    load_incidents()
    load_activities()

    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "7":
            save_incidents()
            save_activities()
            print("Incidents saved successfully.")
            print("Exiting Sentinel Security Services.")
            break

        elif choice == "1":
            view_incidents()

        elif choice == "2":
            report_incident()

        elif choice == "3":
            close_incident()

        elif choice == "4":
            print("Coming soon")

        elif choice == "5":
            print("Coming soon")

        elif choice == "6":
            print("Coming soon")

        else:
            print("Invalid option. Please choose 1-7.")


# Stores incident records loaded from the CSV file
incidents = {}

# Stores incident activity transacgtions
activities = []

# Loads incident records from incidents.csv.
def load_incidents():
    with open("incidents.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            incident_id = int(row["id"])

            incidents[incident_id] = {
                "client": row["client"],
                "type": row["type"],
                "severity": row["severity"],
                "status": row["status"]
            }


# Saves incident records to incidents.csv.
def save_incidents():
    with open("incidents.csv", "w", newline="") as file:
        fieldnames = ["id", "client", "type", "severity", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for incident_id in incidents:
            incident = incidents[incident_id]

            writer.writerow({
                "id": incident_id,
                "client": incident["client"],
                "type": incident["type"],
                "severity": incident["severity"],
                "status": incident["status"]
            })



# Loads previously recorded activities from activities.csv.
def load_activities():
    try:
        with open("activities.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                activities.append({
                    "date": row["date"],
                    "incident_id": int(row["incident_id"]),
                    "client": row["client"],
                    "action": row["action"]
                })

    except FileNotFoundError:
        print("No previous activity records found.")


# Saves activity transactions to activities.csv.
def save_activities():
    with open("activities.csv", "w", newline="") as file:
        fieldnames = ["date", "incident_id", "client", "action"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for activity in activities:
            writer.writerow(activity)


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


# Incident types and their assigned severity
incident_types = {
    "1": {"type": "Suspicious Login", "severity": "Low"},
    "2": {"type": "Phishing", "severity": "Medium"},
    "3": {"type": "Malware", "severity": "High"},
    "4": {"type": "Account Compromise", "severity": "High"},
    "5": {"type": "Unauthorized Access", "severity": "Critical"}
}


# Adds a new security incident or updates an existing one.
def report_incident():
    print("\n=== Report or Update Incident ===")

    incident_id = input("Enter incident ID: ")

    # Check that the ID contains only numbers
    if not incident_id.isdigit():
        print("Invalid ID. Please enter a number.")
        return

    incident_id = int(incident_id)

    # Update an existing incident
    if incident_id in incidents:
        print("Incident already exists.")
        print("Current status:", incidents[incident_id]["status"])

        new_status = input("Enter new status (Open/Closed): ")

        if new_status == "Open" or new_status == "Closed":
            incidents[incident_id]["status"] = new_status
            print("Incident updated successfully.")
        else:
            print("Invalid status. No changes made.")

    # Create a new incident
    else:
        client = input("Enter client name: ").strip()

        if client == "":
            print("Client name cannot be empty.")
            return

        print("\nIncident Types:")
        for key in incident_types:
            print(key + ".", incident_types[key]["type"])

        type_choice = input("Select incident type (1-5): ")

        if type_choice not in incident_types:
            print("Invalid incident type.")
            return

        incident_type = incident_types[type_choice]["type"]
        severity = incident_types[type_choice]["severity"]

        incidents[incident_id] = {
            "client": client,
            "type": incident_type,
            "severity": severity,
            "status": "Open"
        }

        print("New incident added successfully.")


# Closes an open incident and records the action as a transaction.
def close_incident():
    print("\n=== Close an Incident ===")

    incident_id = input("Enter incident ID to close: ")

    if not incident_id.isdigit():
        print("Invalid ID. Please enter a number.")
        return

    incident_id = int(incident_id)

    if incident_id not in incidents:
        print("Incident not found.")
        return

    if incidents[incident_id]["status"] == "Closed":
        print("This incident is already closed.")
        return

    incidents[incident_id]["status"] = "Closed"

    activities.append({
        "date": str(date.today()),
        "incident_id": incident_id,
        "client": incidents[incident_id]["client"],
        "action": "Closed"
    })

    print("Incident closed and activity recorded.")


main()

