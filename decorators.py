from django.shortcuts import redirect


def login_required(function):

    def wrapper(request, *args, **kwargs): # Added **kwargs
        if 'user' not in request.session: # Changed 'usuario' to 'user'
            return redirect('/login')
        resp = function(request, *args, **kwargs) # Pass **kwargs
        return resp
    
    return wrapper