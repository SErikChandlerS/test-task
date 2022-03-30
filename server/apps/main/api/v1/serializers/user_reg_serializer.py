from rest_framework import serializers

from server.apps.main.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            sex=self.validated_data['sex'],
            avatar=self.validated_data['avatar'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})

        user.set_password(password)
        user.save()

        return user

