# Generated by Django 4.0.9 on 2023-04-23 21:31

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
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
                ('user_type', models.CharField(choices=[('CL', 'Client'), ('TR', 'Trainer')], default='CL', max_length=2)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('current_address', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('certifications', models.CharField(blank=True, max_length=255, null=True)),
                ('experience_years', models.PositiveIntegerField(blank=True, null=True)),
                ('previous_work_experience', models.TextField(blank=True, null=True)),
                ('fitness_specialization', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video_url', models.URLField(blank=True, null=True)),
                ('plan_url', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('views', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('rating', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('category', models.CharField(blank=True, choices=[('CARDIO', 'Cardio'), ('STRENGTH', 'Strength'), ('FLEXIBILITY', 'Flexibility'), ('BALANCE', 'Balance')], max_length=255, null=True)),
                ('level', models.CharField(blank=True, choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], max_length=255, null=True)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='workout_videos/')),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('calories', models.IntegerField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutsAssigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.workouts')),
            ],
        ),
        migrations.CreateModel(
            name='IntakeForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('preferred_workout_category', models.CharField(blank=True, choices=[('CARDIO', 'Cardio'), ('STRENGTH', 'Strength'), ('FLEXIBILITY', 'Flexibility'), ('BALANCE', 'Balance')], max_length=20, null=True)),
                ('preferred_workout_level', models.CharField(blank=True, choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('meals', models.TextField(blank=True, null=True)),
                ('sleep_cycle', models.TextField(blank=True, null=True)),
                ('progress_metrics', models.TextField(blank=True, null=True)),
                ('calories_burnt', models.IntegerField(blank=True, null=True)),
                ('goal_progress', models.FloatField(blank=True, null=True)),
                ('completed_workouts', models.ManyToManyField(blank=True, null=True, related_name='completed_workout', to='core.workoutsassigned')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workouts', models.ManyToManyField(blank=True, null=True, related_name='assigned_workouts', to='core.workoutsassigned')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
