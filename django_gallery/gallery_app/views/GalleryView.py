from django.views.generic import TemplateView
from gallery_app.models import Picture
from gallery_app.forms import PictureModelForm
from django.shortcuts import render

class GalleryView(TemplateView):
    
    template_name = 'gallery.html'
    
    def get(self, request):
        import json
        print (json.dumps(request.GET, indent=3))
        #modelForm = PictureModelForm()
        pictures = self._getPictures()
        context = {'pictures': pictures}
        print (context)
        return render(request, self.template_name, context)
    
    def post(self, request):
        modelForm = PictureModelForm(request.POST)
        if modelForm.is_valid():
            print (modelForm.save())
        pictures = self._getPictures()
        context = {'pictures': pictures}
        print (context)
        return render(request, self.template_name, context)
    
    def _getPictures(self):
        return Picture.objects.all()