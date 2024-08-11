from django import forms

from FruitipediaApp.fruits.models import Category, Fruit


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Category name'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class CategoryAddForm(CategoryBaseForm):
    pass


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit name'}),
            'description': forms.TextInput(attrs={'placeholder': 'Fruit description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit image URL'}),
            'nutrition': forms.NumberInput(attrs={'placeholder': 'Nutrition information'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
