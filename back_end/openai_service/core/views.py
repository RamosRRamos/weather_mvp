from celery.result import AsyncResult
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import generate_and_save_playlist
from common.snippets import get_playlist


# Create your views here.
class PlaylistView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
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
    def get(self, request, task_id):
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
