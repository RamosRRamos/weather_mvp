from celery.result import AsyncResult
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import generate_and_save_playlist
from common.snippets import get_playlist


class PlaylistView(APIView):
    """
    API view to generate a music playlist based on a specified genre and optionally save it asynchronously.

    This view handles GET requests, generating a playlist based on the provided genre and amount of songs.
    The playlist generation task is then queued for asynchronous processing.

    Permission:
        - AllowAny: This view is accessible without authentication.

    Methods:
        - get: Handles GET requests to generate and queue the playlist generation task.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        """
        Handles GET requests to generate a playlist and queue the playlist saving task.

        Query Parameters:
            - genre (str): The music genre for the playlist (optional).
            - amount (int): The number of songs in the playlist (default is 10).
            - request_code (str): A unique code associated with the request (optional).

        Workflow:
            1. Generates a playlist based on the provided genre and amount.
            2. Queues the task to save the playlist asynchronously using Celery.

        Returns:
            - HTTP 200 OK: If the playlist is successfully generated and the task is queued.
            - HTTP 500 Internal Server Error: If an error occurs during playlist generation or task queuing.
        """
        genre = request.query_params.get("genre", None)
        amount = request.query_params.get("amount", 10)
        request_code = request.query_params.get("request_code", None)

        playlist = get_playlist(genre, amount=int(amount))

        generate_and_save_playlist.delay(playlist, request_code)

        try:
            return Response({"playlist": playlist}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TaskStatusView(APIView):
    """
    API view to check the status of an asynchronous task.

    This view handles GET requests to check the status of a Celery task by its task ID.

    Permission:
        - AllowAny: This view is accessible without authentication.

    Methods:
        - get: Handles GET requests to retrieve the status of the specified task.
    """

    def get(self, request, task_id):
        """
        Handles GET requests to retrieve the status of a Celery task.

        URL Parameters:
            - task_id (str): The ID of the task to check.

        Returns:
            - HTTP 200 OK: If the task status is retrieved successfully.
                - Includes the status (PENDING, SUCCESS, FAILURE) and the result or error if applicable.
            - HTTP 500 Internal Server Error: If the task failed during execution.
        """
        result = AsyncResult(task_id)
        if result.state == "PENDING":
            return Response({"status": "PENDING"}, status=status.HTTP_200_OK)
        elif result.state == "SUCCESS":
            return Response(
                {"status": "SUCCESS", "result": result.result},
                status=status.HTTP_200_OK,
            )
        elif result.state == "FAILURE":
            return Response(
                {"status": "FAILURE", "error": str(result.info)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        else:
            return Response({"status": result.state}, status=status.HTTP_200_OK)
