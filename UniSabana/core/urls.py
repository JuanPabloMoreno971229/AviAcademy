from django.urls import path
from .views import HomePageView, SingInPageView, SingOutPageView, ChatPageView, TestGeneratorView

urlpatterns = [
    path("", HomePageView.as_view(), name="Home"),
    path("signin/", SingInPageView.as_view(), name="SignIn"),
    path("signout/", SingOutPageView.as_view(), name="SingOut"),
    path("chat-avi/", ChatPageView.as_view(), name="ChatAvi"),
    path("test-generator/", TestGeneratorView.as_view(), name="TestGenerator"),
]
