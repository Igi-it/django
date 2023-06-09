# Generated by Django 4.2.1 on 2023-05-21 13:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obchod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název obchodu', max_length=100, verbose_name='Název obchodu')),
                ('obec', models.CharField(help_text='Zadejte obec, ve které se obchod nachází', max_length=100, verbose_name='Obec')),
                ('ulice', models.CharField(help_text='Zadejte ulici, ve které se obchod nachází', max_length=50, verbose_name='Ulice')),
                ('psc', models.PositiveIntegerField(help_text='Zadejte PSČ', verbose_name='PSČ')),
            ],
            options={
                'verbose_name': 'Obchod',
                'verbose_name_plural': 'Obchody',
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Vyrobce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadej název výrobce motorek', max_length=100, unique=True, verbose_name='Název výrobce')),
                ('datum', models.DateField(help_text='Zadejte datum založení firmy', verbose_name='Datum založení')),
                ('zeme', models.CharField(help_text='Zadejte zemi, ze které firma pochází', max_length=100, verbose_name='Země původu')),
            ],
            options={
                'verbose_name': 'Výrobce',
                'verbose_name_plural': 'Výrobci',
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Zbran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název zbraně', max_length=50, verbose_name='Název zbraně')),
                ('model_zbrane', models.CharField(choices=[('bodné', 'Bodné'), ('střelné', 'Střelné'), ('palné', 'Palné'), ('automatické palné', 'Automatické palné'), ('granátomety', 'Granátomety'), ('raketové palné', 'Raketové palné')], default='střelné', help_text='Vyberte model zbraně', max_length=100, verbose_name='Model zbraně')),
                ('cena', models.PositiveIntegerField(help_text='Zadejte cenu zbraně', verbose_name='Cena zbraně')),
                ('rok_vyroby', models.PositiveSmallIntegerField(help_text='Zadejte rok výroby zbraně', verbose_name='Rok výroby')),
                ('palivo', models.CharField(choices=[('náboje', 'Náboje'), ('rakety', 'Rakety'), ('granáty', 'Granáty'), ('jiné', 'Jiné')], help_text='Vyberte co používá zbraň za munici', max_length=100, verbose_name='Munice')),
                ('obchod', models.ManyToManyField(help_text='Vyberte obchod, ve kterém se zbraň nachází', to='myapp.obchod', verbose_name='Ohchod')),
                ('vyrobce', models.ForeignKey(default=0, help_text='Vyberte výrobce zbraně', on_delete=django.db.models.deletion.CASCADE, to='myapp.vyrobce', verbose_name='Výrobce')),
            ],
            options={
                'verbose_name': 'Zbraň',
                'verbose_name_plural': 'Zbraňe',
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Zamestnanec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(help_text='Zadejte jméno zaměstnance', max_length=50, verbose_name='Jméno zaměstnance')),
                ('prijmeni', models.CharField(help_text='Zadejte příjmení zaměstnance', max_length=50, verbose_name='Příjmení zaměstnance')),
                ('obec', models.CharField(help_text='Zadejte obec, ve které zaměstnanec bydlí', max_length=100, verbose_name='Obec')),
                ('ulice', models.CharField(help_text='Zadejte ulici, ve které zaměstnanec bydlí', max_length=50, null=True, verbose_name='Ulice')),
                ('cislo_popisne', models.PositiveSmallIntegerField(help_text='Zadejte číslo popisné', verbose_name='Číslo popisné')),
                ('psc', models.PositiveIntegerField(help_text='Zadejte PSČ', verbose_name='PSČ')),
                ('telefon', models.CharField(help_text='Zadejte telefonní číslo zaměstnance (včetně předvolby)', max_length=20, validators=[django.core.validators.RegexValidator(message='Zadejte prosím platné telefonní číslo.', regex='^(\\+420)? ?[1-9][0-9]{2}( ?[0-9]{3}){2}$')], verbose_name='Telefon')),
                ('fotka', models.ImageField(blank=True, help_text='Nahrejte fotku zaměstnance', null=True, upload_to='zamestnanci', verbose_name='Fotka zaměstnance')),
                ('obchod', models.ForeignKey(default=0, help_text='Vyberte obchod, ve kterém zaměstnanec pracuje', on_delete=django.db.models.deletion.CASCADE, to='myapp.obchod', verbose_name='Obchod')),
            ],
            options={
                'verbose_name': 'Zaměstnanec',
                'verbose_name_plural': 'Zaměstnanci',
                'ordering': ['prijmeni', 'jmeno'],
            },
        ),
    ]
