from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from accounts.models import Student, Avatar, Badge
from .views import remaining_points, remaining_points_in_percentage

# =============================== Tic Tac Toe ===========================


def tic_tac_toe(request):

    student = Student.objects.get(id=request.user.id)

    parameters = {
        "student": student,
        "remaining_points": remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
    }

    return render(request, "dashboard/games/tic_tac_toe.html", parameters)

# =============================== Piano ===========================


def piano(request):

    student = Student.objects.get(id=request.user.id)

    parameters = {
        "student": student,
        "remaining_points": remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
    }

    return render(request, "dashboard/games/piano.html", parameters)


# =============================== GUESS THE NUMBER GAME ===========================

def guess_the_number(request):

    student = Student.objects.get(id=request.user.id)

    parameters = {
        "student": student,
        "remaining_points": remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
    }

    return render(request, "dashboard/games/guess_the_number.html", parameters)

# =============================== CHESS GAME ===========================


def chess(request):

    student = Student.objects.get(id=request.user.id)

    parameters = {
        "student": student,
        "remaining_points": remaining_points(student),
        "remaining_points_in_percentage": remaining_points_in_percentage(student),
    }

    return render(request, "dashboard/games/chess.html", parameters)

# ===============================================================================================================================
# ====================================================== UPDATING POINTS ==========================================================
# ===============================================================================================================================

# ===================================== Award Badges ============================================


def award_badges(student):
    # Fetch badge conditions from the database
    badge_conditions = Badge.objects.all()

    awarded_badges = []
    for condition in badge_conditions:
        points_required = condition.points_required
        if student.points >= points_required:
            # Check if the student already has the badge
            if not student.badges.filter(id=condition.id).exists():

                # Add the badge to the student
                student.badges.add(condition)
                awarded_badges.append(condition)

    return awarded_badges


# ====================================== Update Points ==========================================

@csrf_exempt
def update_points(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        points = request.POST.get("points")
        try:
            student = Student.objects.get(pk=student_id)
            # Add 5 points to the student's current points
            student.points += int(points)
            student.save()

            award_badges(student)

            return JsonResponse({"message": "Points updated successfully."})
        except Student.DoesNotExist:
            return JsonResponse({"message": "Student not found."})
    else:
        return JsonResponse({"message": "Invalid request method."})
