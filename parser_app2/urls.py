from django.urls import path
from . import views

app_name = "parse"
urlpatterns = [
    path("parserr/", views.ParserFormView.as_view(),
         name="parse_func"),
]