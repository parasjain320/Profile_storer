from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


# Create your models here.
TITLE_CHOICES = (
    ('Normal', 'Normal'),
    ('Manager', 'Manager')
)

user_sex = (
    ('MaLE', 'Male'),
    ('Female', 'Female')
)


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=160)
    type = models.CharField(max_length=7, choices=TITLE_CHOICES, default='Manager')
    phone = PhoneNumberField(null=True)
    gender = models.CharField(max_length=6, default='Male', choices=user_sex)
    hobbies = models.CharField(max_length=250)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):                                #will return search add by the user
        return '{}'.format(self.email)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})


    # def __str__(self):                                #will return search add by the user
    #     return '{}'.format(self.name)


    class Meta:
        verbose_name_plural = 'User'
