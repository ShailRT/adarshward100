from .models import Navbar

def navbar(request):
    nav_obj = Navbar.objects.all()
    return {'nav_obj': nav_obj}