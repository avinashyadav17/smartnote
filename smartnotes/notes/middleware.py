from django.http import HttpResponse

class BlockIPMiddleware:  # << Class name must match what you use in settings
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_ips = ['127.0.0.2']

        if request.META.get('REMOTE_ADDR') in blocked_ips:
            return HttpResponse("Access Denied")

        response = self.get_response(request)
        return response
