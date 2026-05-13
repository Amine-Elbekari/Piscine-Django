import time
import random
from django.conf import settings

def session_context(request):
    users = settings.ANYONYM_USERS
    current_time = time.time()
    
    if not request.session.get('random_user'):
        request.session['random_user'] = random.choice(users)
        request.session['timestamp'] = current_time
    else:
        time_saved = request.session.get('timestamp', current_time)
        if current_time - time_saved >= 42:
            request.session['random_user'] = random.choice(users)
            request.session['timestamp'] = current_time
            
    return {'setted_name': request.session.get('random_user')}
