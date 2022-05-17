from telnetlib import IP
from .models import MyIPAddress 

class SaveMyIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request, count=0):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]

        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            ip_address = MyIPAddress.objects.get(ip_address=ip)
        except MyIPAddress.DoesNotExist:
            ip_address = MyIPAddress(ip_address=ip)  
            ip_address.save()
            
        request.user.ip_address = ip_address        
             
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response 
