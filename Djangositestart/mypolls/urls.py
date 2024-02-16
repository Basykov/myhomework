from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="main_page"),
    path("first_sub/", views.return_simple_html, name="first_sub"),
    path("second_page/", views.return_html_page, name="second_page"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("note/", views.return_note_page, name="note"),
    path("note_list/", views.return_note_list, name="note_list"),
    path("note_detail/<int:pk>/", views.return_note_detail, name="note_detail"),
    path("note_delete/<int:pk>/", views.return_delete_note, name="note_delete")
]