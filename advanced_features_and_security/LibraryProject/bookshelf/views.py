from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # Assuming you have a form for creating/editing books

@permission_required('books.can_view', raise_exception=True)
def view_book(request, book_id):
    """
    View details of a specific book.
    Requires 'books.can_view' permission.
    """
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    """
    Create a new book.
    Requires 'books.can_create' permission.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect after successful creation
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, book_id):
    """
    Edit an existing book.
    Requires 'books.can_edit' permission.
    """
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect after successful update
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

@permission_required('books.can_delete', raise_exception=True)
def delete_book(request, book_id):
    """
    Delete an existing book.
    Requires 'books.can_delete' permission.
    """
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect after successful deletion
    return render(request, 'delete_book.html', {'book': book})
