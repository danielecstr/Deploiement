# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files import File

"""
my_choices = [
       ('Ridley', 'Ridley'),
       ('Pinarello', 'Pinarello'),
       ('De Rosa', 'De Rosa'),
       ('Cannondale', 'Cannondale'),
       ('Specialized', 'Specialized'),
       ('Van Rysel', 'Van Rysel'),
       ('Eddardo Bianchi', 'Eddardo Bianchi'),
       ('Look', 'Look'),
   ]

class ItStore(models.Model):
    item_name = models.CharField(max_length='100', blank=True, null=False, choices=type_choice)
    quantity = models.IntegerField(default='', blank=True, null=False)
    MARQUE_CHOICES = [
        ('Ridley', 'Ridley'),
        ('Pinarello', 'Pinarello'),
        ('De Rosa', 'De Rosa'),
        ('Cannondale', 'Cannondale'),
        ('Specialized', 'Specialized'),
        ('Van Rysel', 'Van Rysel'),
        ('Eddardo Bianchi', 'Eddardo Bianchi'),
        ('Look', 'Look'),
    ]

    COULEUR_CHOICES = [
   ('Rouge', 'Rouge'),
       ('Vert', 'Vert'),
       ('Bleu', 'Bleue'),
      ('Jane', 'Jaune'),
      ('Violet', 'Violet'),
       ('Rose', 'Rose'),
       ('Orange', 'Orange'),
       ('Cyan', 'Cyan'),
       ('Brun', 'Brun'),
       ('Noir', 'Noir'),
       ('Gris', 'Gris'),
       ('Blanc', 'Blanc'),
   ]

   TYPE_CHOICES = [
       ('VTT', 'Vélo Tout-Terrain'),
       ('VR', 'Vélo de route'),
       ('BMX', 'BMX'),
   ]

   ETAT_CHOICES = [
       ('Cassé', 'Cassé'),
      ('Bon état', 'Bon état'),
       ('Noir', 'Noir'),
   ]

   STATUT_CHOICES = [
       ('Libre', 'Libre'),
       ('Réservation', 'Réservé'),
       ('Commande', 'En commande'),
       ('Location', 'En cours de location'),
   ]
   item_name = models.CharField(max_length='100', blank=True, null=False, choices=type_choice)
   name = models.IntegerField(default='', blank=True, null=False)

class MyModel(models.Model):
  my_field = models.CharField(max_length=100)
"""


class Fournisseur(models.Model):
    fourni_id = models.AutoField(db_column='FOURNI_ID', primary_key=True)  # Field name made lowercase.
    fourni_nom = models.TextField(db_column='FOURNI_NOM', blank=True, null=True)  # Field name made lowercase.
    fourni_adresseposte = models.TextField(db_column='FOURNI_ADRESSEPOSTE', blank=True, null=True)
    # Field name made lowercase.
    fourni_tel = models.IntegerField(db_column='FOURNI_TEL', blank=True, null=True)  # Field name made lowercase.
    fourni_npa = models.IntegerField(db_column='FOURNI_NPA', blank=True, null=True)  # Field name made lowercase.
    fourni_desc = models.TextField(db_column='FOURNI_DESC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fournisseur'


class CommandeFournisseur(models.Model):
    commande_fourni_id = models.AutoField(db_column='COMMANDE_FOURNI_ID', primary_key=True)
    # Field name made lowercase.
    commadne_fourni_datecommande = models.IntegerField(db_column='COMMADNE_FOURNI_DATECOMMANDE', blank=True, null=True)
    # Field name made lowercase.
    commande_fourni_statut = models.TextField(db_column='COMMANDE_FOURNI_STATUT', blank=True, null=True)
    # Field name made lowercase.
    fourni_id = models.IntegerField(db_column='FOURNI_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Commande_fournisseur'


class Local(models.Model):
    local_id = models.AutoField(db_column='LOCAL_ID', primary_key=True)  # Field name made lowercase.
    local_nom = models.CharField(max_length=50, db_column='LOCAL_NOM', blank=True,
                                 null=True)  # Field name made lowercase.
    local_adresseposte = models.TextField(db_column='LOCAL_ADRESSEPOSTE', blank=True, null=True)
    # Field name made lowercase.
    local_npa = models.IntegerField(db_column='LOCAL_NPA', blank=True, null=True)  # Field name made lowercase.
    local_capacite = models.IntegerField(db_column='LOCAL_CAPACITE', blank=True, null=True)
    # Field name made lowercase.
    local_nb_velo = models.IntegerField(db_column='LOCAL_NB_VELO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Local'

    def __str__(self):
        return self.local_nom


class Donateur(models.Model):
    don_id = models.IntegerField(db_column='DON_ID', primary_key=True)  # Field name made lowercase.
    don_nom = models.TextField(db_column='DON_NOM', blank=True, null=True)  # Field name made lowercase.
    don_prenom = models.TextField(db_column='DON_PRENOM', blank=True, null=True)  # Field name made lowercase.
    don_adresseposte = models.TextField(db_column='DON_ADRESSEPOSTE', blank=True,
                                        null=True)  # Field name made lowercase.
    don_npa = models.IntegerField(db_column='DON_NPA', blank=True, null=True)  # Field name made lowercase.
    don_localite = models.TextField(db_column='DON_LOCALITE', blank=True, null=True)  # Field name made lowercase.
    don_tel = models.IntegerField(db_column='DON_TEL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Donateur'

    def __str__(self):
        return self.don_nom + " " + self.don_prenom


class PieceDeVelo(models.Model):
    piece_id = models.AutoField(db_column='PIECE_ID', primary_key=True)  # Field name made lowercase.
    piece_num = models.IntegerField(db_column='PIECE_NUM', blank=True, null=True)  # Field name made lowercase.
    piece_nom = models.IntegerField(db_column='PIECE_NOM', blank=True, null=True)  # Field name made lowercase.
    piece_type = models.TextField(db_column='PIECE_TYPE', blank=True, null=True)  # Field name made lowercase.
    piece_marque = models.TextField(db_column='PIECE_MARQUE', blank=True, null=True)  # Field name made lowercase.
    piece_nb = models.IntegerField(db_column='PIECE_NB', blank=True, null=True)  # Field name made lowercase.
    local_id = models.ForeignKey(Local, on_delete=models.CASCADE)
    fourni_id = models.ManyToManyField(Fournisseur)
    commandfourni_id = models.ManyToManyField(CommandeFournisseur)

    class Meta:
        managed = False
        db_table = 'Piece_de_velo'


class Velo(models.Model):
    fs = FileSystemStorage(location='media')

    MARQUE_CHOICES = [
        ('Ridley', 'Ridley'),
        ('Pinarello', 'Pinarello'),
        ('De Rosa', 'De Rosa'),
        ('Cannondale', 'Cannondale'),
        ('Specialized', 'Specialized'),
        ('Van Rysel', 'Van Rysel'),
        ('Eddardo Bianchi', 'Eddardo Bianchi'),
        ('Look', 'Look'),

    ]

    COULEUR_CHOICES = [
        ('Rouge', 'Rouge'),
        ('Vert', 'Vert'),
        ('Bleu', 'Bleue'),
        ('Jaune', 'Jaune'),
        ('Violet', 'Violet'),
        ('Rose', 'Rose'),
        ('Orange', 'Orange'),
        ('Cyan', 'Cyan'),
        ('Brun', 'Brun'),
        ('Noir', 'Noir'),
        ('Gris', 'Gris'),
        ('Nlanc', 'Blanc'),
    ]

    TYPE_CHOICES = [
        ('Vélo tout-terrain', 'VTT'),
        ('Vélo de route', 'Vélo de route'),
        ('BMX', 'BMX'),
    ]

    ETAT_CHOICES = [
        ('Cassé', 'Cassé'),
        ('Bon état', 'Bon état'),
    ]

    STATUT_CHOICES = [
        ('Libre', 'Libre'),
        ('Réservation', 'Réservé'),
        ('Commande', 'En commande'),
        ('Location', 'En cours de location'),
    ]

    # https://www.geeksforgeeks.org/imagefield-django-models/
    # https://stackoverflow.com/questions/63298721/how-to-update-imagefield-in-django
    def photo(self):
        return self.vel_photo

    vel_id = models.AutoField(db_column='VEL_ID', primary_key=True)  # Field name made lowercase.
    vel_num_cadre = models.IntegerField(db_column='VEL_NUM_CADRE', blank=False, null=True)  # Field name made lowercase.
    vel_nom = models.CharField(max_length=100, db_column='VEL_NOM', blank=False,
                               null=True)  # Field name made lowercase.
    vel_marque = models.CharField(choices=MARQUE_CHOICES, max_length=50, db_column='VEL_MARQUE', blank=False,
                                  null=True)  # Field name made lowercase.
    vel_couleur = models.CharField(choices=COULEUR_CHOICES, max_length=25, db_column='VEL_COULEUR', blank=False,
                                   null=True)  # Field name made lowercase.
    vel_type = models.CharField(choices=TYPE_CHOICES, max_length=50, db_column='VEL_TYPE', blank=False,
                                null=True)  # Field name made lowercase.

    vel_photo = models.ImageField(default='Aucune image', upload_to=FileSystemStorage, blank=True,
                                 max_length=100)  # Field name made lowercase.
    vel_statut = models.CharField(choices=STATUT_CHOICES, max_length=100, db_column='VEL_STATUT', blank=True,
                                  null=True)  # Field name made lowercase.
    vel_etat = models.CharField(choices=ETAT_CHOICES, max_length=100, db_column='VEL_ETAT', blank=False,
                                null=True)  # Field name made lowercase.
    vel_remarque = models.TextField(db_column='VEL_REMARQUE', blank=True, null=True)  # Field name made lowercase.
    vel_local = models.ForeignKey(Local, on_delete=models.CASCADE)
    vel_don = models.ForeignKey(Donateur, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.vel_nom

    class Meta:
        managed = False
        db_table = 'Velo'





class EstFourniPar(models.Model):
    fourni_id = models.IntegerField(db_column='FOURNI_ID', blank=True, null=True)  # Field name made lowercase.
    piece_id = models.IntegerField(db_column='PIECE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EST_FOURNI_PAR'


class PieceComandeFourni(models.Model):
    quantite_commande = models.IntegerField(db_column='QUANTITE_COMMANDE', blank=True, null=True)
    # Field name made lowercase.
    pcf_piece_id = models.IntegerField(db_column='PCF_PIECE_ID', blank=True, null=True)  # Field name made lowercase.
    pcf_commande_fourni_id = models.IntegerField(db_column='PCF_COMMANDE_FOURNI_ID', blank=True, null=True)

    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PIECE_COMANDE_FOURNI'


class Reparation_velos(models.Model):
    rep_id = models.IntegerField(db_column='REP_ID', blank=True, null=True)  # Field name made lowercase.
    rep_date_heure = models.DateField(auto_now=False, auto_now_add=False, db_column='REP_DATE_HEURE')  # Field name made lowercase.
    rep_desc = models.TextField(db_column='REP_DESC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EST_FOURNI_PAR'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FileField(models.Model):
    upload = models.FileField(upload_to='photo_velos/')
