from django import forms
from .models import Entry, ProducerSupplier
import os

reason_choices = [
    ('Nowe narzędzie - nowe uruchomienie', 'Nowe narzędzie - nowe uruchomienie'),
    ('Nowe narzędzie - optymalizacja', "Nowe narzędzie - optymalizacja"),
    ('Brak pwrk / Inwentaryzacja', "Brak pwrk / Inwentaryzacja")
]

type_of_employee_choices = [
    ("Pracownik wypożyczalni", "Pracownik wypożyczalni"),
    ("Technolog", "Technolog"),
]

type_of_tool_choices = [
    ("Katalog", "Katalog"),
    ("Specjał", "Specjał"),
]


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        exclude = ("entry_employee",)
        widgets = {
            "description_1": forms.TextInput(attrs={'class': 'text-input text-input-description_1'}),
            "reason": forms.Select(choices=reason_choices, attrs={'class': 'combobox reason'}),
            'type_of_employee': forms.RadioSelect(choices=type_of_employee_choices, attrs={'class': 'radio-select type-of-employee'}),
            'type_of_tool': forms.RadioSelect(choices=type_of_tool_choices, attrs={'class': 'radio-select type-of-tool'}),
            'producer': forms.Select(attrs={'class': 'combobox producer'}),
            'supplier': forms.Select(attrs={'class': 'combobox supplier'}),
            "drawings_2d": forms.FileInput(attrs={'accept': '.zip,application/pdf'}),
            "drawings_3d": forms.FileInput(),
            "screen_catalog": forms.FileInput(),
        }
        labels = {
            "description_1": "Cecha narzędzia*",
            "type_of_employee": "Osoba zgłaszająca*",
            "type_of_tool": "Rodzaj narzędzia*",
            "reason": "Powód zgłoszenia*",
            "producer": "Producent*",
            "supplier": "Dostawca*",
            "drawings_2d": "Rysunek 2D",
            "drawings_3d": "Rysunek 3D",
            "comments": "Uwagi / Link do katalogu",
            "screen_catalog": "Screen z katalogu"
        }

    def _clean_fields(self):
        if self.data.get('type_of_employee', None) == "Technolog":
            self.fields['type_of_tool'].required = True
        super(EntryForm, self)._clean_fields()
