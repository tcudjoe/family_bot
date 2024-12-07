import os

TEMPLATE_DIR = "templates/"

def load_template(template_name, **kwargs):
    """Load a template and format it with the provided keyword arguments."""
    template_path = os.path.join(TEMPLATE_DIR, template_name)
    with open(template_path, "r") as file:
        content = file.read()
    return content.format(**kwargs)
