from rest_framework import serializers


class CrewInputSerializer(serializers.Serializer):
    topic = serializers.CharField(max_length=255, required=True)


class CrewOutputSerializer(serializers.Serializer):
    markdown = serializers.CharField()  # Output formatted as Markdown
