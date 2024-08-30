from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Requirements
from .serializers import RequirementsSerializer
from django.http import Http404

class RequirementsListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        requirements = Requirements.objects.all()
        serializer = RequirementsSerializer(requirements, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequirementsSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequirementsDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Requirements.objects.get(pk=pk)
        except Requirements.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        requirement = self.get_object(pk)
        serializer = RequirementsSerializer(requirement)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        requirement = self.get_object(pk)
        serializer = RequirementsSerializer(requirement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        requirement = self.get_object(pk)
        requirement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
