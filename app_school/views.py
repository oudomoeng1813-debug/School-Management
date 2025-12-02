from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.shortcuts import render
from .models import Student, Subject, Teacher
from .forms import StudentForm, SubjectForm, TeacherForm


def home(request):
    return render(request, 'home.html')


# ----------------------------
# STUDENT
# ----------------------------
class StudentListView(generic.ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'object_list'  # keeps your template unchanged
    paginate_by = 3  # 3 items per page

    def get_queryset(self):
        q = self.request.GET.get('q', '').strip()
        qs = Student.objects.all()
        if q:
            qs = qs.filter(
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q)
            )
        return qs.order_by('id')


class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')


class StudentDeleteView(generic.DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')


# ----------------------------
# SUBJECT
# ----------------------------
class SubjectListView(generic.ListView):
    model = Subject
    template_name = 'subject_list.html'
    context_object_name = 'subjects'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Subject.objects.all()
        if query:
            object_list = object_list.filter(
                Q(subject_name__icontains=query)
            )
        return object_list.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class SubjectCreateView(generic.CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_form.html'
    success_url = reverse_lazy('subject_list')


class SubjectUpdateView(generic.UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_form.html'
    success_url = reverse_lazy('subject_list')


class SubjectDeleteView(generic.DeleteView):
    model = Subject
    template_name = 'subject_confirm_delete.html'
    success_url = reverse_lazy('subject_list')


# ----------------------------
# TEACHER
# ----------------------------
class TeacherListView(generic.ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Teacher.objects.all()
        if query:
            object_list = object_list.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        return object_list.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class TeacherCreateView(generic.CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')


class TeacherUpdateView(generic.UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')


class TeacherDeleteView(generic.DeleteView):
    model = Teacher
    template_name = 'teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')
