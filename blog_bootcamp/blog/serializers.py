from rest_framework import serializers

class CategorySerializers(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class NewsSerializers(serializers.Serializer):
    category = serializers.CharField()
    title = serializers.CharField()
    tags = serializers.CharField()
    summary = serializers.CharField()
    content = serializers.CharField()
    image = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()