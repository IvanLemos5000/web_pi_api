from orator.seeds import Seeder


class RegistrationSituationsTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('registration_situations').insert({
            'description': 'ativo'
        })
        self.db.table('registration_situations').insert({
            'description': 'bloqueado'
        })

