"""
Auteur : Daniele Castro
"""

from datetime import date
from django import forms

from django.db import models

class Client(models.Model):
    cli_id = models.AutoField(db_column='CLI_ID', primary_key=True)  # Field name made lowercase.
    cli_nom = models.CharField(db_column='CLI_NOM', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_prenom = models.CharField(db_column='CLI_PRENOM', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_adresseposte = models.CharField(db_column='CLI_ADRESSEPOSTE', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_date_naissance = models.DateField()  # Field name made lowercase.
    cli_mail = models.CharField(db_column='CLI_MAIL', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_tel = models.CharField(db_column='CLI_TEl', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_membre = models.CharField(db_column='CLI_MEMBRE', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_date_debut = models.DateField()  # Field name made lowercase.
    cli_date_fin = models.DateField()  # Field name made lowercase.
    cli_num = models.IntegerField(db_column='CLI_NUM', blank=False)
    def __str__(self):
        return self.cli_nom  + " " + self.cli_prenom + " (" + str(self.cli_date_naissance) + ")"

    class Meta:
        managed = False
        db_table = 'Client'




class Velo(models.Model):
    vel_id = models.AutoField(db_column='VEL_ID', primary_key = True)  # Field name made lowercase.
    vel_num_cadre = models.IntegerField(db_column='VEL_NUM_CADRE', blank=True, null=True)  # Field name made lowercase.
    vel_nom = models.TextField(db_column='VEL_NOM', blank=True, null=True)  # Field name made lowercase.
    vel_marque = models.TextField(db_column='VEL_MARQUE', blank=True, null=True)  # Field name made lowercase.
    vel_couleur = models.TextField(db_column='VEL_COULEUR', blank=True, null=True)  # Field name made lowercase.
    vel_type = models.TextField(db_column='VEL_TYPE', blank=True, null=True)  # Field name made lowercase.
    vel_photo = models.TextField(db_column='VEL_PHOTO', blank=True, null=True)  # Field name made lowercase.
    vel_statut = models.TextField(db_column='VEL_STATUT', blank=True, null=True)  # Field name made lowercase.
    vel_etat = models.TextField(db_column='VEL_ETAT', blank=True, null=True)  # Field name made lowercase.
    vel_remarque = models.TextField(db_column='VEL_REMARQUE', blank=True, null=True)  # Field name made lowercase.
    vel_num = models.IntegerField(db_column='VEL_NUM', blank=True)

    def __str__(self):
        return self.vel_nom


    class Meta:
        managed = False
        db_table = 'Velo'



class Location(models.Model):

    STAUT_CHOICES = [
        ('En cours', 'En cours'),
        ('Annulé', 'Annulé'),
        ('Demande de diminution', 'Demande de diminution'),
        ('Demande de prolongation', 'Demande de prolongation'),
        ('En attente', 'En attente'),
        ('Terminé', 'Terminé'),]
    loc_id = models.AutoField(db_column='LOC_ID', primary_key = True)  #Field name made lowercase.
    loc_statut = models.CharField(db_column='LOC_STATUT', blank=True, null=True, max_length=30,choices=STAUT_CHOICES, default='En cours')  # Field name made lowercase.
    loc_client = models.ForeignKey(Client, on_delete=models.CASCADE)  #Field name made lowercase.
    loc_num = models.IntegerField(db_column='LOC_NUM', blank=False)
    date_modifier = models.DateField(blank=True)

    class Meta:
        managed = False
        db_table = 'Location'



class Location_Velo(models.Model):
    STAUT_CHOICES = [
        ('En cours', 'En cours'),
        ('Annulé', 'Annulé'),
        ('Terminé', 'Terminé'), ]
    date_debut = models.DateField()  # Field name made lowercase.
    date_fin   = models.DateField()  # Field name made lowercase.
    lv_loc_id = models.ForeignKey(Location, on_delete=models.CASCADE)  # Field name made lowercase.
    lv_vel_id = models.ForeignKey(Velo, on_delete=models.CASCADE)  # Field name made lowercase.
    mail_envoyer = models.CharField(default="False", max_length=30)
    loc_statut = models.CharField(db_column='LOC_STATUT', blank=True, null=True, max_length=30,choices=STAUT_CHOICES, default='En cours')  # Field name made lowercase.
    loc_num = models.IntegerField(db_column='LOC_NUM', blank=False)
    def ends_within_10_days(self):
        return (self.date_fin - date.today()).days < 11
    def termine(self):
        return (date.today() - self.date_fin).days >= 0
    def annule(self):
        return self.lv_loc_id.loc_statut == "Annulé"

    class Meta:
        managed = False
        db_table = 'Location_Velo'


