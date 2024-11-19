from django.shortcuts import render
from .models import PetsTypes, Breeds, PetsOwners, Pets
from django.http import HttpResponse
from django import forms
from .forms import PetsFilter

# Create your views here.

def pets_types(request):
    template_name = 'pets_list/pets_types.html'
    if request.method == 'GET':
        tmp = PetsTypes.objects.all().order_by('name') #Сортировка по имени
        items = [str(item) for item in tmp] #получили строковое представление объекта
    context = {'title': 'Типы животных','data': items}
    #return HttpResponse(','.join(items))
    return render(request, template_name, context)

def breeds(request):
    template_name = 'pets_list/breeds.html'
    if request.method == 'GET':
        tmp = Breeds.objects.all().order_by('name') 
        items = [item for item in tmp]
    context = {'title': 'Породы','data': items}
    return render(request, template_name, context)

def pets_owners(request):
    template_name = 'pets_list/pets_owners.html'
    if request.method == 'GET':
        tmp = PetsOwners.objects.all().order_by('name') 
        items = [str(item) for item in tmp]
    context = {'title': 'Хозяева','data': items}
    return render(request, template_name, context)
    

def pets(request, pk =None):
    template_name = 'pets_list/pets.html'
    form = PetsFilter(request.GET or None)
    context = {'form': form}
    if request.method == 'GET':
        if form.is_valid() and (form.cleaned_data['pet_name'] != '' or 
                                form.cleaned_data['owner_name'] != '' or
                                form.cleaned_data['birthday'] is not None):
            tmp = Pets.objects
            if form.cleaned_data['pet_name']:
                tmp = tmp.filter(name__icontains = form.cleaned_data['pet_name'])
                #items = list(tmp)
            if form.cleaned_data['birthday']:
                tmp = tmp.filter(year_of_birth = form.cleaned_data['birthday'])
                #items = list(tmp)
            if form.cleaned_data['owner_name']:
                tmp = tmp.filter(owner__name__icontains = form.cleaned_data['owner_name'])
            items = list(tmp)
        elif pk == None:  
            tmp = Pets.objects.all().order_by('name')
            items = list(tmp)
        else:
            tmp = Pets.objects.get(id=pk)
            items = [tmp]
            
    context.update({'title': 'Питомцы','data': items})
    return render(request, template_name, context)  