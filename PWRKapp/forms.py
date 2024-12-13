from django import forms
from .models import Entry
import os

reason_choices = [
    ('choice1', 'Nowe narzędzie - nowe uruchomienie'),
    ('choice2', "Nowe narzędzie - optymalizacja"),
    ('choice3', "Brak pwrk / Inwentaryzacja")
]

type_of_employee_choices = [
    ("choice1", "Pracownik wypożyczalni"),
    ("choice2", "Technolog"),
]

type_of_tool_choices = [
    ("choice1", "Katalog"),
    ("choice2", "Specjał"),
]


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ("entry_employee",)
        widgets = {
            "reason": forms.Select(choices=reason_choices, attrs={'class': 'combobox reason'}),
            'type_of_employee': forms.RadioSelect(choices=type_of_employee_choices, attrs={'class': 'radio-select type-of-employee'}),
            'type_of_tool': forms.RadioSelect(choices=type_of_tool_choices, attrs={'class': 'radio-select type-of-tool'}),
            "producer": forms.Select(choices=reason_choices, attrs={'class': 'combobox producer'}),
            "supplier": forms.Select(choices=reason_choices, attrs={'class': 'combobox supplier'}),
            # "drawings_2d": forms.FileInput(attrs={'allow_multiple_selected': True, 'class': 'combobox drawing-2d'}),
        }
