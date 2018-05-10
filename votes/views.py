from django.shortcuts import render

from .models import Vote
from .serializers import VoteSerializer

from rest_framework import generics

from rest_framework.renderers import (BrowsableAPIRenderer,
 JSONRenderer, TemplateHTMLRenderer,)

class VoteList(generics.ListCreateAPIView):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,BrowsableAPIRenderer)
    template_name = "vote_list.html"
    queryset = Vote.objects.all()#this is the total set of object the query can work on DEFAULT_PAGINATION_CLASS' in settings.py  controls the content on a page
    serializer_class = VoteSerializer
# Create your views here.

class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,BrowsableAPIRenderer)
    template_name = "vote.html"
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

