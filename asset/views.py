from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from asset.models import Asset
from .serializers import  AssetSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class AssetCreate(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AssetSerializer
    def post(self, request,format="json"):
        serializer =  AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
        return Response({"Status":" Created","Data":serializer.data}, status=status.HTTP_201_CREATED)