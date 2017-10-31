import falcon
import json
 
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world!'
 
    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Error',
                ex.message)
 
        try:
            result_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Malformed JSON',
                'Could not decode the request body. The '
                'JSON was incorrect.')
 
        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, encoding='utf-8')
 
# falcon.API instances are callable WSGI apps
wsgi_app = api = falcon.API()
 
# Resources are represented by long-lived class instances
things = ThingsResource()
 
# things will handle all requests to the '/things' URL path
api.add_route('/things', things)
