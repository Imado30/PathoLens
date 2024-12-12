import uuid
import os
import sys
import django
from pathlib import Path
import random

# Add project path (root directory where manage.py is located)
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Define Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patholensProject.settings")

# Initialize Django
django.setup()


import image.dataHandler as dataHandler
from accounts.models import Doctors


def createDoctor(user: django.contrib.auth.models.User):
    """
    Creates a new doctor entry in the database.

    Args:
        user (django.contrib.auth.models.User):  The`User`object representing the doctor to be created.

    Returns:
        Doctors: The created doctor object, including information about the remaining and finished patients.
    """

    doc = Doctors.objects.create(
        doctorID=user, finishedPatients = {}
    )

    return doc


def addIdsToUrls(allDataSets: list, allUrls: dict):
    """
    Generates a dictionary that associates each dataset with patient IDs and their respective picture URLs.

    Args:
        allDataSets (list): A list of dataset names to be processed.
        allUrls (dict): A dictionary containing URLs for the pictures, structured as:
            {
                "dataSetName":
                {
                    "urls": ["url1", "url2", ...]
                },
                ...
            }

    Returns:
        dict: An dictionary which has the following format:
            {
                "dataSet":
                {
                    "patient id": "url to the picture",
                    ...
                },
                ...
            }
    """

    idsAndUrls = {}

    for dataSet in allDataSets:
        urls = allUrls[dataSet]["url"]
        amount = len(urls)
        patientIDs = createUUIDs(amount)

        # Initialize the dictionary for dataSet if it does not exist yet
        if dataSet not in idsAndUrls:
            idsAndUrls[dataSet] = {}

        # Add urls and uuids to dictionary
        for index in range(amount):
            idsAndUrls[dataSet][patientIDs[index]] = urls[index]

    return idsAndUrls


def createUUIDs(amount: int):
    """
    Generates a specified number of unique UUIDs (Universally Unique Identifiers).

    Args:
        amount (int): The number of unique UUIDs to generate.

    Returns:
        list: A list of randomly generated UUIDs in string format.
    """
    allUUIDs = []
    for i in range(amount):
        allUUIDs.append(str(uuid.uuid4()))

    return allUUIDs


def getRandomIDAndURL(docID: str, dataSet: str):
    """

    Returns a random diagnosis id with the linked url from the doctors`remainingPatients`dictionary.

    Args:
        docID (str): The unique identifier of the doctor
        dataSet (str): The name of the dataset, which must exist within the`remainingPatients`dictionary associated with the doctor.

    Raises:
        KeyError: If the specified dataset (dataSet) is not found in the doctor's`remainingPatients`dictionary.

    Returns:
        tuple: A tuple containing:
            - str: The ID of the diagnosis entry.
            - str: The URL of the picture.
        Returns False if no remaining patients are available or the doctor does not exist.
    """
    # Check if the doctor exists in the database
    if not Doctors.objects.filter(doctorID=docID).exists():
        return False

    doctor = Doctors.objects.get(doctorID=docID)

    if dataSet not in doctor.remainingPatients:
        raise KeyError(f"Data set '{dataSet}' not found for doctor {docID}")

    remainingPatients = doctor.remainingPatients
    remainingPatientsAsList = list(remainingPatients[dataSet].keys())

    # Return False if no remaining patients are available
    if len(remainingPatientsAsList) <= 0:
        return False

    # Randomly select a patient from the remaining ones
    index = random.randint(0, len(remainingPatientsAsList) - 1)

    idForPicture = remainingPatientsAsList[index]
    urlForPicture = remainingPatients[dataSet][idForPicture]

    return (idForPicture, urlForPicture)


def getDoctorObject(docID: str):
    """
    Returns the object to the linked doctor

    Args:
        docID (str): The ID of the doctor

    Returns:
        Doctor: Returns the object of the Doctor
    """

    # Check if the doctor exists in the database
    if not Doctors.objects.filter(doctorID=docID).exists():
        return False

    doctor = Doctors.objects.get(doctorID=docID)
    return doctor


def addFinishedPatient(docID: str, datasetUrlKey: str, url: str):
    
    # Check if the doctor exists in the database
    if not Doctors.objects.filter(doctorID=docID).exists():
        return False

    doctor = Doctors.objects.get(doctorID=docID)    
    finishedPatients = doctor.finishedPatients
    
    # create unique id
    uuid = createUUIDs(1)[0]   
    if datasetUrlKey not in finishedPatients:
        finishedPatients[datasetUrlKey] = {}

    finishedPatients[datasetUrlKey][uuid] = url

    return True