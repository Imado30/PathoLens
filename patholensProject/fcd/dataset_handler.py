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

def get_dataset_to_id(id: int):
    Dataset.objects.get()

def add_dataset_to_database(path_to_dataset: str):

def get_available_masks_for_dataset(id: int):