from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer



# --> return multiple queryset objects in json format
#def api_home(request, *args, **kwargs):
    #model_data = Product.objects.all()
    #data = {}
    #if model_data:
        #data = [model_to_dict(obj, fields =['title', 'price']) for obj in model_data]
    #return JsonResponse(data, safe=False)


# --> return only one model at a time in json format
@api_view(["POST"])
def api_home(request, *args, **kwargs):

    # DRF API VIEW

    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
        # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    # return Response(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})

   serializer = ProductSerializer(data=request.data)
   if serializer.is_valid():
      # instance = serializer.save(commit=False)
      print(serializer.data)
      return Response(serializer.data)
   return Response({"invalid": "not a good data"}, status = 400)