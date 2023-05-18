from django.contrib.auth.models import Group
from django.db import models

from apps.auth_app.models.base_user import User
from apps.auth_app.models.managers import JobSeekerManager, EmployerManager


class JobSeeker(User):
    objects = JobSeekerManager()
    base_type = User.Types.JOBSEEKER

    class Meta:
        proxy = True


class Employer(User):
    objects = EmployerManager()
    base_type = User.Types.EMPLOYER

    def save(self, *args, **kwargs):
        employer: Employer = super().save(*args, **kwargs)
        owner_group = Group.objects.get(name="Owner")
        employer.groups.add(owner_group)

    class Meta:
        proxy = True
        permissions = [
            ("add_CV", "Can upload CV"),
        ]


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="jobseeker_profile")
    cv = models.FileField(upload_to="cv", blank=True, null=True, default=None)
    jobseeker_id = models.IntegerField(null=True, blank=True)
    skills = models.ManyToManyField("job_board.PositionType")


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employer_profile")
    has_company = models.BooleanField(default=False)
    owner_id = models.IntegerField(null=True, blank=True)
