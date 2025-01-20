import django
import os
import sys
from pathlib import Path

# Add project path (root directory where manage.py is located)
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Define Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patholensProject.settings")

# Initialize Django
django.setup()

from fcd.models import *


def get_sessions_of_user():


def create_session():
    # TODO Implement
    Session.objects.create()
def get_dataset_id():

def get_diagnosis():

def set_diagnosis():