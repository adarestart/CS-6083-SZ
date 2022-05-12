from django.db import models

# Create your models here.


class IndividualInfo(models.Model):
    street = models.CharField(verbose_name="street", max_length=50)
    city = models.CharField(verbose_name="city", max_length=30)
    state = models.CharField(verbose_name="state", max_length=2)
    zipcode = models.CharField(verbose_name="zipcode", max_length=10)
    email = models.CharField(verbose_name="e-mail address", max_length=30)
    phone = models.CharField(verbose_name="phone number", max_length=10)
    FirstName = models.CharField(verbose_name="first name", max_length=25)
    MiddleName = models.CharField(verbose_name="middle name", max_length=25)
    LastName = models.CharField(verbose_name="last name", max_length=25)
    InsuranceCompany = models.CharField(verbose_name="insurance company", max_length=30)
    InsuranceNumber = models.CharField(verbose_name="insurance number", max_length=10)
    rate = models.DecimalField(verbose_name="Coupon Rate", max_digits=4, decimal_places=2, default=0)
    StartDate = models.DateField(verbose_name="Start Date")
    EndDate = models.DateField(verbose_name="End Date")

    class Meta:
        verbose_name = 'Indivisual Customer'

    def __str__(self):
        return self.FirstName+" "+self.LastName


class CorporationUser(models.Model):
    street = models.CharField(verbose_name="street", max_length=50)
    city = models.CharField(verbose_name="city", max_length=30)
    state = models.CharField(verbose_name="state", max_length=2)
    zipcode = models.CharField(verbose_name="zipcode", max_length=10)
    email = models.CharField(verbose_name="e-mail address", max_length=30)
    phone = models.CharField(verbose_name="phone number", max_length=10)
    employ_id = models.CharField(verbose_name="employ id", max_length=10)
    corporation_choices = (
        (1, "D&G Tax Law"),
        (2, "The Acrobatic Accountants LLC"),
        (3, "Cafe Msica"),
        (4, "Artisan Recording"),
        (5, "New York Man"),
        (6, "Dreamlike Moustaches"),
        (7, "Swift River Sports"),
        (8, "The Big Apple Cocktail Company"),
        (9, "Pouring Palaces"),
        (10, "Schmalzy Pet"),
    )
    corporation_name = models.SmallIntegerField(verbose_name="corporation name", choices=corporation_choices)
    rate = models.DecimalField(verbose_name="Coupon Rate", max_digits=4, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Corporation Customer'

    def __str__(self):
        return str(self.corporation_name)