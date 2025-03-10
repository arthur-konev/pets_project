from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model() 



class PetsTypes(models.Model):
    name = models.CharField(
        max_length=64, unique=True, blank=False, null=False, verbose_name="Название"
    )
    note = models.TextField(blank=True, null=True, verbose_name="Заметки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип домашнего животного"
        verbose_name_plural = "Типы домашних животных"


class Breeds(models.Model):
    type = models.ForeignKey(PetsTypes, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=64, unique=True, blank=False, null=False, verbose_name="Название"
    )
    note = models.TextField(blank=True, null=True, verbose_name="Заметки")

    def __str__(self):
        return f"{self.name} ({self.type})"

    class Meta:
        verbose_name = "Тип породы"
        verbose_name_plural = "Типы пород"


class PetsOwners(models.Model):
    name = models.CharField(
        max_length=128, unique=True, blank=False, null=False, verbose_name="Имя"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Владельцы"
        verbose_name_plural = "Владелец"


class Pets(models.Model):
    breed = models.ForeignKey(Breeds, on_delete=models.CASCADE)
    owner = models.ForeignKey(PetsOwners, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name="Имя")
    sex = models.BooleanField(null=True)
    birth = models.DateField(null=True)  # если не знаем дату рождения
    color = models.CharField(max_length=64)
    note = models.TextField(blank=True, null=True, verbose_name="Заметки")

    @property
    def owner_name(self):
        return f"{self.owner}"
    
    @property
    def breed_name(self):
        return str(self.breed)
    
    @property
    def sex_name(self):
        if self.sex:
            return "Жен."
        elif self.sex is None:
            return "Пол не указан"
        else:
            return "Муж."
    

    def __str__(self):
        return f'{self.breed} по имени "{self.name}"'

    class Meta:
        verbose_name = "Питомцы"
        verbose_name_plural = "Питомец"
