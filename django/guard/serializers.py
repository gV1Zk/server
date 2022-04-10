from rest_framework import serializers
from asgiref.sync import async_to_sync

from config.socketio import sio
from .models import Button, ButtonClick


class ButtonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = ('mts_id', 'geolocation')


class ButtonClickCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        data = ButtonClickViewSerializer(instance).data
        async_to_sync(sio.emit)('click', data, room='flash')
        return instance

    class Meta:
        model = ButtonClick
        fields = ('id', 'button', 'type', 'created_at')
        read_only_fields = ('created_at', )


class ButtonClickViewSerializer(serializers.ModelSerializer):

    button = ButtonViewSerializer()

    class Meta:
        model = ButtonClick
        fields = ('id', 'button', 'type', 'created_at')
