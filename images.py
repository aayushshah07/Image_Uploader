import falcon
import json
import io
import os
import uuid
import mimetypes
import re
class Resource :

    def __init__(self,storage_path):
        self._storage_path = storage_path

    def on_get(self,req,resp):
        data ={
            'images' :[
                {
                    'href' : 'Hi am there...'
                }
            ]
        }

        resp.text = json.dumps(data , ensure_ascii=False)
        resp.status = falcon.HTTP_200

    
    def on_post(self, req,resp):
        ext = mimetypes.guess_extension(req.content_type)
        name = '{uuid}{ext}'. format(uuid=uuid.uuid4(), ext=ext)

        image_path = os.path.join(self._storage_path, name)

        with io.open(image_path, 'wb') as image_file:
            while True :
                chunk = req.stream.read(5120)

                if not chunk :
                    break
                
                image_file.write(chunk)

        resp.status = falcon.HTTP_201
        resp.location = '/images/' + name

    def on_get(self,req,resp,name):
        resp.content_type =  mimetypes.guess_type(name)[0]
        image_path = os.path.join(self._storage_path , name)
        resp.stream = io.open(image_path,'rb')
        content_length = os.path.getsize(image_path)

# class Image_store:

#     def __init__(self,storage_path):
#         self._storage_path = storage_path

    
    

