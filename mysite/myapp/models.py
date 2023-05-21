from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Vyrobce(models.Model):
    nazev = models.CharField(max_length=100, unique=True, verbose_name='Název výrobce', help_text='Zadej název výrobce motorek')
    datum = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False,verbose_name='Datum založení', help_text='Zadejte datum založení firmy')
    zeme = models.CharField(max_length=100, null=False, verbose_name='Země původu', help_text='Zadejte zemi, ze které firma pochází')

    class Meta:
        verbose_name = 'Výrobce'
        verbose_name_plural = 'Výrobci'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev

class Zbran(models.Model):
    MODELY_ZBRANI = [
        ("bodné", "Bodné"),
        ("střelné", "Střelné"),
        ("palné", "Palné"),
        ("automatické palné", "Automatické palné"),
        ("granátomety", "Granátomety"),
        ("raketové palné", "Raketové palné")
    ]
    MUNICE = [
        ("náboje", "Náboje"),
        ("rakety", "Rakety"),
        ("granáty", "Granáty"),
        ("jiné", "Jiné")
    ]

    nazev = models.CharField(max_length=50, null=False, blank=False,verbose_name='Název zbraně', help_text='Zadejte název zbraně')
    model_zbrane = models.CharField(max_length= 100, verbose_name='Model zbraně', help_text='Vyberte model zbraně', default='střelné', choices=MODELY_ZBRANI)
    cena = models.PositiveIntegerField(null=False, blank=False,verbose_name='Cena zbraně', help_text='Zadejte cenu zbraně')
    rok_vyroby = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Rok výroby', help_text='Zadejte rok výroby zbraně')
    palivo = models.CharField(max_length=100, verbose_name='Munice', help_text='Vyberte co používá zbraň za munici', choices=MUNICE)
    vyrobce = models.ForeignKey('Vyrobce', on_delete=models.CASCADE, verbose_name='Výrobce', help_text='Vyberte výrobce zbraně', default=0)
    obchod = models.ManyToManyField('Obchod', verbose_name='Ohchod', help_text='Vyberte obchod, ve kterém se zbraň nachází')

    class Meta:
        verbose_name = 'Zbraň'
        verbose_name_plural = 'Zbraně'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev
    
class Obchod(models.Model):
    nazev = models.CharField(max_length=100, null=False, blank=False, verbose_name='Název obchodu', help_text='Zadejte název obchodu')
    obec = models.CharField(max_length=100, null=False, blank=False, verbose_name='Obec', help_text='Zadejte obec, ve které se obchod nachází')
    ulice = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ulice', help_text='Zadejte ulici, ve které se obchod nachází')
    psc = models.PositiveIntegerField(null=False, blank=False, verbose_name='PSČ', help_text='Zadejte PSČ')
    
    class Meta:
        verbose_name = 'Obchod'
        verbose_name_plural = 'Obchody'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev
    
class Zamestnanec(models.Model):
    jmeno = models.CharField(max_length=50, null=False, blank=False, verbose_name='Jméno zaměstnance', help_text='Zadejte jméno zaměstnance')
    prijmeni = models.CharField(max_length=50, null=False, blank=False, verbose_name='Příjmení zaměstnance', help_text='Zadejte příjmení zaměstnance')
    obec = models.CharField(max_length=100, null=False, blank=False, verbose_name='Obec', help_text='Zadejte obec, ve které zaměstnanec bydlí')
    ulice = models.CharField(max_length=50, null=True, verbose_name='Ulice', help_text='Zadejte ulici, ve které zaměstnanec bydlí')
    cislo_popisne = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Číslo popisné', help_text='Zadejte číslo popisné')
    psc = models.PositiveIntegerField(null=False, blank=False, verbose_name='PSČ', help_text='Zadejte PSČ')
    telefon = models.CharField(max_length=20, verbose_name='Telefon', help_text='Zadejte telefonní číslo zaměstnance (včetně předvolby)',
                               validators=[RegexValidator(regex='^(\\+420)? ?[1-9][0-9]{2}( ?[0-9]{3}){2}$',message='Zadejte prosím platné telefonní číslo.')])
    fotka = models.ImageField(upload_to='zamestnanci', null=True, blank=True, verbose_name='Fotka zaměstnance', help_text='Nahrejte fotku zaměstnance')
    obchod = models.ForeignKey('Obchod', on_delete=models.CASCADE, verbose_name='Obchod', help_text='Vyberte obchod, ve kterém zaměstnanec pracuje', default=0)
    
    class Meta:
        verbose_name = 'Zaměstnanec'
        verbose_name_plural = 'Zaměstnanci'
        ordering = ['prijmeni', 'jmeno']

    def __str__(self):
        return f'{self.prijmeni}, {self.jmeno}'