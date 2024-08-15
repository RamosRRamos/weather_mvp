from celery import shared_task
from .models import OpenAIRequest, LogOpenAIRequest

@shared_task
def generate_and_save_playlist(response, request_code):
    """
    Celery task to generate and save a playlist response.

    This task handles the creation and saving of records in the database based on the GPT-generated response.
    It saves the prompt in the OpenAIRequest model and logs the full response and additional information
    in the LogOpenAIRequest model.

    Args:
        response (dict): The response dictionary containing the prompt and the GPT-generated playlist data.
        request_code (str): A unique code associated with the request for tracking purposes.

    Workflow:
        1. Creates a new OpenAIRequest record to store the prompt.
        2. Creates a new LogOpenAIRequest record to log the full response data and the associated request code.

    Models:
        - OpenAIRequest: Stores the prompt used in the GPT request.
        - LogOpenAIRequest: Logs the full response data, linking it to the OpenAIRequest and tracking it with the request code.
    """
    # Save the prompt in the OpenAIRequest model
    openai_request = OpenAIRequest.objects.create(prompt=response['prompt'])

    # Save the response and additional information in the LogOpenAIRequest model
    LogOpenAIRequest.objects.create(
        request=openai_request,
        data=response,
        request_code=request_code
    )
