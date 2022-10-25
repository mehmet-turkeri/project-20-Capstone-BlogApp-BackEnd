from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

# Post kategorileri tablosu / Tabloda gorunen isim 'Categories' / name'e gore sirala
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name

# Post tablosu / Post durumu-taslakmi, yayinmi / Post fields / title'a gore sirala / yorum, like, goruntuleme tespit
class Post(models.Model):
    STATUS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
  
    title = models.CharField(max_length=150)    
    content = models.TextField(max_length=6000)
    image = models.ImageField(upload_to=user_directory_path, default='django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='d')
    slug = models.SlugField(blank=True, null=True)
   
    def __str__(self):
        return self.title
    
    
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def view_count(self):
        return self.postview_set.all().count()
    
    def like_count(self):
        return self.like_set.all().count()
    
    def comments(self):
        return self.comment_set.all()

# Yorumlar Tablosu / username'e gore sirala
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username

# Like(begenme) Tablosu / username'e gore sirala    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Kim kac kez goruntuledi tablosu / username'e gore sirala    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
