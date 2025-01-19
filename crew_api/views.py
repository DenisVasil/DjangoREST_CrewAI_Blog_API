from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CrewInputSerializer, CrewOutputSerializer
from .crew.crew import crew


class CrewProcessView(APIView):
    def post(self, request):
        # Validate input
        input_serializer = CrewInputSerializer(data=request.data)
        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Extract validated data
        topic = input_serializer.validated_data['topic']

        # Run the Crew logic
        try:
            res = crew.kickoff(inputs={"topic": topic})
            result = res.raw
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Prepare the response
        output_serializer = CrewOutputSerializer(data={"markdown": result})
        if output_serializer.is_valid():
            return Response(output_serializer.data, status=status.HTTP_200_OK)

        return Response(output_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
