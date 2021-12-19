from django.http import HttpResponse
from django.views.generic import TemplateView

import pages.classes.MlModelFactory as MlFactory


class HomePageView(TemplateView):
    template_name = 'home.html'


def process(request):
    try:
        model = MlFactory.getModel(request.POST.get('model'))
    except ValueError:
        return HttpResponse('invalid model')
    digit = [int(sq) for sq in request.POST.get('digit')]
    return HttpResponse(model.predict([digit])[0])

# Create your views here.
