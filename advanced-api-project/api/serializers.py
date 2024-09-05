from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields of the Book model

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        from datetime import date
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
