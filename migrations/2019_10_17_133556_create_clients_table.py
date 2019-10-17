from orator.migrations import Migration


class CreateClientsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('clients') as table:
            table.increments('id')
            table.string('name')
            table.integer('document')
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
        self.schema.drop('clients')
