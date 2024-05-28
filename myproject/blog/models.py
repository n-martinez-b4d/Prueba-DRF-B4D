from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator, MaxValueValidator, MinValueValidator

regex = r'^[\w\s!@#$%^&*(),.?":{}|<>-]*$'
min_val = 10

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, validators=[MinLengthValidator(min_val), RegexValidator(regex=regex)])
    content = models.TextField(validators=[MinLengthValidator(min_val), RegexValidator(regex=regex)])
    created_at = models.DateTimeField(default=timezone.now, validators=[MinValueValidator(limit_value=timezone.now() - timezone.timedelta(days=365*20)), MaxValueValidator(limit_value=timezone.now())])
