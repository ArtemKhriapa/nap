from django.db import models
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# class SentEmail(models.Model):
#     user = models.ForeignKey(User)
#     text = models.TextField()
#     datetime = models.DateTimeField(auto_now_add=True)
#
#FIXME: include this in RegTry!

class EmailLog(models.Model):
    mail_sent_at = models.DateTimeField(auto_now_add=True)
    mail_to = models.EmailField()
    # user = models.ForeignKey(User, null=True, related_name='email_log')
    text = models.TextField(null=True, blank=True)

    def sendmail(self,reason):
        email = EmailMessage(reason, self.text, to=[self.mail_to])
        email.send()
        print('mail to ',self.mail_to, 'in', reason)