from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.
class DatasetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def post(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def put(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def patch(self, request, dataset_id: int):        
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

class SessionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def post(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def put(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def patch(self, request, dataset_id: int):        
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

class LoginAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def post(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def put(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def patch(self, request, dataset_id: int):        
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

class StudyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def post(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def put(self, request, dataset_id: int):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def patch(self, request, dataset_id: int):        
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
