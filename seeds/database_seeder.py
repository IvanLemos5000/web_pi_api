from orator.seeds import Seeder
from seeds.user_types_table_seeder import UserTypesTableSeeder
from seeds.registration_situations_table_seeder import RegistrationSituationsTableSeeder
from seeds.budget_situations_table_seeder import BudgetSituationsTableSeeder
from seeds.service_types_table_seeder import ServiceTypesTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(UserTypesTableSeeder)
        self.call(RegistrationSituationsTableSeeder)
        self.call(BudgetSituationsTableSeeder)
        self.call(ServiceTypesTableSeeder)

