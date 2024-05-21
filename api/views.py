from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser
from drf_spectacular.utils import extend_schema
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.pagination import PageNumberPagination


class EventAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticated, )
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    @extend_schema(
        request=EventSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: EventSerializer(many=True)},
        tags=['Event'],
        methods=['GET'],
        operation_id='Event_get'
    )
    def get(self, request, pk: int = None, *args, **kwargs):
        if pk:
            obj = get_object_or_404(Event, pk=pk)
            serializer = EventSerializer(obj)
            return Response({"Response": serializer.data})
        elif request.GET.get('page') and request.GET.get('limit'):
            paginator = PageNumberPagination()
            queryset = Event.objects.all().order_by('id')
            paginator.page_size = request.GET.get('limit')
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = EventSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = EventSerializer(Event.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=EventSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: EventSerializer(many=True)},
        tags=['Event'],
        methods=['POST'],
        operation_id='Event_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Response": "Event has been created"}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=EventSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: EventSerializer(many=True)},
        tags=['Event'],
        methods=['PUT'],
        operation_id='Event_put'
    )
    def put(self, request, pk, *args, **kwargs):
        try:
            instance = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({'error': 'Object doesn\'t found'})

        serializer = EventSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=EventSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: EventSerializer(many=True)},
        tags=['Event'],
        methods=['DELETE'],
        operation_id='Event_delete'
    )
    def delete(self, request, pk, *args, **kwargs):
        try:
            event = Event.objects.get(pk=pk)
            event.delete()
            evenv = EventSerializer(event)
            return Response({"Event has been deleted": evenv.data}, status=status.HTTP_200_OK, content_type='application/json')
        except:
            return Response({"Error occurred"}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')


class VolunteerAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    @extend_schema(
        request=VolunteerSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: VolunteerSerializer(many=True)},
        tags=['Volunteer'],
        methods=['GET'],
        operation_id='Volunteer_get'
    )
    def get(self, request, pk: int = None):
        if pk:
            obj = get_object_or_404(Volunteer, pk=pk)
            serializer = VolunteerSerializer(obj)
            return Response({'Volunteer': serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        elif request.GET.get('page') and request.GET.get('limit'):
            paginator = PageNumberPagination()
            queryset = Volunteer.objects.all().order_by('id')
            paginator.page_size = request.GET.get('limit')
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = VolunteerSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = VolunteerSerializer(Volunteer.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=VolunteerSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: VolunteerSerializer(many=True)},
        tags=['Volunteer'],
        methods=['POST'],
        operation_id='Volunteer_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Volunteer has been saved": serializer.data}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=VolunteerSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: VolunteerSerializer(many=True)},
        tags=['Volunteer'],
        methods=['PUT'],
        operation_id='Volunteer_put'
    )
    def put(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(Volunteer, pk=pk)
        serializer = VolunteerSerializer(instance=obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Success": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=VolunteerSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: VolunteerSerializer(many=True)},
        tags=['Volunteer'],
        methods=['DELETE'],
        operation_id='Volunteer_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Volunteer, pk=pk)
        serializer = VolunteerSerializer(obj)
        Volunteer.objects.get(pk=pk).delete()
        return Response({"Object is deleted": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')


class InvestorAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    @extend_schema(
        request=InvestorSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: InvestorSerializer(many=True)},
        tags=['Investor'],
        methods=['GET'],
        operation_id='Investor_get'
    )
    def get(self, request, pk: int = None):
        if pk:
            obj = get_object_or_404(Investor, pk=pk)
            serializer = InvestorSerializer(obj)
            return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        elif request.GET.get('offset') and request.GET.get('limit'):
            paginator = PageNumberPagination()
            queryset = Investor.objects.all().order_by('id')
            paginator.page_size = request.GET.get('limit')
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = InvestorSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = InvestorSerializer(Investor.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=InvestorSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: InvestorSerializer(many=True)},
        tags=['Investor'],
        methods=['POST'],
        operation_id='Investor_post'
    )
    def post(self, request):
        serializer = InvestorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Investor has beem saved": serializer.data}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=InvestorSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: InvestorSerializer(many=True)},
        tags=['Investor'],
        methods=['PUT'],
        operation_id='Investor_put'
    )
    def put(self, request, pk):
        obj = get_object_or_404(Investor, pk=pk)
        serializer = InvestorSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Success": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=InvestorSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: InvestorSerializer(many=True)},
        tags=['Investor'],
        methods=['DELETE'],
        operation_id='Investor_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Investor, pk=pk)
        obj.delete()
        return Response(data={"Success": "Object is deleted"}, status=status.HTTP_200_OK, content_type='application/json')


class NewsAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    @extend_schema(
        request=NewsSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: NewsSerializer(many=True)},
        tags=['News'],
        methods=['GET'],
        operation_id='News_get'
    )
    def get(self, request, pk: int = None):
        if pk:
            obj = get_object_or_404(News, pk=pk)
            serializer = NewsSerializer(instance=obj)
            return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        elif request.GET.get('page') and request.GET.get('limit'):
            paginator = PageNumberPagination()
            queryset = News.objects.all().order_by('id')
            paginator.page_size = request.GET.get('limit')
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = NewsSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = NewsSerializer(News.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=NewsSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: NewsSerializer(many=True)},
        tags=['News'],
        methods=['POST'],
        operation_id='News_post'
    )
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"News has been saved": serializer.data}, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=NewsSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: NewsSerializer(many=True)},
        tags=['News'],
        methods=['PUT'],
        operation_id='News_put'
    )
    def put(self, request, pk: int):
        obj = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(instance=obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"News has been updated": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=NewsSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: NewsSerializer(many=True)},
        tags=['News'],
        methods=['DELETE'],
        operation_id='News_delete'
    )
    def delete(self, request, pk: int):
        obj = get_object_or_404(News, pk=pk)
        obj.delete()
        serializer = NewsSerializer(instance=obj, data=request.data)
        return Response({"News has been deleted": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')