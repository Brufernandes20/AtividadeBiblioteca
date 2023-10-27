from django.db import models
 
class Genres(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

        class meta:
            verbose_name = 'Gender'
            verbose_name_plural = 'Genres'

class Books(models.Model):

    cod = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    gender = models.ForeignKey(Genres, on_delete=models.CASCADE)
    picture = models.ImageField(blank=False)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()
    qtd = models.IntegerField()
    in_stock = models.BooleanField(default=False)
   

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'