from orator.migrations import Migration


class CreateRegistrationSituationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('registration_situations') as table:
            table.increments('id')
            table.string('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('registration_situations')
