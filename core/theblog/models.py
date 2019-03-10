from django.db import models
from django.urls import reverse

class Blog(models.Model):
    """Model representing a blog"""
    title = models.CharField(max_length=200)

    # Foreign Key used because blog can only have one author/blogger but bloggers can have multiple blogs
    # Blogger as a string rather than object because it hasn't been declaryed yet in the file
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief summary of the blog post')

    date_of_blog = models.DateField(null=True, blank=True)

    post = models.TextField(max_length=5000, help_text='Start your blog post here', null=True)

    class Meta:
        ordering = ['-date_of_blog']

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a more details about this blog."""
        return reverse('blog-detail', args=[str(self.id)])



class Blogger(models.Model):
    """Model representing a blog author."""
    name = models.CharField(max_length=200, help_text='Enter your username')
    location = models.CharField(max_length=100, help_text='Enter your location', null=True)
    bio = models.CharField(max_length=1000, help_text='Tell us about yourself', null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular blogger instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name