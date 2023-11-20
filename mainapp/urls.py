from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("students/", views.StudentListView.as_view(), name="students"),
    path("students/create/", views.StudentCreateView.as_view(), name="students_create"),
    path("students/<str:pk>/detail", views.StudentDetailView.as_view(), name="students_detail"),
    path("students/<str:pk>/update", views.StudentUpdateView.as_view(), name="students_update"),
    path("students/<str:pk>/delete", views.StudentDeleteView.as_view(), name="students_delete"),
    path("teachers/", views.TeachersListView.as_view(), name="teachers"),
    path("teachers/create/", views.TeachersCreateView.as_view(), name="teachers_create"),
    path("teachers/<str:pk>/detail", views.TeachersDetailView.as_view(), name="teachers_detail"),
    path("teachers/<str:pk>/update", views.TeachersUpdateView.as_view(), name="teachers_update"),
    path("teachers/<str:pk>/delete", views.TeachersDeleteView.as_view(), name="teachers_delete"),
    path("cardstudent/", views.CardStudentListView.as_view(), name="cardstudents"),
    path("cardstudent/<str:pk>/detail", views.CardStudentDetailView.as_view(), name="cardstudents_detail"),
    path("cardstudent/<str:pk>/delete", views.CardStudentDeleteView.as_view(), name="cardstudents_delete"),
    path("courses/", views.CoursesListView.as_view(), name="courses"),
    path("courses/<str:pk>/detail", views.CoursesDetailView.as_view(), name="courses_detail"),
    path("courses/<str:pk>/delete", views.CoursesDeleteView.as_view(), name="courses_delete"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("login/", views.LoginPageView.as_view(), name="login"),
]
