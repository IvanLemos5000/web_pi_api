from rest_framework.serializers import ModelSerializer
from api.models import Addresses, BudgetSituations, Budgets, Clients, Migrations, RegistrationSituations, ServiceProviders, ServiceTypes, Services, UserTypes, Users


class AddressesSerializer(ModelSerializer):

    class Meta:
        model = Addresses
        fields = '__all__'


class BudgetSituationsSerializer(ModelSerializer):

    class Meta:
        model = BudgetSituations
        fields = '__all__'


class BudgetsSerializer(ModelSerializer):

    class Meta:
        model = Budgets
        fields = '__all__'


class ClientsSerializer(ModelSerializer):

    class Meta:
        model = Clients
        fields = '__all__'


class MigrationsSerializer(ModelSerializer):

    class Meta:
        model = Migrations
        fields = '__all__'


class RegistrationSituationsSerializer(ModelSerializer):

    class Meta:
        model = RegistrationSituations
        fields = '__all__'


class ServiceProvidersSerializer(ModelSerializer):

    class Meta:
        model = ServiceProviders
        fields = '__all__'


class ServiceTypesSerializer(ModelSerializer):

    class Meta:
        model = ServiceTypes
        fields = '__all__'


class ServicesSerializer(ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'


class UserTypesSerializer(ModelSerializer):

    class Meta:
        model = UserTypes
        fields = '__all__'


class UsersSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'
