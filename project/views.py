from rest_framework import viewsets
from project.serializers import UserInfoSerializer
from rest_framework.response import Response

class TestView(viewsets.ViewSet):
    def test(self, request):
        serializer = UserInfoSerializer(request.user)
        return Response(serializer.data)