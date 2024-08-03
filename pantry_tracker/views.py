from django.shortcuts import render, redirect
from pantry.models import Pantry
from django.http import HttpResponse


def pantry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = request.POST.get('count')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Pantry.objects.create(
            inventory_name=name,
            inventory_count=count,
            inventory_description=description,
            inventory_image=image
        )
        return redirect('/')

    queryset = Pantry.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = Pantry.objects.filter(inventory_name__icontains=search)

    context = {
            'queryset': queryset
    }

    return render(request, 'index.html', context)


def delete_pantry(request, id):
    item = Pantry.objects.get(id=id)

    item.delete()
    return redirect('/')


def update_pantry(request, id):
    queryset = Pantry.objects.get(id=id)

    prev_name = queryset.inventory_name
    prev_count = queryset.inventory_count
    prev_desc = queryset.inventory_description

    if request.method == 'POST':
        name = request.POST.get('name')
        count = request.POST.get('count')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        queryset.inventory_name = name
        queryset.inventory_count = count
        queryset.inventory_description = description

        if image:
            queryset.inventory_image = image

        queryset.save()
        return redirect('/')

    context = {
        'queryset': queryset,
        'prev_name': prev_name,
        'prev_count': prev_count,
        'prev_desc': prev_desc

    }

    return render(request, 'update_pantry.html', context)


