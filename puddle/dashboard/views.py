from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(added_by=request.user)

    return render(request, 'dashboard/index.html', {   #dashboard here refers to appname not folder name
        'items': items,
    })