from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EntryForm
from django.contrib import messages
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
        # if entry.cleaned_data("type_of_employee") == "Technolog":
        #     entry

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
        context = {
            "nav_button_active": 2
        }
        return render(request, "PWRKapp/new_entry.html", context)


class EntryHandlingView(View):
    def get(self, request):
        context = {
            "nav_button_active": 3
        }
        return render(request, "PWRKapp/new_entry.html", context)
