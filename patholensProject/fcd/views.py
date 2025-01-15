from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.
class DatasetAPIVied(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def post(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def put(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def patch(self, request, dataset_id: int):        
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
