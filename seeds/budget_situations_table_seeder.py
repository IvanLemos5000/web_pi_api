from orator.seeds import Seeder


class BudgetSituationsTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('budget_situations').insert({
            'description': 'aberto'
        })
        self.db.table('budget_situations').insert({
            'description': 'aguardando aprovação'
        })
        self.db.table('budget_situations').insert({
            'description': 'aprovado'
        })
        self.db.table('budget_situations').insert({
            'description': 'pago'
        })
        self.db.table('budget_situations').insert({
            'description': 'finalizado'
        })

