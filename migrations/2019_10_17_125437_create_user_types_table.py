from orator.migrations import Migration


class CreateUserTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('user_types') as table:
            table.increments('id')
            table.string('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('user_types')
