from orator.migrations import Migration


class CreateServicesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('services') as table:
            table.increments('id')
            table.float('value')
            table.integer('service_type').unsigned()
            table.foreign('service_type').references('id').on('service_types')
            table.integer('budget').unsigned()
            table.foreign('budget').references('id').on('budgets')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('services')
