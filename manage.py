import os

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogmaker_lite.settings")

    # handles setting up the settings and running the server
    execute_from_command_line()
