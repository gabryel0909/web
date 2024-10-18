from django.db import models

# Create your models here.

class Posts(models.Model):
    titulo=models.CharField(max_length=50)
    description = models.TextField()
    imagem=models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.title
    
    class Meta:  
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']