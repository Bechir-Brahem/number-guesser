import os

import joblib
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


def process(request):
    model = joblib.load(os.path.join(settings.BASE_DIR, 'pages/my_model2.pkl'))
    digit = [int(sq) for sq in request.POST.get('digit')]
    return HttpResponse(model.predict([digit])[0])

# Create your views here.
