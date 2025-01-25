import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .messages import send_telegram

@api_view(['POST'])
def handle_message_tg_view(request):
    if request.method == 'POST':
        update = json.loads(request.body)
        print('Received update:', update)

        message = update.get('message', {}).get('text', '')
        chat_id = update.get('message', {}).get('chat', {}).get('id', '')

        print(f"Message: {message}, Chat ID: {chat_id}")

        if message:
            send_telegram(message,chat_id)
        return Response({'status': 'ok'})

