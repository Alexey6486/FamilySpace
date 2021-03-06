from rest_framework import serializers

from api.apigroupapp.serializers import GroupSerializer
from authapp.models import UserProfile, User
from groupapp.models import GroupUser
from api.core import errorcodes
from api.core import exceptions
from userapp.models import UserContactList


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.HiddenField(default='', required=False)

    class Meta:
        model = UserProfile
        fields = ('gender', 'birth_date', 'id', 'email',
                  'first_name', 'last_name', 'patronymic', 'phone', 'password')
        read_only_fields = ('id', 'password')

    def update(self, instance, validated_data):
        # почему то он даёт изменять других пользователей и без проверки
        # if self.context['request'].user.id != self.initial_data['id']:
        #     raise exceptions.FamilySpaceException(**errorcodes.ERR_NO_RIGHTS_FOR_ACTION)
        if 'email' in self.initial_data:
            self.context['request'].user.email = self.initial_data['email']
        if 'password' in self.initial_data and self.initial_data['password']:
            self.context['request'].user.set_password(self.initial_data['password'])
        self.context['request'].user.save()
        return super().update(instance, validated_data)


class ContactListSerializer(serializers.ModelSerializer):
    contact_user = UserProfileSerializer(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    contact_user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserContactList
        fields = ('id', 'contact_user', 'user', 'contact_user_id')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = validated_data['user']
        contact_user_id = validated_data['contact_user_id']
        try:
            contact_user = User.objects.get(pk=validated_data['contact_user_id'])
        except User.DoesNotExist:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_USER_NOT_FOUND)
        if UserContactList.objects.filter(user=user, contact_user=contact_user_id):
            raise exceptions.FamilySpaceException(**errorcodes.ERR_USER_ALREADY_IN_CONTACT_LIST)

        return super().create(validated_data)


class GetUserGroupsSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        model = GroupUser
        fields = ['group']
