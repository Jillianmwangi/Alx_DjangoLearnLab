from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()

book = Book.objects.get(title="Nineteen Eighty-Four") Traceback (most recent call last): File "", line 1, in File "C:\Users\O AND A.virtualenvs\0x1.Introduction__to__Django-nTZn9Wdl\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method return getattr(self.get_queryset(), name)(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "C:\Users\O AND A.virtualenvs\0x1.Introduction__to__Django-nTZn9Wdl\Lib\site-packages\django\db\models\query.py", line 649, in get raise self.model.DoesNotExist( bookshelf.models.Book.DoesNotExist: Book matching query does not exist.
