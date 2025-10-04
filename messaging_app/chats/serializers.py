from rest_framework import serializers
from .models import user, Message, Conversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
        read_only_fields = ['user_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['message_id', 'sender_id', 'sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        read_only_fields = ['conversation_id', 'participants_id', 'created_at']