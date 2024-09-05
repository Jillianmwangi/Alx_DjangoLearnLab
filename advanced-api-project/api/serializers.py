from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    # The BookSerializer is used to serialize and validate data related to the Book model.
    # It serializes all fields of the Book model and includes custom validation
    # to ensure that the publication year is not in the future.

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        # This method checks if the publication year is greater than the current year.
        # If it is, a ValidationError is raised to prevent future publication dates.
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    # The AuthorSerializer is used to serialize data related to the Author model.
    # It includes the author's name and a nested BookSerializer to serialize related books dynamically.
    # The books are serialized as a list of BookSerializer objects, thanks to the 'many=True' argument.

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
