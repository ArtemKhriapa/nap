from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from ..models import Data as Data_model
from .serializers import DataSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CustomPagePagination(PageNumberPagination):
    #class for set pagination parameters
    page_size = 10 #obj in page
    page_size_query_param = 'page_size'
    max_page_size = 10

@method_decorator(login_required, name='dispatch')
class DataView(generics.ListAPIView):
    # queryset = Data_model.objects.all().order_by('id') # sorted by id
    serializer_class = DataSerializer
    pagination_class = CustomPagePagination

    def get_queryset(self, *args, **kwargs):
        return Data_model.objects.all().filter(user=self.request.user).order_by('id')

