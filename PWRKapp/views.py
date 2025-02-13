from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, FileResponse, Http404, HttpResponse
from django.urls import reverse
from .forms import EntryForm, CreateUserForm
from .models import Entry, Employee
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.dateparse import parse_date
import os
from django.conf import settings
from django.db.models import Q
import mimetypes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
# Create your views here.


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("new-entry"))

        form = CreateUserForm()
        return render(request, "PWRKapp/register.html", {
            "form": form
        })

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Konto dla " +
                             user + " zostało założone.")
            return HttpResponseRedirect(reverse("login")
                                        )
        return render(request, "PWRKapp/register.html", {
            "form": form
        })


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("new-entry"))
        return render(request, "PWRKapp/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("new-entry"))
        else:
            messages.info(request, "Niepoprawna nazwa użytkownika lub hasło")

        return render(request, "PWRKapp/login.html")


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


class StartingPageView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse("new-entry"))


@method_decorator(login_required(login_url="login"), name='dispatch')
class NewEntryView(View):

    def get(self, request):
        userLogged = False
        if request.user.is_authenticated:
            userLogged = True
        # welcome_user = request.META.get('REMOTE_USER')
        test_list = []
        for i in range(1, 30000):
            test_list.append(i)

        entry = EntryForm(form_type="new_entry_form")
        employee_type = request.session.get("employee_type")
        if employee_type is not None:
            entry.fields["type_of_employee"].initial = request.session["employee_type"]
            if entry.fields["type_of_employee"].initial == "Technolog":
                entry.fields["type_of_tool"].required = True

        context = {
            "nav_button_active": 1,
            "comp_list": test_list,
            "entry_form": entry,
            "user_logged": userLogged
        }
        return render(request, "PWRKapp/new_entry.html", context)

    def post(self, request):
        test_list = []
        for i in range(1, 30000):
            test_list.append(i)

        entry = EntryForm(request.POST, request.FILES,
                          form_type="new_entry_form")

        if entry.is_valid():
            employee = Employee.objects.filter(pk=request.user).first()
            entry.instance.entry_employee = employee
            entry.instance.entry_date = timezone.now()
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


@method_decorator(login_required(login_url="login"), name='dispatch')
class AllEntriesView(View):
    def get(self, request):
        userLogged = False
        if request.user.is_authenticated:
            userLogged = True
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

        employee = Employee.objects.filter(pk=request.user).first()

        entry = EntryForm(form_type="all_entry_form")
        return render(request, 'PWRKapp/all_entries.html', {
            "nav_button_active": 2,
            'page_obj': page_obj,
            'name_filter': name_filter,
            'created_after': created_after,
            'admin_user': employee.admin_accesss,
            "entry_form": entry,
            "page_number": page_number,
            "user_logged": userLogged
        })

    def post(self, request):

        entry = EntryForm(request.POST, form_type="all_entries_form")
        record = Entry.objects.filter(pk=request.POST.get("record-id")).first()

        if entry.is_valid():
            record.description_1 = entry.cleaned_data["description_1"]
            record.PWRK = entry.cleaned_data["PWRK"]
            record.reason = entry.cleaned_data["reason"]
            record.type_of_employee = entry.cleaned_data["type_of_employee"]
            record.type_of_tool = entry.cleaned_data["type_of_tool"]
            record.producer = entry.cleaned_data["producer"]
            record.supplier = entry.cleaned_data["supplier"]
            record.comments = entry.cleaned_data["comments"]
            record.status = entry.cleaned_data["status"]

            employee = Employee.objects.filter(pk=request.user).first()
            record.manage_employee = employee

            record.change_date = timezone.now()
            record.save(form_type="all_entries_form")

            page_number = request.POST.get('page')
            # new_entry.fields['type_of_employee'].initial = entry.cleaned_data["type_of_employee"]

            # messages.success(request, "Zgłoszenie zostało wysłane")
            # request.session["employee_type"] = entry.cleaned_data["type_of_employee"]

            return HttpResponseRedirect(reverse("all-entries") + f"?page={page_number}")

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
        page_number = request.POST.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'PWRKapp/all_entries.html', {
            "nav_button_active": 2,
            'page_obj': page_obj,
            'name_filter': name_filter,
            'created_after': created_after,
            'admin_user': True,
            "entry_form": entry
        })


class EntryHandlingView(View):
    def get(self, request):
        context = {
            "nav_button_active": 3
        }
        return render(request, "PWRKapp/new_entry.html", context)


def download(request, file_type, id):
    try:
        entry_record = Entry.objects.get(pk=id)
    except Entry.DoesNotExist:
        raise Http404("Plik nie istnieje.")

    # Sprawdź, które pole pliku zostało wybrane
    if file_type == 'drawings_2d':
        file = entry_record.drawings_2d
    elif file_type == 'drawings_3d':
        file = entry_record.drawings_3d
    elif file_type == 'screen_catalog':
        file = entry_record.screen_catalog
    else:
        raise Http404("Nieznany typ pliku.")

    # Sprawdzamy, czy plik jest przypisany
    if file:
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                mime_type, _ = mimetypes.guess_type(file.name)
                if not mime_type:
                    # Domyślny typ, jeśli nie możemy ustalić typu
                    mime_type = 'application/octet-stream'
                response = HttpResponse(f.read(), content_type=mime_type)
                response['Content-Disposition'] = f'attachment; filename="{
                    os.path.basename(file.name)}"'
                # Ustawienie dodatkowych nagłówków, aby wymusić pobieranie
                response['Content-Transfer-Encoding'] = 'binary'
                response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                response['Pragma'] = 'no-cache'
                response['Expires'] = '0'
                return response
        else:
            if file_type == 'drawings_2d':
                entry_record.drawings_2d = None
            elif file_type == 'drawings_3d':
                entry_record.drawings_3d = None
            elif file_type == 'screen_catalog':
                entry_record.screen_catalog = None
            entry_record.save()
            return HttpResponse("Plik nie istnieje w systemie.", status=404)
    else:
        return HttpResponse("Brak wybranego pliku.", status=404)
