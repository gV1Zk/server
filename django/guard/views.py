from rest_framework import generics, status
from rest_framework.response import Response

from .models import ButtonClick
from .serializers import ButtonClickCreateSerializer
import base64
import json


class ButtonClickCreateView(generics.CreateAPIView):
    queryset = ButtonClick.objects.all()
    serializer_class = ButtonClickCreateSerializer

    def create(self, request, *args, **kwargs):
        data = request.data['data']
        data = base64.b64decode(data)
        data = json.loads(data)
        data = {
            'button': data['deviceName'],
            'type': data['telemetry']['firstButton']['status'],
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)