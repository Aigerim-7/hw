from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ProductListView(ListView):
    queryset = models.Product.objects.all()
    context_object_name = 'my_products'
    template_name = "products_list.html"

    def get_queryset(self):
        return models.Product.objects.all()


class ProductDetailView(DetailView):
    template_name = "products_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product_id)


class OrderCreateView(CreateView):
    template_name = "add_order.html"
    form_class = forms.OrderForm
    success_url = "/products/"
    queryset = models.Order.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)