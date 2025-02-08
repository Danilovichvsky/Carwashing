from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def handle_callback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        callback_data = data.get('callback_query', {}).get('data')
        if callback_data:
            action, booking_id = callback_data.split('_')
            if action == 'accept':
                print("accepted")
                # Обработка принятия бронирования

            elif action == 'reject':
                print("rejected")
                # Обработка отклонения бронирования

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)