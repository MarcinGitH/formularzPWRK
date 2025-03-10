from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("new-entry", views.NewEntryView.as_view(), name="new-entry"),
    path("all-entries", views.AllEntriesView.as_view(), name="all-entries"),
    path("entry-handling", views.EntryHandlingView.as_view(), name="entry-handling"),
    path("download/<str:file_type>/<int:id>",
         views.download, name="download-handling"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.logoutUser, name="logout")
]
