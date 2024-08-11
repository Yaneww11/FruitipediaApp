from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from FruitipediaApp.fruits.forms import CategoryAddForm, FruitCreateForm, FruitEditForm, FruitDeleteForm
from FruitipediaApp.fruits.models import Fruit


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits,
    }

    return render(request, 'common/dashboard.html', context)


class CreateFruitView(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


def edit_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form,
    }

    return render(request, 'fruits/edit-fruit.html', context)


def details_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    context = {
        'fruit': fruit,
    }

    return render(request, 'fruits/details-fruit.html', context)


class DeleteFruitView(DeleteView):
    model = Fruit
    form_class = FruitDeleteForm
    success_url = reverse_lazy('dashboard')
    template_name = 'fruits/delete-fruit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, object=self.object))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


def create_category(request):
    if request.method == 'GET':
        form = CategoryAddForm()
    else:
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'categories/create-category.html', context)
