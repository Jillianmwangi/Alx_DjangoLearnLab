
# Django Custom User Model with Permissions and Groups

## Overview
This project demonstrates how to create a custom user model in Django, add custom fields, and implement permissions and groups to control access within the application.

## Custom User Model
The custom user model `CustomUser` extends Django's `AbstractUser`. Two additional fields have been added:
- `date_of_birth`: A `DateField` to store the user's date of birth.
- `profile_photo`: An `ImageField` to store the user's profile photo.

### Location
- **Model**: `bookshelf/models.py`
- **Admin Configuration**: `bookshelf/admin.py`

## Permissions Setup
Custom permissions have been defined for the `CustomUser` model:

- `can_edit`: Permission to edit user details.
- `can_create`: Permission to create new users.

These permissions are used throughout the application to control user access to various functionalities.

### Location
- **Permissions Definition**: `bookshelf/models.py` within the `Meta` class of `CustomUser`.

### Usage in Views
To enforce these permissions in views, the following decorators can be used:
```python
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request, user_id):
    # Logic to edit user
    pass

@permission_required('bookshelf.can_create', raise_exception=True)
def create_user(request):
    # Logic to create a new user
    pass

