from django.db import models


class College(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    college_email = models.CharField(max_length=300, null=False, blank=False)
    form_donate = models.URLField(max_length=300, null=False, blank=False)
    form_receive = models.URLField(max_length=300, null=False, blank=False)
    college_ext = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
