from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict

from products.models import Product



# --> return multiple queryset objects in json format
#def api_home(request, *args, **kwargs):
    #model_data = Product.objects.all()
    #data = {}
    #if model_data:
        #data = [model_to_dict(obj, fields =['title', 'price']) for obj in model_data]
    #return JsonResponse(data, safe=False)


# --> return only one model at a time in json format
def api_home(reqeust, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})