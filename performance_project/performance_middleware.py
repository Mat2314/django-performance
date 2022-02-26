from django.db import connection


class PerformanceMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(f"Endpoint {request.path} executed {len(connection.queries)} database queries")
        # print(connection.queries)
        return response