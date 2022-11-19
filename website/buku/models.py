from django.db import models

# Create your models here.

class Kategori(models.Model):
    Kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.Kategori

class Post(models.Model):
    judul = models.CharField(max_length=255)
    sinopsis = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.judul
