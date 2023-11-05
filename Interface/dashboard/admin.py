from django.contrib import admin
from .models import Word, Phoneme, SignVideo

# Register your models here.

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('alphabet', 'word')
    list_filter = ('alphabet',)
    search_fields = ('alphabet', 'word')
    ordering = ('alphabet', 'word')
    readonly_fields = ('alphabet',)
    
# ============================ PHONEMES ================================

@admin.register(Phoneme)
class PhonemeAdmin(admin.ModelAdmin):
    list_display = ('key', 'description', 'example')
    list_filter = ('key',)
    search_fields = ('key', 'description', 'example')
    ordering = ('key', 'description', 'example')

# ============================ SIGN VIDEOS ================================

@admin.register(SignVideo)
class SignVideoAdmin(admin.ModelAdmin):
    list_display = ('word', 'video')
    list_filter = ('word',)
    search_fields = ('word', 'video')
    ordering = ('word', 'video')