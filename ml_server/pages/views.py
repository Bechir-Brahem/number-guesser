from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import pages.classes.MlModelFactory as MlFactory


@csrf_exempt
def process(request):
    try:
        model = MlFactory.getModel(request.POST.get('model'))
    except ValueError:
        return HttpResponse('invalid model', status=400)
    try:
        digit = [int(sq) for sq in request.POST.get('digit')]
    except ValueError:
        return HttpResponse('invalid number', status=400)

    if len(digit) != 784:
        return HttpResponse('invalid number', status=400)

    return HttpResponse(int(model.predict(digit)))


@csrf_exempt
def listModels(request):
    model_names = MlFactory.getModelNames()
    return JsonResponse(model_names)

# Create your views here.
