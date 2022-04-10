from rest_framework import serializers
from asgiref.sync import async_to_sync

from config.socketio import sio
from .models import Button, ButtonClick


class ButtonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = '__all__'


class ButtonClickCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        data = ButtonClickViewSerializer(instance).data
        async_to_sync(sio.emit)('click', data, room='flash')
        return instance

    class Meta:
        model = ButtonClick
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ButtonClickViewSerializer(serializers.ModelSerializer):

    button = ButtonViewSerializer()

    class Meta:
        model = ButtonClick
        fields = '__all__'
