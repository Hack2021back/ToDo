# from django.conf import settings
from django.urls import include, path

# from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from to_do_app.views import LoginUser, RegisterUser, LogoutUser

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api", include("to_do_api.urls")),
    # path("api/accounts/", include("accounts.urls")),
    # path("api/comments/", include("comments.urls")),
    path("", include("to_do_app.urls")),
    path("sign_in/", LoginUser.as_view(), name="sign_in"),
    path("register/", RegisterUser.as_view(), name="register"),
    # path("accounts/profile/", ProfileView.as_view(), name="profile"),
    path("logout/<slug:admin_name>", LogoutUser.as_view(), name="logout"),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="reset_password",
    ),
    path(
        "accounts/password_reset_sent/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "accounts/password_change/",
        PasswordChangeView.as_view(
            template_name="registration/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "accounts/password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path('', include('social_django.urls', namespace='social')),
]
