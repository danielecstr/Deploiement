from django.db import models

# Create your models here.

class Client(models.Model):
    cli_id = models.AutoField(db_column='CLI_ID', primary_key=True)  # Field name made lowercase.
    cli_nom = models.CharField(db_column='CLI_NOM', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_prenom = models.CharField(db_column='CLI_PRENOM', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_adresseposte = models.CharField(db_column='CLI_ADRESSEPOSTE', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_date_naissance = models.IntegerField(db_column='CLI_DATE_NAISSANCE', blank=True, null=True)  # Field name made lowercase.
    cli_mail = models.CharField(db_column='CLI_MAIL', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_tel = models.CharField(db_column='CLI_TEl', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_membre = models.CharField(db_column='CLI_MEMBRE', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_date_debut = models.DateField()  # Field name made lowercase.
    cli_date_fin = models.DateField()  # Field name made lowercase.

    def __str__(self):
        return self.cli_nom

    class Meta:
        managed = False
        db_table = 'Client'

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)
    CLI_ID = models.ForeignKey(Client, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_user'
