from orator.seeds import Seeder


class ServiceTypesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('service_types').insert({
            'description': 'limpeza de interior'
        })
        self.db.table('service_types').insert({
            'description': 'limpeza de exterior'
        })
        self.db.table('service_types').insert({
            'description': 'limpeza de estofados'
        })
        self.db.table('service_types').insert({
            'description': 'limpeza de carpetes'
        })
        self.db.table('service_types').insert({
            'description': 'lavanderia'
        })

