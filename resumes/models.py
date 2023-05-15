from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from auths.models import User
import datetime

# Create your models here.

class CreateResume(models.Model):
    name = models.CharField(max_length=225)
    slug = models.CharField(max_length=225)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Profile(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    fullname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    # Phone = PhoneNumberField(blank=True, region=None)
    gender = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=400, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100,  blank=True)
    region = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal = models.IntegerField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Links(models.Model):
    title = models.CharField(max_length=100)
    website = models.URLField(max_length=360)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


def __str__(self):
    return self.title


class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    employer = models.CharField(max_length=100)
    url = models.URLField()
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)
    website = models.URLField(max_length=300, blank=True)
    summary = models.CharField(max_length=400)
    present = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Education(models.Model):
    institute = models.CharField(max_length=400)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    url = models.URLField()
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField(blank=True)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.institute


class Awards(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    url = models.URLField()
    date = models.DateField()
    description = models.CharField(max_length=300)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    belong = models.ForeignKey(to=CreateResume, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


class Certifications(models.Model):
    certificate = models.CharField(max_length=100)
    Issuer = models.CharField(max_length=100)
    URL = models.URLField()
    Description = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    belong = models.ForeignKey(to=CreateResume, on_delete=models.CASCADE)

    def __str__(self):
        return self.certificate


class Publication(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


SELECT_LEVEL_CHOICE = [
    ('Beginner', 'Beginner'),
    ('Advanced', 'Advanced'),
    ('Expert', 'Expert')
]


class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=SELECT_LEVEL_CHOICE, default='Beginner')
    subSkill = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=SELECT_LEVEL_CHOICE, default='beginner')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Interests(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class VolunteerExperience(models.Model):
    organization = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)
    url = models.URLField(blank=True)
    summary = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.organization


class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    url = models.URLField()
    summary = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class References(models.Model):
    name = models.CharField(max_length=100, blank=True)
    relationship = models.CharField(max_length=100, blank=True)
    # Phone = PhoneNumberField(blank=True, region=None, )
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


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
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


