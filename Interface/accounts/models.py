from django.db import models

from django.contrib.auth.models import User

# ============================== BADGES =================================


class Badge(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='badges/', blank=True, null=True)
    points_required = models.PositiveIntegerField()

    def title(self):
        return self.image.name.split('/')[-1]

# =============================== STUDENT Model ===============================


class Student(User):

    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Prefer Not To Say", "Prefer Not To Say")
    )

    phone_number = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=20, choices=gender_choices, blank=True, null=True)
    address = models.TextField(blank=True, null=True, default="---")

    points = models.PositiveIntegerField(default=0)

    badges = models.ManyToManyField(Badge, blank=True)
    avatar = models.ForeignKey(
        'Avatar', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    # calculate the rank of the student on the basis of the points

    def rank(self):
        students = Student.objects.all().order_by("-points")
        for index, student in enumerate(students):
            if student == self:
                return index + 1
        return 0


# =============================== AVATARS =================================

class Avatar(models.Model):
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    # title of the next avatar should be as "avatar-<id>.png"

    def title(self):
        return self.image.name.split('/')[-1]
