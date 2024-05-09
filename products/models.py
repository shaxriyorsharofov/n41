from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='media/default_book_img.png', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title





