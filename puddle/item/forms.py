from django import forms
from .models import Item

# form design
INPUT_CLASSES = 'w-full py-4 px-6 rounded-lg border border-gray-300 shadow-sm focus:border-teal-500 focus:ring-2 focus:ring-teal-400 transition duration-150 ease-in-out'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES  # Dropdown styling
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES  # Text input styling
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' h-32 resize-none'  # Textarea styling with fixed height and no resizing
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES  # Text input styling
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES  # File input styling
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
