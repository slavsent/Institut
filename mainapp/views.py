from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class StudentListView(ListView):
    model = mainapp_models.Student
    paginate_by = 5

    def get_queryset(self):
        filter_firstname = self.request.GET.get('filter_firstname')
        filter_surname = self.request.GET.get('filter_surname')

        if filter_firstname and filter_surname:

            return super().get_queryset().filter(firstname__icontains=filter_firstname,
                                                 surname__icontains=filter_surname,
                                                 deleted=False)
        elif filter_firstname:

            return super().get_queryset().filter(firstname__icontains=filter_firstname, deleted=False)
        elif filter_surname:

            return super().get_queryset().filter(surname__icontains=filter_surname, deleted=False)
        else:

            return super().get_queryset().filter(deleted=False)


#class StudentCreateView(PermissionRequiredMixin, CreateView):
class StudentCreateView(CreateView):
    model = mainapp_models.Student
    fields = "__all__"
    success_url = reverse_lazy("mainapp:students")
    #permission_required = ("mainapp.add_student",)


class StudentDetailView(DetailView):
    model = mainapp_models.Student


#class StudentUpdateView(PermissionRequiredMixin, UpdateView):
class StudentUpdateView(UpdateView):
    model = mainapp_models.Student
    fields = "__all__"
    success_url = reverse_lazy("mainapp:students")
    #permission_required = ("mainapp.change_student",)


#class StudentDeleteView(PermissionRequiredMixin, DeleteView):
class StudentDeleteView(DeleteView):
    model = mainapp_models.Student
    success_url = reverse_lazy("mainapp:students")
    #permission_required = ("mainapp.delete_student",)


class TeachersListView(ListView):
    model = mainapp_models.Teachers
    paginate_by = 5

    def get_queryset(self):
        filter_firstname = self.request.GET.get('filter_firstname')
        filter_surname = self.request.GET.get('filter_surname')

        if filter_firstname and filter_surname:

            return super().get_queryset().filter(firstname__icontains=filter_firstname,
                                                 surname__icontains=filter_surname,
                                                 deleted=False)
        elif filter_firstname:

            return super().get_queryset().filter(firstname__icontains=filter_firstname, deleted=False)
        elif filter_surname:

            return super().get_queryset().filter(surname__icontains=filter_surname, deleted=False)
        else:

            return super().get_queryset().filter(deleted=False)


class TeachersCreateView(CreateView):
    model = mainapp_models.Teachers
    fields = "__all__"
    success_url = reverse_lazy("mainapp:teachers")


class TeachersDetailView(DetailView):
    model = mainapp_models.Teachers


class TeachersUpdateView(UpdateView):
    model = mainapp_models.Teachers
    fields = "__all__"
    success_url = reverse_lazy("mainapp:teachers")


class TeachersDeleteView(DeleteView):
    model = mainapp_models.Teachers
    success_url = reverse_lazy("mainapp:teachers")


class CardStudentListView(ListView):
    model = mainapp_models.CardStudent
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class CardStudentDetailView(DetailView):
    model = mainapp_models.CardStudent


class CardStudentDeleteView(DeleteView):
    model = mainapp_models.CardStudent
    success_url = reverse_lazy("mainapp:cardstudents")


class CoursesListView(ListView):
    model = mainapp_models.Courses
    paginate_by = 5

    def get_queryset(self):
        filter_name = self.request.GET.get('filter_name')
        filter_number = self.request.GET.get('filter_number')

        if filter_name and filter_number:
            return super().get_queryset().filter(firstname__icontains=filter_name,
                                                 number=filter_number,
                                                 deleted=False)
        elif filter_name:
            return super().get_queryset().filter(firstname__icontains=filter_name, deleted=False)
        elif filter_number:

            return super().get_queryset().filter(number=filter_number, deleted=False)
        else:

            return super().get_queryset().filter(deleted=False)


class CoursesDetailView(DetailView):
    model = mainapp_models.Courses


class CoursesDeleteView(DeleteView):
    model = mainapp_models.Courses
    success_url = reverse_lazy("mainapp:courses")


class TermsListView(ListView):
    model = mainapp_models.Terms
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class TermCoursesListView(ListView):
    model = mainapp_models.TermCourses
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
