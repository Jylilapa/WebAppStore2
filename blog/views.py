from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Record

class BlogListView(LoginRequiredMixin, ListView):
    model = Record

    # def get_queryset(self):
    #     return Record.objects.filter(publication=True)


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Record

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter_views += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Record
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:record_list")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:record_list")

    def get_success_url(self):
        return reverse("blog:record_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = reverse_lazy("blog:record_list")
