from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail
from event.models import RSVP

@receiver(post_save, sender=RSVP)
def send_rsvp_cofirm_mail(sender, instance, created, **kwargs):
    if created:
        subject = f"RSVP confirmation for {instance.event.name}"
        message = f"Hello {instance.user.username}, \n\nyou have successfully RSVPed for the event: {instance.event.name}"
        recipient_list = [instance.user.email]

        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)