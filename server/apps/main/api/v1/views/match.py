from django.core.mail import send_mail
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from server.apps.main.api.v1.serializers.match_serializer import MatchSerializer
from server.apps.main.models import Match, User
from server.settings.components.common import EMAIL_HOST_USER


class MatchView(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    http_method_names = ['post']

    @action(detail=True, methods=['POST'], name='send_your_match')
    def match(self, request, pk=None):
        sender = request.user
        recipient = User.objects.get(pk=pk)

        serializer = MatchSerializer(context={'recipient': recipient, 'request': request}, data=request.data)
        data_valid = serializer.is_valid(raise_exception=True)
        if data_valid:
            serializer.save()

        reverse_match = Match.objects.filter(sender=recipient, recipient=sender)
        if reverse_match:
            send_mail(
                f'Good afternoon, {sender.first_name}',
                f'You have a match with {recipient.first_name}! Email: {recipient.email}',
                EMAIL_HOST_USER,
                [sender.email],
                fail_silently=False,
            )
            send_mail(
                f'Good afternoon, {recipient.first_name}',
                f'You have a match with {sender.first_name}! Email: {sender.email}',
                EMAIL_HOST_USER,
                [recipient.email],
                fail_silently=False,
            )

            return Response(recipient.email, 201)
        else:
            return Response(f'Your sympathy had been sent to the user {recipient.first_name}.', 201)
