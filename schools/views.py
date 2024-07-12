from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import School, Class, Stream, Student

# School Views
class SchoolListView(ListView):
    model = School
    template_name = 'school_list.html'


class SchoolDetailView(DetailView):
    model = School
    template_name = 'school_detail.html'


class SchoolCreateView(CreateView):
    model = School
    fields = ['name', 'address']
    template_name = 'school_form.html'
    success_url = reverse_lazy('school_list')


class SchoolUpdateView(UpdateView):
    model = School
    fields = ['name', 'address']
    template_name = 'school_form.html'
    success_url = reverse_lazy('school_list')


class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'school_confirm_delete.html'
    success_url = reverse_lazy('school_list')


# Class Views
class ClassListView(ListView):
    model = Class
    template_name = 'class_list.html'

    def get_queryset(self):
        return Class.objects.filter(school_id=self.kwargs['school_id'])


class ClassDetailView(DetailView):
    model = Class
    template_name = 'class_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_id'] = self.kwargs['school_id']
        return context


class ClassCreateView(CreateView):
    model = Class
    fields = ['name', 'school']
    template_name = 'class_form.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['school'] = get_object_or_404(School, pk=self.kwargs['school_id'])
        return initial

    def get_success_url(self):
        return reverse_lazy('class_list', kwargs={'school_id': self.object.school.id})


class ClassUpdateView(UpdateView):
    model = Class
    fields = ['name', 'school']
    template_name = 'class_form.html'

    def get_success_url(self):
        return reverse_lazy('class_list', kwargs={'school_id': self.object.school.id})


class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'class_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('class_list', kwargs={'school_id': self.object.school.id})


# Stream Views
class StreamListView(ListView):
    model = Stream
    template_name = 'stream_list.html'

    def get_queryset(self):
        return Stream.objects.filter(school_class_id=self.kwargs['class_id'])


class StreamDetailView(DetailView):
    model = Stream
    template_name = 'stream_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_id'] = self.kwargs['class_id']
        return context


class StreamCreateView(CreateView):
    model = Stream
    fields = ['name', 'school_class']
    template_name = 'stream_form.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['school_class'] = get_object_or_404(Class, pk=self.kwargs['class_id'])
        return initial

    def get_success_url(self):
        return reverse_lazy('stream_list', kwargs={'class_id': self.object.school_class.id})


class StreamUpdateView(UpdateView):
    model = Stream
    fields = ['name', 'school_class']
    template_name = 'stream_form.html'

    def get_success_url(self):
        return reverse_lazy('stream_list', kwargs={'class_id': self.object.school_class.id})


class StreamDeleteView(DeleteView):
    model = Stream
    template_name = 'stream_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('stream_list', kwargs={'class_id': self.object.school_class.id})


# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

    def get_queryset(self):
        return Student.objects.filter(stream_id=self.kwargs['stream_id'])


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'date_of_birth', 'stream']
    template_name = 'student_form.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['stream'] = get_object_or_404(Stream, pk=self.kwargs['stream_id'])
        return initial

    def get_success_url(self):
        return reverse_lazy('student_list', kwargs={'stream_id': self.object.stream.id})


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'date_of_birth', 'stream']
    template_name = 'student_form.html'

    def get_success_url(self):
        return reverse_lazy('student_list', kwargs={'stream_id': self.object.stream.id})


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('student_list', kwargs={'stream_id': self.object.stream.id})
