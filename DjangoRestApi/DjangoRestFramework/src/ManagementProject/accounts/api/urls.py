from django.urls import path
from accounts.api.views import(
        CustomObtainAuthToken,
        Logout,
        registration_view,
        api_get_auth_user_view,

)

app_name="accounts"

urlpatterns = [
      path('register',registration_view,name="register"),
      path('login', CustomObtainAuthToken.as_view(), name="login"),
      path('auth', api_get_auth_user_view, name="get_auth"),
      path('logout', Logout.as_view(), name="logout"),





]