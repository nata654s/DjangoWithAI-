from rest_framework import serializers
from ..models import Digits
import base64
import uuid
from django.core.files.base import ContentFile


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        print('data', data)
        _format, _str_img = data.split(';base64')
        print('format', _format)
        print('str_img', str_img)
        print('type str_image', type(str_img))
        decode_file = base64.b64decode(str_img)
        print('decoded file', decode_file)
        print('type decoded_file', decode_file)
        fname = f"{str(uuid.uuid4())[:10]}.png"
        print('fname', fname)
        data = ContentFile(decode_file, name=fname)
        return super().to_internal_value(data)

class DigitSerializers(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Digits
        fields = ('id', 'image', 'result')