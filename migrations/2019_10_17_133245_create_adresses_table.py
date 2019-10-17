from orator.migrations import Migration


class CreateAdressesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('addresses') as table:
            table.increments('id')
            table.string('street')
            table.integer('number')
            table.string('complement').nullable()
            table.string('neighborhood')
            table.integer('zip_code')
            table.string('city')
            table.string('state')
            table.integer('user_type').unsigned()
            table.foreign('user_type').references('id').on('user_types')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('addresses')
