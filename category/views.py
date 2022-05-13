from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from .models import *

class SubcategoryList(APIView):
      permission_classes=[IsAuthenticated,]
      def post(self, request,format=None):
          category=request.data['category']
          subcategory={}
          if category:
             subcategories=Category.objects.get(id=category).subcategorys.all()
             subcategory={p.name:p.id for p in subcategories}
             return JsonResponse(data=subcategory,safe=False)
             
class SubcategoryChildList(APIView):
     permission_classes=[IsAuthenticated,]
     def post(self, request, format=None):
         subcategory=request.data['subcategory']
         subcategory_child={}
         if subcategory:
            subcategory_childs=Subcategory.objects.get(id=subcategory).SubcategoryChild.all()
            subcategory_child={p.name:p.id for p in subcategory_childs}
            return JsonResponse(data=subcategory_child,safe=False)