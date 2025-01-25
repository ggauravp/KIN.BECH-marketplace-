from django.shortcuts import render, get_object_or_404,redirect, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


@login_required  # Ensures only logged-in users can access this view
def new(request):
    if request.method == 'POST':  # Checks if the form is submitted via POST
        form = NewItemForm(request.POST, request.FILES)  # Initializes the form with POST data and any uploaded files

        if form.is_valid():  # Validates the form data
            item = form.save(commit=False)  # Creates an item instance without saving it to the database yet
            item.added_by = request.user  # Sets the added_by field to the current user
            item.save()  # Saves the item to the database

            return redirect('item:detail', pk=item.id)  # Redirects to the item detail page after saving
    else:
        form = NewItemForm()  # If not POST, initializes an empty form for a new item

    return render(request, 'item/form.html', {  # Renders the form template with context
        'form': form,  # Passes the form (either empty or with submitted data) to the template
        'title': 'New item',  # Sets a title for the form page
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, added_by=request.user )
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, added_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

