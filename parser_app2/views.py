from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import FormView

from . import forms


class ParserFormView(FormView):
    template_name = "parser.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponse('Parser Success')
            # return redirect(reverse("parse:list_objects"))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
