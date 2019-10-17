from orator.migrations import Migration


class CreateServiceTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('service_types') as table:
            table.increments('id')
            table.string('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('service_types')
