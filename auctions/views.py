from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Bid
from .serializers import UserSerializer, BidSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BidViewSet(viewsets.ModelViewSet):
    """
    API endpoint for bids.
    TODO: Receive POST from braintree form and:
        1. braintree.Transaction.sale()
        2. Create bid object
    """
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def pre_save(self, obj):
        obj.user = self.request.user
