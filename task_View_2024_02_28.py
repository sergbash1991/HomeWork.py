class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods
        self.dict_methods = {'GET': self.get, 'POST': self.post, 'PUT': self.put, 'DELETE': self.delete}


    def get(self, request):
        return [f'{key}: <{value}>' for key, value in request.items()]

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods):
        super().__init__(methods)

    def render_request(self, request, method):
        if not isinstance(request, dict) or 'url' not in request.keys():
            raise ValueError(f'Invalid request type: {type(request)} or request doesn`t contain url')
        if method not in self.methods():
            raise TypeError('данный запрос не может быть выполнен')
        super().dict_methods[method](request)


dv = DetailView(methods=('GET', 'POST'))
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
print(html)
