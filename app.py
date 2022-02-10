import falcon
from images import Resource

app = application = falcon.App();

app.add_route('/images', Resource(''))
app.add_route('/images/{name}', Resource(''))
