# Sentinel Security Services
Cybersecurity Incident Tracker

## Business Problem
Sentinel Security Services is a small managed security service provider (MSSP) that monitors cybersecurity incidents for multiple business clients. The application allows security analysts to record incidents, track their severity and status, and maintain a history of incident closures.

## Business Question
How many security analysts are needed to keep the unresolved incident backlog at or below 10 incidents during a 30-day period?

## How to Run
1. Open the project folder in VS Code.
2. Make sure Python is installed.
3. Open the terminal and run `python main.py`.
4. Choose an option from the menu.
5. Select option 7 to save changes and exit.

## Menu Options
1. **View All Incidents** — Displays all recorded security incidents.
2. **Report New Incident** — Adds a new incident or updates the status of an existing incident.
3. **Close an Incident** — Closes an open incident and records the action in the activity history.
4. **View Incident Statistics** — Coming soon.
5. **Run 30-Day Simulation** — Coming soon.
6. **Display Charts** — Coming soon.
7. **Save and Exit** — Saves incident and activity records to CSV files before closing the program.

## Files
- `main.py` — Runs the application menu and contains the incident management functions.
- `incidents.csv` — Stores incident IDs, client names, incident types, severity levels, and statuses.
- `activities.csv` — Stores the date, incident ID, client, and action for recorded incident closures.
- `README.md` — Explains the project and how to run it.

## Author
Joseph McClish
