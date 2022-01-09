from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from department.models import Department
from asset.models import Asset
from .serializers import  DepartmentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class DepartmentCreate(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class =DepartmentSerializer
    def post(self, request,asset_name,format="json"):
        serializer = DepartmentSerializer(data=request.data)
        asset=Asset.objects.get(name=asset_name)
        request.data['assets']=asset.id
        if serializer.is_valid():
            serializer.save()
        return Response({"Status":" Created","Data":serializer.data}, status=status.HTTP_201_CREATED)