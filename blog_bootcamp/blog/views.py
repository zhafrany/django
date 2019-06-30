from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, News
from .serializers import CategorySerializers, NewsSerializers

@api_view(["GET"])
def hello_world(request):
    return Response({"message":"hello world"})

@api_view(["GET"])
def categories(request):
    queryset = Category.objects.all()
    serialized = CategorySerializers(queryset, many=True)
    return Response(serialized.data)

@api_view(["GET"])
def news(request):
    queryset = News.objects.all()
    serialized = NewsSerializers(queryset, many=True)
    return Response(serialized.data)

