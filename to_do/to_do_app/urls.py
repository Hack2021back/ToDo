# from django.conf import settings
from django.urls import path
# from django.conf.urls.static import static
from to_do_app.views import RegisterUser, today, inbox

# from .yasg import urlpatterns as dock_urls
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework.routers import DefaultRouter
# from store_api.views import CategoryViewSet, AuthorViewSet
# from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path("", RegisterUser.as_view(), name="register"),
    path("today", today, name="today"),
    path("inbox", inbox, name="inbox")
]
