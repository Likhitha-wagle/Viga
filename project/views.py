from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from project.models import Project
from department.models import Department
from asset.models import Asset
from .serializers import  ProjectSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from wsgiref.util import FileWrapper
from django.http import HttpResponse,FileResponse
import json

class ProjectCreate(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class =ProjectSerializer
    def post(self, request,department_name,format="json"):
        serializer = ProjectSerializer(data=request.data)
        department=Department.objects.get(name=department_name)
        request.data['departments']=department.id
        if serializer.is_valid():
            serializer.save()
        return Response({"Status":" Created","Data":serializer.data}, status=status.HTTP_201_CREATED)

class ArchiveCreate(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self,request,project_id,format="json"):
        projects=Project.objects.filter(id=project_id).values_list('id','name','departments')
        print(projects)
        departments=Department.objects.filter(id=projects[0][2]).values_list('id','name','assets')
        print(departments)
        assets=Asset.objects.filter(id=departments[0][2]).values_list('id','name')
        print(assets)
        dict={}
        dict.update({"project_id":project_id,"project_name":projects[0][1],"department":departments[0][1],"asset":assets[0][1]})
        # dict.update(project_id=2,project_name="project2",department="department2",asset="asset2")
        print(dict)
        res = json.dumps(dict)
        # print(type(res))
        with open('projectinfo.json', 'w') as outfile:
            outfile.write(res)
        response = HttpResponse(res, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=ProjectInfo.json'
        return response

class ArchiveReplicate(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self,request,file_name,format="json"):
        data = []
        with open('projectinfo.json') as f:
            for line in f:
                data.append(json.loads(line))
        return Response(data, status=status.HTTP_201_CREATED)
