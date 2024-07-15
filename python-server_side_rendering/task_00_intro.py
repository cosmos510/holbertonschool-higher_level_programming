def generate_invitations(template, attendees):
    """Generate invitations for attendees based on a template."""
    if not isinstance(template, str):
        print("template must be a string")
        return
    if not isinstance(attendees, list):
        print("attendees must be a list")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for i, attendee in enumerate(attendees, start=1):
        invitation = template.format(**attendee)
        output_file = f"output_{i}.txt"
        with open(output_file, "w") as file:
            for key, value in attendee.items():
                if value is None:
                    value = "N/A"
                invitation = invitation.replace("{" + key + "}", str(value))
            file.write(invitation)
