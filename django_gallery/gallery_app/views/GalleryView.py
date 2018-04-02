from django.views.generic import TemplateView
from gallery_app.models import Picture
from django.shortcuts import render
from django.conf import settings
import os

KEY_PICTURES = 'pictures'
KEY_MESSAGE = 'message'
KEY_ACTION = 'action'
KEY_ID = 'id'

ACTION_CREATE = 'create'
ACTION_GRAYSCALE = 'grayscale'
ACTION_DELETE = 'delete'

GRAYSCALE_SUFFIX = '_grayscale'

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
                self._doAddPicture(request.FILES)
            elif action == ACTION_GRAYSCALE:
                self._doSaveGrayscaledPicture(postContent)
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
        picture = postContent.get('picture', None)
        if not picture:
            self.message = 'Please choose a picture to upload.'
            return
        '''
        EXCEPTIONS HERE !!!
        '''
        newPicture = Picture(picture = picture)
        newPicture.save()
        return
    
    def _doSaveGrayscaledPicture(self, postContent):
        '''
        a method that saves grayscaled picture
        '''
        pictureId = postContent.get(KEY_ID, None)
        if not pictureId:
            return
        pictureToEdit = Picture.objects.get(pk=pictureId)
        if not pictureToEdit:
            return
        #pictureToEdit.name += GRAYSCALE_SUFFIX
        pictureToEdit.isGrayscaled = True
        pictureToEdit.save()
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
        self._doDeleteFileFromDisk(pictureToDelete.picture)
        return
    
    def _doDeleteFileFromDisk(self, fileToDelete):
        '''
        a method that deletes a file from a disk
        '''
        fileFolder = settings.MEDIA_ROOT
        filePath = '%s%s' % (fileFolder, fileToDelete)
        os.remove(filePath)
        return