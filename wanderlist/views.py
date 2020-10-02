from wanderlist.models import *
from wanderlist.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
from django.http import HttpResponse, JsonResponse


def index(request):
    #return HttpResponse('Refer to onedrive Routes document for details on routes')
    template = loader.get_template('wanderlist/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

class BusinessList(APIView):
    def get(self, request, format=None):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class BusinessDetail(APIView):
    def get_object(self, id):
        try:
            return Business.objects.get(id=id)
        except Business.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        business = self.get_object(id)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        business = self.get_object(id)
        serializer = BusinessSerializer(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        business = self.get_object(id)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_business(self, request, id, format=None):
        business = list(Business.objects.filter(id=id).values('id', 'name'))
        return Response(business, status=status.HTTP_200_OK)

class ActivityList(APIView):
    def get(self, request, format=None):
        activity = Activity.objects.all()
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)