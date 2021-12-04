from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from to_do_app.models import ToDoList
from .serializers import ToDoListAllSerialzer


def home(request):
    return HttpResponse("hello world")


class ToDoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """
    order_fields = ["priority", "start_data"]

    queryset = ToDoList.objects.order_by(*order_fields)

    def list(self, request):
        queryset = ToDoList.objects.order_by("priority", "start_data")
        serializer = ToDoListAllSerialzer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ToDoList.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ToDoListAllSerialzer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = ToDoListAllSerialzer(data=request.data)

        if serializer.is_valid():
            ToDoList.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(
            {"status": "Bad Request", "message": serializer.is_valid()},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None):
        serializer = ToDoListAllSerialzer(data=request.data)
        if serializer.is_valid():
            ToDoList(pk=pk, **serializer.validated_data).save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(
            {"status": "Bad Request", "message": serializer.is_valid()},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, pk=None):
        try:
            ToDoList.objects.get(pk=pk).delete()
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(
                {"status": "Bad Request"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ToDoListDateAPIViews(APIView):

    filter_backends = [OrderingFilter]
    order_fields = ["priority", "end_data"]

    def get(self, request, date):
        queryset = ToDoList.objects.filter(end_data=date)
        serializer = ToDoListAllSerialzer(queryset, many=True)
        return Response(serializer.data)


class ToDoListTodayAPIViews(APIView):

    filter_backends = [OrderingFilter]
    order_fields = ["priority", "end_data"]

    def get(self, request):
        print(datetime.now().strftime("%Y/%m/%d"))
        queryset = ToDoList.objects.filter(end_data=datetime.now().strftime("%Y/%m/%d"))
        serializer = ToDoListAllSerialzer(queryset, many=True)
        return Response(serializer.data)
