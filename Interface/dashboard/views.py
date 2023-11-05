from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .phonemes import segment_sentence_to_phonemes

from random import choices

from django.http import JsonResponse
from .models import Word, Phoneme, SignVideo

from accounts.models import Student, Avatar, Badge


# ===========================================================================================================================
# =================================================== EXTRA FUNCTIONS =======================================================
# ===========================================================================================================================

def remaining_points(student):
    remaining_points = 0
    for badge in Badge.objects.all():
        if student.points < badge.points_required:
            remaining_points = badge.points_required - student.points
            break
    return remaining_points


def remaining_points_in_percentage(student):
    remaining_points = 0
    for badge in Badge.objects.all():
        if student.points < badge.points_required:
            remaining_points = badge.points_required - student.points
            break
    return 100 - int((remaining_points / 1000) * 100)
# ====================================== HOME ================================


@login_required(login_url='login')
def index(request):

    student = Student.objects.get(id=request.user.id)
    total_badges = Badge.objects.all().count()

    # fetch those badges which student has not earned yet
    rest_badges = Badge.objects.all()
    for badge in rest_badges:
        if badge in student.badges.all():
            rest_badges = rest_badges.exclude(id=badge.id)

    parameters = {
        'student': student,
        'total_badges': total_badges,
        'rest_badges': rest_badges,
        'remaining_points': remaining_points(student),
        'remaining_points_in_percentage': remaining_points_in_percentage(student),
    }

    return render(request, "dashboard/index.html", parameters)

# ====================================== TRAININGS ============================


@login_required(login_url='login')
def trainings(request):

    student = Student.objects.get(id=request.user.id)

    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
    }

    return render(request, "dashboard/training/choice.html", parameters)


# ======================================== HAND SIGN TRAINING ==================


def hand_sign_training(request):

    student = Student.objects.get(id=request.user.id)
    random_10_words = choices(Word.objects.all(), k=10)
    
    sign_words = SignVideo.objects.all()

    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
        
        "words": random_10_words,
        "sign_words": sign_words,
    }

    return render(request, "dashboard/training/hand_sign.html", parameters)

def play_sign_video(request, id):
    student = Student.objects.get(id=request.user.id)
    sign_video = SignVideo.objects.get(id=id)

    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
        
        "sign_video": sign_video,
    }

    return render(request, "dashboard/training/hand_sign.html", parameters)


# ======================================== Get words by alphabet ==================


def get_words_by_character(request):
    
    student = Student.objects.get(id=request.user.id)

    random_10_words = choices(Word.objects.all(), k=10)
    
    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
        
        "words": random_10_words,
    }
    
    return render(request,  "dashboard/training/hand_sign.html", parameters)

# ============================================= SELECTED WORD ===================


def selected_word(request, id):
    student = Student.objects.get(id=request.user.id)
    word = Word.objects.get(id=id)


    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
        
        "word": word,
    }

    return render(request, "dashboard/training/hand_sign.html", parameters)


# ===================================== SOUNDS TRAINING ========================

def sounds_training(request):
    
    student = Student.objects.get(id=request.user.id)
    
    words = choices(Word.objects.all(), k=1)

    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
        
        "words": words,
    }

    return render(request, "dashboard/training/sounds_training.html", parameters)

def get_word(request, id):
    student = Student.objects.get(id=request.user.id)
    word = Word.objects.get(id=id).word
    
    print(word)
    
    result = segment_sentence_to_phonemes(word)
    
    phonemes = []
    
    for pair in result:
        phoenem = Phoneme.objects.get(key=pair[1])
        phonemes.append(phoenem)
    
    

    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
        
        "word": word,
        "phonemes": phonemes,
    }

    return render(request, "dashboard/training/sounds_training.html", parameters)

# ===================================== STATISTICS ==========================


@login_required(login_url='login')
def statistics(request):
    student = Student.objects.get(id=request.user.id)

    top_students = Student.objects.all().order_by("-points")[:3]
    rest_students = Student.objects.all().order_by("-points")[3:]

    parameters = {
        'student': student,
        "top_students": top_students,
        'total_badges': Badge.objects.all().count(),
        "rest_students": rest_students,
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
        'avatars': Avatar.objects.all()[:3],
    }

    return render(request, "dashboard/statistics.html", parameters)

# ====================================== PLAY ================================


@login_required(login_url='login')
def play_games(request):

    student = Student.objects.get(id=request.user.id)

    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),

    }

    return render(request, "dashboard/games/index.html", parameters)

# ====================================== PROFILE =============================


@login_required(login_url='login')
def my_profile(request):

    student = Student.objects.get(id=request.user.id)

    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),

    }

    return render(request, "dashboard/profile.html", parameters)

# ===================================== UPDATE PROFILE =========================


def update_profile(request):

    student = Student.objects.get(id=request.user.id)
    all_avatars = Avatar.objects.all()
    
    if request.method == "POST":
        student.first_name = request.POST.get("f_name")
        student.last_name = request.POST.get("l_name")
        student.gender = request.POST.get("gender")
        student.email = request.POST.get("email")
        student.phone_number = request.POST.get("phone")
        student.address = request.POST.get("address")
        
        student.save()
        
        messages.success(request, "Profile updated successfully!")
        
        return redirect("my-profile")

    parameters = {
        'student': student,
        'avatars': all_avatars,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
    }

    return render(request, "dashboard/update_profile.html", parameters)

# ===================================== UPDATE AVATAR ===========================


def update_avatar(request, id):
    student = Student.objects.get(id=request.user.id)
    avatar = Avatar.objects.get(id=id)

    student.avatar = avatar
    student.save()

    messages.success(request, "Your avatar has been updated successfully!")

    return redirect("update-profile")


# ================================================================================================
# =========================================== TESTING ==================================
# ================================================================================================


def practice(request):
    
    student = Student.objects.get(id=request.user.id)
    
    parameters = {
        'student': student,
        'total_badges': Badge.objects.all().count(),
        'remaining_points': remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
    }
    
    return render(request, "dashboard/testing/choice.html", parameters)













def test(request):
    
    word = "cat"
    
    result = segment_sentence_to_phonemes(word)
    
    phonemes = []
    
    for pair in result:
        phoenem = Phoneme.objects.get(key=pair[1])
        phonemes.append(phoenem)
    
    
    parameters = {
        "result": result,
        "phonemes": phonemes,
        "word": word
    }
    
    return render(request, "dashboard/training/test.html", parameters)