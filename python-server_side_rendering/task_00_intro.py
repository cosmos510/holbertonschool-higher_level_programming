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

    class DefaultDict(dict):
        def __missing__(self, key):
            return 'N/A'

        def __getitem__(self, key):
            return dict.get(self, key, 'N/A') or 'N/A'

    for i, attendee in enumerate(attendees, start=1):
        invitation = template.format_map(DefaultDict(attendee))
        output_file = f"output_{i}.txt"
        with open(output_file, "w") as file:
            file.write(invitation)
