from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        context = {
            "nav_button_active": 1,
            "comp_list": test_list,
            # "welcome_user": welcome_user
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
