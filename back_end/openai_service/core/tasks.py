from celery import shared_task
from .models import OpenAIRequest, LogOpenAIRequest

@shared_task
def generate_and_save_playlist(response, request_code):


    # Salva o prompt na model OpenAIRequest
    openai_request = OpenAIRequest.objects.create(prompt=response['prompt'])

    # Salva a resposta e informações adicionais na model LogOpenAIRequest
    LogOpenAIRequest.objects.create(
        request=openai_request,
        data=response,
        request_code=request_code
    )
