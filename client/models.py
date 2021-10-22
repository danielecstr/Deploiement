
"""
Auteur : Fatma Aydin
"""
from django.db import models

class Client(models.Model):
    cli_id = models.AutoField(db_column='CLI_ID', primary_key=True)  # Field name made lowercase.
    cli_nom = models.CharField(db_column='CLI_NOM', blank=False, null=True, max_length=100)  # Field name made lowercase.
    cli_prenom = models.CharField(db_column='CLI_PRENOM', blank=False, null=True, max_length=100)  # Field name made lowercase.
    cli_adresseposte = models.CharField(db_column='CLI_ADRESSEPOSTE', blank=False, null=True, max_length=100)  # Field name made lowercase.
    cli_date_naissance = models.DateField(blank=False)  # Field name made lowercase.
    cli_mail = models.CharField(db_column='CLI_MAIL', blank=False, null=True, max_length=100)  # Field name made lowercase.
    cli_tel = models.CharField(db_column='CLI_TEl', blank=False, null=True, max_length=100)  # Field name made lowercase.
    cli_membre = models.CharField(db_column='CLI_MEMBRE', blank=False, null=True, max_length=100)  # Field name made lowercase.
    cli_date_debut = models.DateField(blank=True)  # Field name made lowercase.
    cli_date_fin = models.DateField(blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.cli_nom

    class Meta:
        managed = False
        db_table = 'Client'

