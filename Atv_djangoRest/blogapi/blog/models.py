from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=80)
    suite = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=10)

    class Meta:
        ordering = ('zipcode',)
    
    def __str__(self):
        return self.zipcode

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    profile = models.ForeignKey(Profile, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name