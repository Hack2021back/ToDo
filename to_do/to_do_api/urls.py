# from django.conf import settings
from django.urls import path
# from django.conf.urls.static import static
from to_do_api.views import home, ToDoListDateAPIViews
# from .yasg import urlpatterns as dock_urls
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework.routers import DefaultRouter
# from store_api.views import CategoryViewSet, AuthorViewSet
# from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path("", home),
    path("to_do_list_date/<slug:date>/", ToDoListDateAPIViews.as_view()),


    # path("api/comments/", include("comments.urls")),

    # path("api/auth/token/", obtain_jwt_token),
    # path("api/category/", include(router.urls)),
    # path("api/author/", include(router2.urls)),
    # path("api/schema/", schema_view),
    # path("api/docs/", include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('swagger/', schema_view),

]
