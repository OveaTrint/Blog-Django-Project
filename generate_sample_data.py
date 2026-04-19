"""Script to generate some data"""

import os
from argparse import ArgumentParser

import django
from django.core.management import call_command

# Load the settings
# Settings always need to be loaded when running a .py file directly in a django project
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
os.environ["DJANGO_SUPERUSER_PASSWORD"] = "fake_pw"
django.setup()

parser = ArgumentParser()
parser.add_argument("--num_of_blogs", default=10)
parser.add_argument("--num_of_posts", default=100)
args = parser.parse_args()

cmd = "createsuperuser --username kamal"
cmd += " --email fake_email@example.com"
cmd += " --noinput"

cmd_parts = cmd.split()


# Flush current data
call_command("flush", "--noinput")
print("flushed existing db")

# set up admin/superuser account
call_command(*cmd_parts)

# moved the import here because model_factory needs models that must be set up by django before they are used.
from model_factory import BlogFactory, BlogPostFactory

for _ in range(args.num_of_blogs):
    BlogFactory.create()

for _ in range(args.num_of_posts):
    BlogPostFactory.create()
