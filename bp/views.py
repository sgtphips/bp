from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView, TemplateView
from home.models import Summary, Experience, School, Skill, Certification

# ListView Example
# from django.views.generic import ListView
# from [someapp].models import [Some Model]

# class AcmeBookList(ListView):

# 	context_object_name = 'book_list'
# 	queryset = Book.objects.filter(publisher__name='Acme Publishing')
# 	template_name = 'books/acme_list.html'

# DetailView Example

# CreateView Example

# DeleteView Example

# UpdateView Example

# RedirectView Example

# TemplateView Example



class HomeTemplateView(TemplateView):
	context_object_name = 'home'
	template_name = 'home/home.html'

	def get_context_data(self, **kwargs):
	    context = super(HomeTemplateView, self).get_context_data(**kwargs)
	    context['summaries'] = Summary.objects.all()
	    context['experiences'] = Experience.objects.all()
	    context['schools'] = School.objects.all()
	    context['skills'] = Skill.objects.all()
	    context['certifications'] = Certification.objects.all()

	    return context