from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    USERTYPE = (
        ('student', 'student'),
        ('counsellor', 'counsellor'),
    )
    STATUS = (
        ('approved', 'approved'),
        ('unapproved', 'unapproved'),
    )
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    profile_pic = models.ImageField(
        default="profile1.jpg", null=True, blank=True)
    google_picture = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=100, blank=True, choices=USERTYPE)
    user_status = models.CharField(max_length=100, blank=True, choices=STATUS)
    date_of_joining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class StudentExtendedProfile(models.Model):
    user = models.OneToOneField(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE
    )
    prepared_from = models.CharField(max_length=100, null=True, blank=True)
    rank = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_of_joining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class CounsellorExtendedProfile(models.Model):
    user = models.OneToOneField(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE
    )
    college = models.CharField(max_length=100, null=True, blank=True)
    from_yr = models.CharField(max_length=100, null=True, blank=True)
    to_yr = models.CharField(max_length=100, null=True, blank=True)
    current_job = models.CharField(max_length=100, null=True, blank=True)
    counselling_thought = models.TextField(null=True, blank=True)
    date_of_joining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    comment_to = models.ForeignKey(
        StudentExtendedProfile, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.commented_by) + ' comment ' + str(self.content)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


class Frequestly_Asked_Question(models.Model):
    question = models.CharField(max_length=500, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.question)


class Secret_Key(models.Model):
    key = models.CharField(max_length=500, null=True, blank=True)
    secret_key = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.key)
