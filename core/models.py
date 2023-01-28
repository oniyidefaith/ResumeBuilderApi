from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cvbuilder.models import User


# Create your models here.

class CreateResume(models.Model):
    name = models.CharField(max_length=225)
    slug = models.CharField(max_length=225)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Profile(models.Model):
    Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Full_Name = models.CharField(max_length=100)
    Date = models.DateField()
    email = models.EmailField(max_length=254)
    Phone = PhoneNumberField(blank=True, region=None)
    Gender = models.CharField(max_length=300)
    Description = models.CharField(max_length=100)
    Summary = models.CharField(max_length=400)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100, )
    Region = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Postal = models.IntegerField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Image


class Links(models.Model):
    Title = models.CharField(max_length=100)
    Website = models.URLField(max_length=360)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


def __str__(self):
    return self.Title


class WorkExperience(models.Model):
    Title = models.CharField(max_length=200)
    Position = models.CharField(max_length=200)
    Employer = models.CharField(max_length=100)
    Url = models.URLField()
    StartDate = models.DateField()
    EndDate = models.DateField(blank=True)
    Website = models.URLField(max_length=300, blank=True)
    Summary = models.CharField(max_length=400)
    present = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


class Education(models.Model):
    Institute = models.CharField(max_length=400)
    Degree = models.CharField(max_length=200)
    School = models.CharField(max_length=200)
    URL = models.URLField()
    City = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    StartDate = models.DateField()
    EndDate = models.DateField(blank=True)
    Description = models.CharField(max_length=500)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Institute


class Awards(models.Model):
    Title = models.CharField(max_length=200)
    Issuer = models.CharField(max_length=200)
    URL = models.URLField()
    Date = models.DateField()
    Description = models.CharField(max_length=300)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


class Certifications(models.Model):
    certificate = models.CharField(max_length=100)
    Issuer = models.CharField(max_length=100)
    URL = models.URLField()
    Description = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.certificate


class Publication(models.Model):
    Title = models.CharField(max_length=100)
    URL = models.URLField(max_length=100)
    Name = models.CharField(max_length=100)
    Date = models.DateField()
    Description = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


SELECT_LEVEL_CHOICE = [
    ('Beginner', 'Beginner'),
    ('Advanced', 'Advanced'),
    ('Expert', 'Expert')
]


class Skills(models.Model):
    Name = models.CharField(max_length=100)
    Level = models.CharField(max_length=50, choices=SELECT_LEVEL_CHOICE, default='Beginner')
    SubSkill = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Languages(models.Model):
    Name = models.CharField(max_length=100)
    Level = models.CharField(max_length=50, choices=SELECT_LEVEL_CHOICE, default='beginner')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Interests(models.Model):
    Name = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class VolunteerExperience(models.Model):
    Organization = models.CharField(max_length=100, blank=True)
    Position = models.CharField(max_length=100, blank=True)
    StartDate = models.DateField(blank=True)
    EndDate = models.DateField(blank=True)
    URL = models.URLField(blank=True)
    Summary = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.Organization


class Projects(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    URL = models.URLField()
    Summary = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class References(models.Model):
    Name = models.CharField(max_length=100, blank=True)
    Relationship = models.CharField(max_length=100, blank=True)
    Phone = PhoneNumberField(blank=True, region=None, )
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.Name


# Creating Api end points for a cover letter system

class PersonalDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    postal = models.IntegerField(blank=True)
    city = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class RecipientInfo(models.Model):
    contact_person = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postal = models.IntegerField()
    city = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_person


class DateSubject(models.Model):
    date = models.DateField()
    application_model = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.date


class Introduction(models.Model):
    text = models.TextField(max_length=600)
    person = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=120, blank=True)
    magazine = models.CharField(max_length=100, blank=True)
    website_name = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class CurSituation(models.Model):
    text = models.TextField(max_length=600)
    position = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=120)
    city = models.CharField(max_length=100, blank=True)
    responsibility = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Motivation(models.Model):
    text = models.TextField(max_length=600)
    position = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=120)
    city = models.CharField(max_length=100, blank=True)
    responsibility = models.CharField(max_length=100, blank=True)
    personal_description = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Closing(models.Model):
    text = models.TextField(max_length=600)
    position = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200)
    Phone = PhoneNumberField(blank=True, region=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.position
