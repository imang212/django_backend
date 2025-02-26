from rest_framework import serializers
from .models import Task

from rest_framework.exceptions import ValidationError
import numpy as np
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

        def Over_nazev(self, value):
            if len(value) > 200:
                raise ValidationError("Title must be 200 characters or fewer.")
            return value

        def Over(self, data):
            # Check that all required fields are provided
            if 'title' not in data or 'description' not in data or 'due_date' not in data:
                raise ValidationError("Missing required fields: 'title', 'description', or 'due_date'.")

            # If a photo is provided, process it
            if 'photo' in data:
                # Open image with OpenCV
                photo = data['photo']
                image = Image.open(photo)
                image = image.convert('L')  # Convert image to grayscale
                image = image.resize((800, 800))  # Resize to 800x800 px

                # Save the image into a new content file
                byte_io = BytesIO()
                image.save(byte_io, format='JPEG')
                byte_io.seek(0)
                data['photo'] = ContentFile(byte_io.read(), name=photo.name)

            return data

