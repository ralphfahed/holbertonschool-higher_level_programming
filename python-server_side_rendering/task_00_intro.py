import os  # Import os module to work with file system operations like checking if a file exists

def generate_invitations(template, attendees):
    # Check if 'template' is a string; if not, print error and stop function
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if 'attendees' is a list of dictionaries; if not, print error and stop function
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Remove leading and trailing whitespace from template and check if empty
    # If empty, print error and stop function without creating files
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty; if so, print a message and stop function
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Loop over the list of attendees, enumerate gives index starting from 1
    for i, attendee in enumerate(attendees, start=1):
        invitation = template  # Start with the original template for each attendee

        # For each expected placeholder key, get its value from the attendee dictionary
        # If the key is missing or the value is None, replace it with "N/A"
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)  # Get value from dictionary
            if value is None:
                value = "N/A"  # Substitute "N/A" for missing data
            # Replace the placeholder in the template with the actual value (or "N/A")
            invitation = invitation.replace(f"{{{key}}}", str(value))

        filename = f"output_{i}.txt"  # Define the output filename (output_1.txt, output_2.txt, ...)

        # Check if the output file already exists
        # If it does, print a warning (optional, can be removed if you want silent overwrite)
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists and will be overwritten.")

        # Try to write the personalized invitation content to the output file
        try:
            with open(filename, 'w') as file:  # Open the file for writing
                file.write(invitation)          # Write the invitation text into the file
        except Exception as e:
            # If any error occurs during writing, print the error message
            print(f"Error writing to {filename}: {e}")

