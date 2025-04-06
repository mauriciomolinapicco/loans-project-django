from django.http import HttpResponse

def allowed_users(allowed_roles=[]):
    """
        Decorador para permitir el acceso a vistas solo para usuarios de grupos específicos.
        Verifica si el usuario pertenece a uno de los grupos permitidos. Si es así, permite el acceso a la vista.
        En caso contrario, devuelve un mensaje de error.
        Parámetros:
        allowed_roles: Lista de grupos permitidos para acceder a la vista.
        view_func: La función de vista que será decorada.

        En este caso tenemos solamente un grupo, al cual el usuario con las credenciales enviadas por mail pertenece
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Usted no esta autorizado a ingresar a esta pagina')

        return wrapper_func
    return decorator
