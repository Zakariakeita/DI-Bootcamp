# Generated by Django 4.1.4 on 2022-12-21 14:03

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnneeScolaire",
            fields=[
                (
                    "idAnneeScolaire",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("intituleAnneeScolaire", models.CharField(max_length=50)),
                ("etat", models.BooleanField(default=False)),
                ("supprimer", models.BooleanField(default=False)),
                ("dateSuppression", models.DateTimeField(null=True)),
                ("dateCreation", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Classe",
            fields=[
                ("idClasse", models.AutoField(primary_key=True, serialize=False)),
                ("intituleClasse", models.CharField(max_length=100)),
                ("supprimer", models.BooleanField(default=False)),
                ("dateSuppression", models.DateTimeField(null=True)),
                ("dateCreation", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Eleve",
            fields=[
                ("matricule", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "profil",
                    models.ImageField(default="default.png", upload_to="profil"),
                ),
                ("nom", models.CharField(max_length=70)),
                ("prenom", models.CharField(max_length=90)),
                ("dateNaissance", models.DateField()),
                ("lieuNaissance", models.CharField(max_length=90)),
                ("genre", models.CharField(max_length=10)),
                ("nationalite", models.CharField(max_length=20)),
                ("adresse", models.CharField(max_length=40)),
                ("nomTuteur", models.CharField(max_length=70)),
                ("prenomTuteur", models.CharField(max_length=90)),
                ("contactTuteur", models.CharField(max_length=18)),
                ("dateCreation", models.DateTimeField()),
                ("supprimer", models.BooleanField(default=False)),
                ("dateSuppression", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Matiere",
            fields=[
                ("idMatiere", models.AutoField(primary_key=True, serialize=False)),
                ("intituleMatiere", models.CharField(max_length=200)),
                ("supprimer", models.BooleanField(default=False)),
                ("dateSuppression", models.DateTimeField(null=True)),
                ("dateCreation", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Inscription",
            fields=[
                ("idInscription", models.AutoField(primary_key=True, serialize=False)),
                ("dateInscription", models.DateTimeField()),
                ("supprimer", models.BooleanField(default=False)),
                ("dateSuppression", models.DateTimeField(null=True)),
                (
                    "idAnneeScolaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecoges.anneescolaire",
                    ),
                ),
                (
                    "idClasse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecoges.classe"
                    ),
                ),
                (
                    "matricule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecoges.eleve"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "profil",
                    models.ImageField(default="default.png", upload_to="profil"),
                ),
                ("supprimer", models.BooleanField(default=False)),
                ("role", models.CharField(default="Admin", max_length=20)),
                ("dateSuppression", models.DateTimeField(null=True)),
                ("dateCreation", models.DateTimeField()),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
    ]