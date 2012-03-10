from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.conf import settings
import re, sha, random
from django.contrib.sites.models import Site
from django.template import Context, loader

class RegistrationManager(models.Manager):
    
    def activate_user(self, activationKey):
        if re.match('[a-f0-9]{40}', activationKey):
            try:
                user_profile = self.get(activation_key = activationKey)
            except self.model.DoesNotExist:
                return False
        
            if user_profile.keyValidation:
                user = user_profile.user
                user.is_active = True
                user.save()
                return user
        return False
    
    
    def create_inactive_user(self, username, password, email, send_email=True):

        # Create the user.
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = False
        new_user.save()
        
        # Generate a salted SHA1 hash to use as a key.
        salt = sha.new(str(random.random())).hexdigest()[:5]
        activation_key = sha.new(salt+new_user.username).hexdigest()
        
        # And finally create the profile.
        new_profile = self.create(user=new_user,
                                  activation_key=activation_key)
        
        if send_email:
            from django.core.mail import send_mail
            subject = "Activate your new account at %s" % settings.SITE_URL
            message_template = loader.get_template('activation_email.txt')
            message_context = Context({ 'site_url': 'http://%s' % settings.SITE_URL,
                                        'activation_key': activation_key,
                                        'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS })
            message = message_template.render(message_context)
            print settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, settings.EMAIL_HOST, [new_user.email])
        return new_user

def delete_expired_users(self):
    for profile in self.all():
        if profile.activation_key_expired():
            user = profile.user
            if not user.is_active:
                user.delete() # Removing the User will remove the RegistrationProfile, too.

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique = True)
    activation_key = models.CharField(max_length = 40)
    key_date = models.DateTimeField()
    objects = RegistrationManager()
    
    class Admin:
        pass
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.key_date = datetime.now()
        super(UserProfile, self).save(*args, **kwargs)
        
    def __str__(self):
        return "User : %s" % self.user.username
    
    def keyValidation(self):
        'check whether activation key has expired or not'
        delta = timedelta(days = settings.ACCOUNT_ACITIVATION_DAYS)
        return self.key_date + delta >= datetime.now() 
        
