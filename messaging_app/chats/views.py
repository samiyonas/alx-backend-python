from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import APIView, status
from rest_framework.response import Response
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer 


class ConversationViewSet(APIView):
    def get(self, request, conversation_id=None):
        if conversation_id:
            try:
                conversation = Conversation.objects.get(conversation_id=conversation_id)
                serializer = ConversationSerializer(conversation)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Conversation.DoesNotExist:
                return Response({"error": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            conversations = Conversation.objects.all()
            serializer = ConversationSerializer(conversations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageViewSet(APIView):
    def get(self, request, message_id=None):
        if message_id:
            try:
                message = Message.objects.get(message_id=message_id)
                serializer = MessageSerializer(message)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Message.DoesNotExist:
                return Response({"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            messages = Message.objects.all()
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)