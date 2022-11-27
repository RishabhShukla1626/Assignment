from django.db import models
import uuid
# Create your models here.

class Debates(models.Model):
    debate_title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True)
    vote_ratio = models.IntegerField(default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    objects = models.Manager()

    def __str__(self):
        return str(self.debate_title)


class Arguments(models.Model):
    debate = models.ForeignKey('Debates', on_delete=models.CASCADE)
    #author =
    argument = models.TextField()
    AGAINST_THE_TOPIC = 'AGAINST'
    SUPPORT_THE_TOPIC = 'SUPPORT'
    OPINION_ON_TOPIC_CHOICES = [
        (AGAINST_THE_TOPIC, 'Against'),
        (SUPPORT_THE_TOPIC, 'Support'),
    ]
    opinion = models.CharField(max_length=7,choices=OPINION_ON_TOPIC_CHOICES, default=AGAINST_THE_TOPIC)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()