from django.shortcuts import render

from accounts.models import Student, Avatar

# ================================= INDEX ===================================

def index(request):
    
    student = Student.objects.get(id=request.user.id)
    all_students = Student.objects.all().exclude(id=request.user.id)
    
    parameters = {
        "student": student,
        "all_students": all_students,
    }
    
    return render(request, "community/index.html", parameters)