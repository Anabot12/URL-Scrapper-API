# url_scrapper_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .maincode import scrape_url
import json

@csrf_exempt  # Disable CSRF protection for simplicity in this example (not recommended for production)
def scrape_url_view(request):
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            result = scrape_url(json_input)
            return JsonResponse(result)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f"Error parsing JSON: {e}"}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method. Only POST requests are allowed.'}, status=405)

# url_scrapper_app/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
