from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser, MultiPartParser


class EventAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    def get(self, request, slug: str = None, *args, **kwargs):
        if slug:
            obj = get_object_or_404(Event, slug=slug)
            serializer = EventSerializer(obj)
            return Response({"Response": serializer.data})
        serializer = EventSerializer(Event.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Response": "Event has been created"}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def put(self, request, slug, *args, **kwargs):
        try:
            instance = Event.objects.get(slug=slug)
        except Event.DoesNotExist:
            return Response({'error': 'Object doesn\'t found'})

        serializer = EventSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, *args, **kwargs):
        try:
            event = Event.objects.get(slug=slug)
            event.delete()
            evenv = EventSerializer(event)
            return Response({"Event has been deleted": evenv.data}, status=status.HTTP_200_OK, content_type='application/json')
        except:
            return Response({"Error occurred"}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')


class VolunteerAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    def get(self, request, slug: str = None):
        if slug:
            obj = get_object_or_404(Volunteer, slug=slug)
            serializer = VolunteerSerializer(obj)
            return Response({'Volunteer': serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        serializer = VolunteerSerializer(Volunteer.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request, *args, **kwargs):
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Volunteer has been saved": serializer.data}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def put(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(Volunteer, slug=slug)
        serializer = VolunteerSerializer(instance=obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Success": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def delete(self, request, slug):
        obj = get_object_or_404(Volunteer, slug=slug)
        serializer = VolunteerSerializer(obj)
        Volunteer.objects.get(slug=slug).delete()
        return Response({"Object is deleted": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')


class InvestorAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    def get(self, request, slug: str = None):
        if slug:
            obj = get_object_or_404(Investor, slug=slug)
            serializer = InvestorSerializer(obj)
            return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        serializer = InvestorSerializer(Investor.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request):
        serializer = InvestorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Investor has beem saved": serializer.data}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def put(self, request, slug):
        obj = get_object_or_404(Investor, slug=slug)
        serializer = InvestorSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Success": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    def delete(self, request, slug):
        obj = get_object_or_404(Investor, slug=slug)
        obj.delete()
        return Response(data={"Success": "Object is deleted"}, status=status.HTTP_200_OK, content_type='application/json')


class NewsAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    def get(self, request, slug: str = None):
        if slug:
            obj = get_object_or_404(News, slug=slug)
            serializer = NewsSerializer(instance=obj)
            # r = request.build_absolute_url(serializer.data.get('image'))
            print(serializer.data)
            return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='multipart/form-data')
        serializer = NewsSerializer(News.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"News has been saved": serializer.data}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def put(self, request, slug: str):
        obj = get_object_or_404(News, slug=slug)
        serializer = NewsSerializer(instance=obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"News has been updated": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def delete(self, request, slug: str):
        obj = get_object_or_404(News, slug=slug)
        obj.delete()
        serializer = NewsSerializer(instance=obj, data=request.data)
        return Response({"News has been deleted": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')