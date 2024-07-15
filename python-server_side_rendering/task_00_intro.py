def generate_invitations(template, attendees):
    """Generate invitations for attendees based on a template."""
    if not isinstance(template, str):
        raise TypeError("template must be a string")
    if not isinstance(attendees, list):
        raise TypeError("attendees must be a list")
    if template is None:
        raise ValueError("Template is empty, no output files generated.")
    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    for i, attendee in enumerate(attendees, start=1):
        invitation = template.format(**attendee)
        output_file = f"output_{i}.txt"
        with open(output_file, "w") as file:
            for key, value in attendee.items():
                if value is None:
                    value = "N/A"
                invitation = invitation.replace("{" + key + "}", str(value))
            file.write(invitation)
