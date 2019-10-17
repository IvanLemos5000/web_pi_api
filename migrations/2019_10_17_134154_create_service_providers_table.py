from orator.migrations import Migration


class CreateServiceProvidersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('service_providers') as table:
            table.increments('id')
            table.string('legal_name')
            table.string('business_name')
            table.string('document')
            table.integer('telephone')
            table.integer('user').unsigned()
            table.foreign('user').references('id').on('users')
            table.integer('address').unsigned()
            table.foreign('address').references('id').on('addresses')
            table.integer('situation').unsigned()
            table.foreign('situation').references('id').on('registration_situations')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('service_providers')
