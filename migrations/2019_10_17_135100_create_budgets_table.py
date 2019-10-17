from orator.migrations import Migration


class CreateBudgetsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('budgets') as table:
            table.increments('id')
            table.float('amount')
            table.date('execution_date').nullable()
            table.date('payment_date').nullable()
            table.integer('client').unsigned()
            table.foreign('client').references('id').on('clients')
            table.integer('service_provider').unsigned()
            table.foreign('service_provider').references('id').on('service_providers')
            table.integer('address').unsigned()
            table.foreign('address').references('id').on('addresses')
            table.integer('situation').unsigned()
            table.foreign('situation').references('id').on('budget_situations')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('budgets')
