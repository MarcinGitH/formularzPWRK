from django import forms
from .models import Entry, ProducerSupplier
import os
from django.db.models.fields import BLANK_CHOICE_DASH
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

reason_choices = [
    ('Nowe narzędzie - nowe uruchomienie', 'Nowe narzędzie - nowe uruchomienie'),
    ('Nowe narzędzie - optymalizacja', "Nowe narzędzie - optymalizacja"),
    ('Brak pwrk / Inwentaryzacja', "Brak pwrk / Inwentaryzacja")
]

status_choices = [
    ('NOWY', 'NOWY'),
    ('W TRAKCIE', "W TRAKCIE"),
    ('DO WYJAŚNIENIA', "DO WYJAŚNIENIA"),
    ('ZAKOŃCZONY', "ZAKOŃCZONY")
]


type_of_employee_choices = [
    ("Pracownik_wypożyczalni", "Pracownik wypożyczalni"),
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
            "description_1": forms.TextInput(attrs={'class': 'text-input text-input-description_1', 'id': 'text-input-description_1', 'oninput': 'let p=this.selectionStart;this.value=this.value.toUpperCase();this.setSelectionRange(p, p);'}),
            "PWRK": forms.TextInput(attrs={'class': 'text-input', 'id': 'text-input-PWRK', 'oninput': 'let p=this.selectionStart;this.value=this.value.toUpperCase();this.setSelectionRange(p, p);'}),
            "reason": forms.Select(choices=BLANK_CHOICE_DASH+reason_choices, attrs={'class': 'combobox reason', 'id': 'reason'}),
            "status": forms.Select(choices=status_choices, attrs={'class': 'combobox status', 'id': 'status'}),
            'type_of_employee': forms.RadioSelect(choices=type_of_employee_choices, attrs={'class': 'radio-select type-of-employee', 'id': 'type-of-employee'}),
            'type_of_tool': forms.RadioSelect(choices=type_of_tool_choices, attrs={'class': 'radio-select type-of-tool', 'id': 'type-of-tool'}),
            'producer': forms.Select(attrs={'class': 'combobox producer', 'id': 'producer'}),
            'supplier': forms.Select(attrs={'class': 'combobox supplier', 'id': 'supplier'}),
            "drawings_2d": forms.FileInput(),
            "drawings_3d": forms.FileInput(),
            "screen_catalog": forms.FileInput(),
        }
        labels = {
            "description_1": "Cecha narzędzia",
            "type_of_employee": "Osoba zgłaszająca",
            "type_of_tool": "Rodzaj narzędzia",
            "reason": "Powód zgłoszenia",
            "status": "Status",
            "producer": "Producent",
            "supplier": "Dostawca",
            "drawings_2d": "Rysunek 2D",
            "drawings_3d": "Rysunek 3D",
            "comments": "Uwagi / Link do katalogu",
            "screen_catalog": "Screen z katalogu"
        }

        error_messages = {
            'PWRK': {
                'PWRK': 'Błędny numer PWRK'
            }
        }

    def __init__(self, *args, **kwargs):
        self.form_type = kwargs.pop('form_type', None)
        super().__init__(*args, **kwargs)

    def _clean_fields(self):
        if self.form_type == "new_entry_form" and self.data.get('type_of_employee', None) == "Technolog":
            self.fields['type_of_tool'].required = True

        super(EntryForm, self)._clean_fields()

    def clean(self):
        cleaned_data = super().clean()
        pwrk = cleaned_data.get("PWRK")
        pwrk_ok = False
        if len(pwrk) == 10:
            if pwrk[:4] == "PWRK":
                if pwrk[4:].isdigit():
                    pwrk_ok = True
        if pwrk == "":
            pwrk_ok = True

        if not pwrk_ok:
            msg = "Bledny numer PWRK"
            self.add_error("PWRK", msg)

        return cleaned_data


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"]
