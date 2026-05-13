

def session_context(request):
    setted_name = request.session.get('random_user')
    return {'setted_name': setted_name}
