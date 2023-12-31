# Generated by Django 4.2.2 on 2023-07-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0002_match_team_1_match_team_1_score_match_team_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='rank.team')),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1_score', models.IntegerField()),
                ('team_2_score', models.IntegerField()),
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rank.match')),
            ],
        ),
    ]
