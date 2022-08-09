from rest_framework import serializers
from users.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='name',
    )

    class Meta:
        model = User
        exclude = ['password']

# некорректно хешируются пароли, нет реализации добавления локаций через post-запрос
# class UserCreateSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#     locations = serializers.SlugRelatedField(
#         required=False,
#         queryset=Location.objects.all(),
#         many=True,
#         slug_field='name',
#     )
#     def create(self, validated_data):
#         user = super().create(validated_data)
#         user.set_password(user.password)
#         user.save()
#         return user
#     class Meta:
#         model = User
#         exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("locations", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data["password"])
        user.save()

        for locations in self._locations:
            obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(obj)

        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field='name',
    )

    def save(self, **kwargs):
        user = super().save()
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
