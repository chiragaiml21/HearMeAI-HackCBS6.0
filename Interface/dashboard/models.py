from django.db import models

# Create your models here.

# =============================================== WORDS ======================================================

class Word(models.Model):
    alphabet = models.CharField(max_length=1, blank=True)
    word = models.CharField(max_length=50)
    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        
        if not self.alphabet:
            self.alphabet = self.word[0].upper() 
        super(Word, self).save(*args, **kwargs)

# =================================================  PHONEMES =================================================

class Phoneme(models.Model):
    key = models.CharField(max_length=5, blank=True)
    description = models.CharField(max_length=50)
    example = models.CharField(max_length=50)
    
    audio = models.FileField(upload_to='phonemes/', blank=True)
    
# ============================================= Sign Videos ====================================================

class SignVideo(models.Model):
    word = models.CharField(max_length=50)
    video = models.FileField(upload_to='sign_videos/', blank=True)