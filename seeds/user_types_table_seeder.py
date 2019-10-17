from orator.seeds import Seeder


class UserTypesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('user_types').insert({
            'description': 'cliente'
        })
        self.db.table('user_types').insert({
            'description': 'prestador'
        })


