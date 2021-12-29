from django.urls import path, include
from rest_framework import routers
from book.views import AuthorViewSet, BookViewSet

api_router = routers.DefaultRouter()


api_router.register(r'authors', AuthorViewSet)
api_router.register(r'books', BookViewSet)

urlpatterns = [

    path('', include(api_router.urls)),

]
