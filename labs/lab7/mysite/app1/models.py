from django.db import models
#Задание 2. Приложение должно содержать не менее трех связанных моделей (таблиц).
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
class Policy(models.Model):
    policy_number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
class Claim(models.Model):
    claim_number = models.CharField(max_length=50)
    date_filed = models.DateField()
    description = models.TextField()
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)