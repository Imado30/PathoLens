from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Diagnosis
import os
from django.shortcuts import get_object_or_404



class GetImageAPIView(APIView):
    """API Class to get the image to a given diagnosisID
       (now its still the imageID for testing reasons)

    Args:
        APIView (_type_): APIView imported from python
    """

    def get(self, request, imageID):
        """Function to get the image to a given diagnosisID
           (now its still the imageID for testing reasons)

        Args:
            request (_type_): _description_
            imageID (string): ID of an Image

        Returns:
            Path: The path to find the requestet image
        """
        
        try:
            imageFormat = request.GET.get("format ")
            if not imageFormat:
                print("Format parameter missing; using default FLAIR.")
                imageFormat = "FLAIR"

            imageFormat = imageFormat.upper()


            if imageFormat not in settings.SUPPORTED_IMAGE_FORMATS:
                return JsonResponse({"error": "Invalid format"}, status=400)
            
            fileSuffix = settings.SUPPORTED_IMAGE_FORMATS[imageFormat]

            imagePath = os.path.join(settings.MEDIA_ROOT, f"website_data/sub-{imageID}/anat/sub-{imageID}{fileSuffix}")
            if not os.path.exists(imagePath):
                return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)
            
            # relative path for the client
            relativePath = f"/media/website_data/sub-{imageID}/anat/sub-{imageID}{fileSuffix}"
            return Response({"path": relativePath}, status=status.HTTP_200_OK)


        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class SaveConfidenceAPIView(APIView):
    def post(self, request, diagID):
        try:
            
            data = request.data
            confidence = data.get('confidence')

            # check if it is a valid value 
            if confidence is None or not (0 <= int(confidence) <= 100):
                return Response({'error': 'Invalid confidence value. It must be between 0 and 100.'}, status=status.HTTP_400_BAD_REQUEST)

           
            diag = get_object_or_404(Diagnosis, diagID=diagID)

            # store confidence value 
            diag.confidence = int(confidence)
            diag.save()

            return Response({'message': 'Confidence value saved successfully via API!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
