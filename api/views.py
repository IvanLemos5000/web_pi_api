from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import AddressesSerializer, BudgetSituationsSerializer, BudgetsSerializer, ClientsSerializer, MigrationsSerializer, RegistrationSituationsSerializer, ServiceProvidersSerializer, ServiceTypesSerializer, ServicesSerializer, UserTypesSerializer, UsersSerializer
from api.models import Addresses, BudgetSituations, Budgets, Clients, Migrations, RegistrationSituations, ServiceProviders, ServiceTypes, Services, UserTypes, Users


class AddressesAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Addresses.objects.get(pk=id)
            serializer = AddressesSerializer(item)
            return Response(serializer.data)
        except Addresses.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Addresses.objects.get(pk=id)
        except Addresses.DoesNotExist:
            return Response(status=404)
        serializer = AddressesSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Addresses.objects.get(pk=id)
        except Addresses.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AddressesAPIListView(APIView):

    def get(self, request, format=None):
        items = Addresses.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AddressesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BudgetSituationsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = BudgetSituations.objects.get(pk=id)
            serializer = BudgetSituationsSerializer(item)
            return Response(serializer.data)
        except BudgetSituations.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = BudgetSituations.objects.get(pk=id)
        except BudgetSituations.DoesNotExist:
            return Response(status=404)
        serializer = BudgetSituationsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = BudgetSituations.objects.get(pk=id)
        except BudgetSituations.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BudgetSituationsAPIListView(APIView):

    def get(self, request, format=None):
        items = BudgetSituations.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = BudgetSituationsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BudgetSituationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BudgetsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Budgets.objects.get(pk=id)
            serializer = BudgetsSerializer(item)
            return Response(serializer.data)
        except Budgets.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Budgets.objects.get(pk=id)
        except Budgets.DoesNotExist:
            return Response(status=404)
        serializer = BudgetsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Budgets.objects.get(pk=id)
        except Budgets.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BudgetsAPIListView(APIView):

    def get(self, request, format=None):
        items = Budgets.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = BudgetsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BudgetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ClientsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Clients.objects.get(pk=id)
            serializer = ClientsSerializer(item)
            return Response(serializer.data)
        except Clients.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Clients.objects.get(pk=id)
        except Clients.DoesNotExist:
            return Response(status=404)
        serializer = ClientsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Clients.objects.get(pk=id)
        except Clients.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ClientsAPIListView(APIView):

    def get(self, request, format=None):
        items = Clients.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ClientsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MigrationsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Migrations.objects.get(pk=id)
            serializer = MigrationsSerializer(item)
            return Response(serializer.data)
        except Migrations.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Migrations.objects.get(pk=id)
        except Migrations.DoesNotExist:
            return Response(status=404)
        serializer = MigrationsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Migrations.objects.get(pk=id)
        except Migrations.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MigrationsAPIListView(APIView):

    def get(self, request, format=None):
        items = Migrations.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = MigrationsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = MigrationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RegistrationSituationsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = RegistrationSituations.objects.get(pk=id)
            serializer = RegistrationSituationsSerializer(item)
            return Response(serializer.data)
        except RegistrationSituations.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = RegistrationSituations.objects.get(pk=id)
        except RegistrationSituations.DoesNotExist:
            return Response(status=404)
        serializer = RegistrationSituationsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = RegistrationSituations.objects.get(pk=id)
        except RegistrationSituations.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RegistrationSituationsAPIListView(APIView):

    def get(self, request, format=None):
        items = RegistrationSituations.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RegistrationSituationsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RegistrationSituationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ServiceProvidersAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = ServiceProviders.objects.get(pk=id)
            serializer = ServiceProvidersSerializer(item)
            return Response(serializer.data)
        except ServiceProviders.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = ServiceProviders.objects.get(pk=id)
        except ServiceProviders.DoesNotExist:
            return Response(status=404)
        serializer = ServiceProvidersSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = ServiceProviders.objects.get(pk=id)
        except ServiceProviders.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ServiceProvidersAPIListView(APIView):

    def get(self, request, format=None):
        items = ServiceProviders.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ServiceProvidersSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceProvidersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ServiceTypesAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = ServiceTypes.objects.get(pk=id)
            serializer = ServiceTypesSerializer(item)
            return Response(serializer.data)
        except ServiceTypes.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = ServiceTypes.objects.get(pk=id)
        except ServiceTypes.DoesNotExist:
            return Response(status=404)
        serializer = ServiceTypesSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = ServiceTypes.objects.get(pk=id)
        except ServiceTypes.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ServiceTypesAPIListView(APIView):

    def get(self, request, format=None):
        items = ServiceTypes.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ServiceTypesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceTypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ServicesAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Services.objects.get(pk=id)
            serializer = ServicesSerializer(item)
            return Response(serializer.data)
        except Services.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Services.objects.get(pk=id)
        except Services.DoesNotExist:
            return Response(status=404)
        serializer = ServicesSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Services.objects.get(pk=id)
        except Services.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ServicesAPIListView(APIView):

    def get(self, request, format=None):
        items = Services.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ServicesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserTypesAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserTypes.objects.get(pk=id)
            serializer = UserTypesSerializer(item)
            return Response(serializer.data)
        except UserTypes.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserTypes.objects.get(pk=id)
        except UserTypes.DoesNotExist:
            return Response(status=404)
        serializer = UserTypesSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserTypes.objects.get(pk=id)
        except UserTypes.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserTypesAPIListView(APIView):

    def get(self, request, format=None):
        items = UserTypes.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserTypesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserTypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UsersAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Users.objects.get(pk=id)
            serializer = UsersSerializer(item)
            return Response(serializer.data)
        except Users.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Users.objects.get(pk=id)
        except Users.DoesNotExist:
            return Response(status=404)
        serializer = UsersSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Users.objects.get(pk=id)
        except Users.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UsersAPIListView(APIView):

    def get(self, request, format=None):
        items = Users.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UsersSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
