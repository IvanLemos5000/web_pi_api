# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    complement = models.CharField(max_length=255, blank=True, null=True)
    neighborhood = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    user_type = models.ForeignKey('UserTypes', models.DO_NOTHING, db_column='user_type')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addresses'


class BudgetSituations(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'budget_situations'


class Budgets(models.Model):
    amount = models.FloatField(blank=True, null=True)
    execution_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING, db_column='client')
    service_provider = models.ForeignKey('ServiceProviders', models.DO_NOTHING, db_column='service_provider')
    address = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='address')
    situation = models.ForeignKey(BudgetSituations, models.DO_NOTHING, db_column='situation')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'budgets'


class Clients(models.Model):
    name = models.CharField(max_length=255)
    document = models.IntegerField()
    telephone = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')
    address = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='address')
    situation = models.ForeignKey('RegistrationSituations', models.DO_NOTHING, db_column='situation')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clients'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class RegistrationSituations(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registration_situations'


class ServiceProviders(models.Model):
    legal_name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    telephone = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')
    address = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='address')
    situation = models.ForeignKey(RegistrationSituations, models.DO_NOTHING, db_column='situation')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_providers'


class ServiceTypes(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_types'


class Services(models.Model):
    value = models.FloatField()
    service_type = models.ForeignKey(ServiceTypes, models.DO_NOTHING, db_column='service_type')
    budget = models.ForeignKey(Budgets, models.DO_NOTHING, db_column='budget')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'services'


class UserTypes(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_types'


class Users(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_type = models.ForeignKey(UserTypes, models.DO_NOTHING, db_column='user_type')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'
