from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ClothesListView1(ListView):
    queryset = models.ClothesCL.objects.filter(
        tags__name="clothes").order_by("-id")
    context_object_name = 'my_clothes'
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.ClothesCL.objects.filter(
            tags__name="clothes").order_by("-id")

class ClothesListView2(ListView):
    queryset = models.ClothesCL.objects.filter(
        tags__name="sweatshirts").order_by("-id")
    context_object_name = 'my_clothes'
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.ClothesCL.objects.filter(
            tags__name="sweatshirts").order_by("-id")

class ClothesListView3(ListView):
    queryset = models.ClothesCL.objects.filter(
        tags__name="shoes").order_by("-id")
    context_object_name = 'my_clothes'
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.ClothesCL.objects.filter(
            tags__name="shoes").order_by("-id")



class ClothesListView4(ListView):
    queryset = models.ClothesCL.objects.filter(
        tags__name="headdress").order_by("-id")
    context_object_name = 'my_clothes'
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.ClothesCL.objects.filter(
            tags__name="headdress").order_by("-id")


class ClothesListView(ListView):
    context_object_name = 'my_clothes'
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.ClothesCL.objects.all()





class ClothesDetailView1(DetailView):
    template_name = "clothes_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.ClothesCL, id=product_id)


class OrderCreateView1(CreateView):
    template_name = "add_order1.html"
    form_class = forms.OrderForm
    success_url = "/clothes/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView1, self).form_valid(form=form)