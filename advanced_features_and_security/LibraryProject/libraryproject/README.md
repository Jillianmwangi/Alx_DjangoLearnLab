# Permissions and Groups Setup

This Django application uses custom permissions and groups to control access to certain parts of the application.

## Custom Permissions

The `Book` model includes the following custom permissions:
- `can_view`: Allows viewing book details.
- `can_create`: Allows creating new book entries.
- `can_edit`: Allows editing book entries.
- `can_delete`: Allows deleting book entries.

## Groups

The following groups have been set up with corresponding permissions:
- **Editors**: Can create and edit books.
- **Viewers**: Can view books.
- **Admins**: Full access to create, view, edit, and delete books.

## Enforcing Permissions

Permissions are enforced in views using Django's `@permission_required` decorator.
