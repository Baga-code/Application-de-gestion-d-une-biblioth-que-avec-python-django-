# Generated by Django 5.1 on 2024-08-16 10:00

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_carte', models.CharField(max_length=20, unique=True, verbose_name='Numéro de carte')),
            ],
            options={
                'verbose_name': 'Emprunteur',
                'verbose_name_plural': 'Emprunteurs',
            },
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200, unique=True, verbose_name='Titre')),
                ('auteur', models.CharField(max_length=100, verbose_name='Auteur')),
                ('date_publication', models.DateField(verbose_name='Date de publication')),
                ('nombre_total', models.IntegerField(default=1, verbose_name='Nombre total de copies')),
            ],
            options={
                'verbose_name': 'Livre',
                'verbose_name_plural': 'Livres',
            },
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(auto_now_add=True, verbose_name="Date d'emprunt")),
                ('date_retour', models.DateField(blank=True, null=True, verbose_name='Date de retour')),
                ('retourne', models.BooleanField(default=False, verbose_name='Retourné')),
                ('emprunteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblotheque.emprunteur', verbose_name='Emprunteur')),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblotheque.livre', verbose_name='Livre')),
            ],
            options={
                'verbose_name': 'Emprunt',
                'verbose_name_plural': 'Emprunts',
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('prenom', models.CharField(max_length=50, verbose_name='Prénom')),
                ('numero', models.CharField(max_length=15, unique=True, verbose_name='Numéro de téléphone')),
                ('groups', models.ManyToManyField(blank=True, related_name='utilisateur_set', to='auth.group', verbose_name='Groupes')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='utilisateur_set', to='auth.permission', verbose_name='Permissions utilisateur')),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='emprunteur',
            name='utilisateur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblotheque.utilisateur', verbose_name='Utilisateur'),
        ),
    ]