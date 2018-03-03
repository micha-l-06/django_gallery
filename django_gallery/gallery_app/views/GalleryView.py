from django.views.generic import TemplateView
from django.shortcuts import render

class GalleryView(TemplateView):
    
    template_name = 'gallery.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
        