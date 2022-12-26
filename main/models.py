from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=200)
    Category_image=models.ImageField(upload_to='imgs/')
    
    def __str__(self):
        return self.title
    
class News(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.title