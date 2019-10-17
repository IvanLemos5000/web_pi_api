from orator.migrations import Migration


class CreateBudgetSituationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('budget_situations') as table:
            table.increments('id')
            table.string('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('budget_situations')
