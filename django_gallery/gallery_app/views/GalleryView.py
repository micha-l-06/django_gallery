from django.views.generic import TemplateView
from gallery_app.models import Picture
from django.shortcuts import render

KEY_PICTURES = 'pictures'
KEY_MESSAGE = 'message'
KEY_ACTION = 'action'
KEY_ID = 'id'

ACTION_CREATE = 'create'
ACTION_GRAYSCALE = 'grayscale'
ACTION_DELETE = 'delete'

class GalleryView(TemplateView):
    '''
    a class that processes gallery HTTP requests
    '''
    
    template_name = 'gallery.html'
    
    def __init__(self):
        '''
        a constructor method
        '''
        self.message = ''
        return
    
    def get(self, request):
        '''
        a method that processes GET request
        '''
        context = {
            KEY_PICTURES: self._getPictures(),
            KEY_MESSAGE: ''
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        '''
        a method that processes POST request
        '''
        message = ''
        action = request.POST.get(KEY_ACTION, None)
        if action:
            postContent = request.POST
            if action == ACTION_CREATE:
                self._doAddPicture(postContent)
            elif action == ACTION_GRAYSCALE:
                self._doGrayscalePicture(postContent)
            elif action == ACTION_DELETE:
                self._doDeletePicture(postContent)
        context = {
            KEY_PICTURES: self._getPictures(),
            KEY_MESSAGE: self.message
        }
        return render(request, self.template_name, context)
    
    def _getPictures(self):
        '''
        a method that returns all pictures from a database
        '''
        return Picture.objects.all()
    
    def _doAddPicture(self, postContent):
        '''
        a method that adds a picture to a dataabse
        '''
        name = postContent.get('name', None)
        '''
        EXCEPTIONS HERE !!!
        '''
        newPicture = Picture(name = name)
        newPicture.save()
        return
    
    def _doGrayscalePicture(self, postContent):
        return
    
    def _doDeletePicture(self, postContent):
        '''
        a method that deletes a picture
        '''
        pictureId = postContent.get(KEY_ID, None)
        if not pictureId:
            return
        pictureToDelete = Picture.objects.get(pk=pictureId)
        if not pictureToDelete:
            return
        pictureToDelete.delete()
        return