from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, FileResponse, HttpResponseNotFound
from django.urls import reverse
from .forms import EntryForm
from .models import Entry
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.dateparse import parse_date
import os
from django.conf import settings
from django.db.models import Q
# Create your views here.


class StartingPageView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse("new-entry"))


class NewEntryView(View):
    def get(self, request):
        # welcome_user = request.META.get('REMOTE_USER')
        test_list = []
        for i in range(1, 30000):
            test_list.append(i)

        entry = EntryForm()
        employee_type = request.session.get("employee_type")
        if employee_type is not None:
            entry.fields["type_of_employee"].initial = request.session["employee_type"]
            if entry.fields["type_of_employee"].initial == "Technolog":
                entry.fields["type_of_tool"].required = True

        context = {
            "nav_button_active": 1,
            "comp_list": test_list,
            "entry_form": entry
        }
        return render(request, "PWRKapp/new_entry.html", context)

    def post(self, request):
        test_list = []
        for i in range(1, 30000):
            test_list.append(i)

        entry = EntryForm(request.POST, request.FILES)

        if entry.is_valid():
            entry.save()

            # new_entry.fields['type_of_employee'].initial = entry.cleaned_data["type_of_employee"]

            messages.success(request, "Zgłoszenie zostało wysłane")
            request.session["employee_type"] = entry.cleaned_data["type_of_employee"]

            return HttpResponseRedirect(reverse("new-entry"))

        context = {
            "nav_button_active": 1,
            "comp_list": test_list,
            "entry_form": entry,
            "valid_ok": False
        }
        return render(request, "PWRKapp/new_entry.html", context)


class AllEntriesView(View):
    def get(self, request):
        # Pobieranie wartości z formularza (jeśli istnieją)
        name_filter = request.GET.get('name', '')
        created_after = request.GET.get('created_after', '')

        # Filtrujemy dane
        items = Entry.objects.all().order_by("-pk")

        if name_filter:
            items = items.filter(description_1__icontains=name_filter)

        if created_after:
            items = items.filter(entry_date__gte=created_after)

        # Pagowanie
        paginator = Paginator(items, 30)  # 30 elementów na stronę
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'PWRKapp/all_entries.html', {
            "nav_button_active": 2,
            'page_obj': page_obj,
            'name_filter': name_filter,
            'created_after': created_after,
        })


class EntryHandlingView(View):
    def get(self, request):
        context = {
            "nav_button_active": 3
        }
        return render(request, "PWRKapp/new_entry.html", context)


def download(request, catalog, file_name):
    db_file_path = catalog + "/" + file_name
    file = os.path.join(settings.BASE_DIR, "uploads/" + db_file_path)
    if os.path.isfile(file):
        fileOpened = open(file, "rb")
        return FileResponse(fileOpened)
    else:
        file_records = Entry.objects.filter(Q(drawings_2d=db_file_path) | Q(
            drawings_3d=db_file_path) | Q(screen_catalog=db_file_path))
        for file_rec in file_records:
            if catalog == "drawings_2d":
                file_rec.drawings_2d = None
                file_rec.save()
            elif catalog == "drawings_3d":
                file_rec.drawings_3d = None
                file_rec.save()
            elif catalog == "screen_catalog":
                file_rec.screen_catalog = None
                file_rec.save()
