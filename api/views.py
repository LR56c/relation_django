from django.http import JsonResponse

def index( request ):
	context = {
		'success': True,
	}
	return JsonResponse( context, status=200 )
