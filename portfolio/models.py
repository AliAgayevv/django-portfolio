from django.db import models

class TechStack(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='tech_icons/', null=True, blank=True)
    proficiency = models.IntegerField(default=50)  # 0-100 arası
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Texnologiya'
        verbose_name_plural = 'Texnologiyalar'


class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('instagram', 'Instagram'),
        ('medium', 'Medium'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(max_length=50, help_text="FontAwesome class adı")
    
    def __str__(self):
        return self.platform
    
    class Meta:
        verbose_name = 'Sosial Media'
        verbose_name_plural = 'Sosial Medialar'


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=300)
    detailed_description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.ManyToManyField(TechStack)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    created_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Proyekt'
        verbose_name_plural = 'Proyektlər'
        ordering = ['-created_date']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ad')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    message = models.TextField(verbose_name='Mesaj')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d.%m.%Y')}"
    
    class Meta:
        verbose_name = 'Əlaqə Mesajı'
        verbose_name_plural = 'Əlaqə Mesajları'
        ordering = ['-created_at']


class AboutMe(models.Model):
    photo = models.ImageField(upload_to='about/')
    bio_text = models.TextField()
    cv_file = models.FileField(upload_to='cv/')
    years_experience = models.IntegerField(default=0)
    location = models.CharField(max_length=100, default='Bakı, Azərbaycan')
    
    def __str__(self):
        return "Haqqımda"
    
    class Meta:
        verbose_name = 'Haqqımda'
        verbose_name_plural = 'Haqqımda'