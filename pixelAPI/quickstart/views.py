from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pixelAPI.quickstart.serializers import UserSerializer, GroupSerializer


# from django.shortcuts import render

# views are where we set up api endpoints.

"""
FTA:
Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.

We can easily break these down into individual views if we need to, but using viewsets keeps the view logic nicely organized as well as being very concise.
"""

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]