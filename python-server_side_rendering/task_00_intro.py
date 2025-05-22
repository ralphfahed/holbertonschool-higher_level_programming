# task_00_intro.py

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders or use 'N/A' if missing
        personalized = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            personalized = personalized.replace(f"{{{key}}}", value if value else "N/A")

        # Write to file
        with open(f"output_{idx}.txt", "w") as f:
            f.write(personalized)

