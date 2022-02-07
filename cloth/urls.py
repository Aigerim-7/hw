from django.urls import path
from . import views

app_name = "clothes"
urlpatterns = [
    path("tag_1/", views.ClothesListView1.as_view(), name="my_clothes"),
    path("tag_2/", views.ClothesListView2.as_view(), name="my_clothes"),
    path("tag_3/", views.ClothesListView3.as_view(), name="my_clothes"),
    path("tag_4/", views.ClothesListView4.as_view(), name="my_clothes"),
    path("add-order1/", views.OrderCreateView1.as_view(), name="order_create"),
    path(
        "clothes/<int:id>/", views.ClothesDetailView1.as_view(),name="clothes_detail"),
]