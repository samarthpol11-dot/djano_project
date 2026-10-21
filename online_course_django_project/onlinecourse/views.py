from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Course, Lesson, Submission, Choice


def course_list(request):
    return render(request, "onlinecourse/course_list.html", {"courses": Course.objects.all()})


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "onlinecourse/course_details_bootstrap.html", {"course": course})


@login_required
@require_POST
def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    score = 0
    total_score = 0

    for question in lesson.questions.prefetch_related("choices").all():
        total_score += question.grade
        selected = request.POST.get(f"question_{question.id}")
        correct_choice = question.choices.filter(is_correct=True).first()
        if correct_choice and selected and str(correct_choice.id) == selected:
            score += question.grade

    result = Submission.objects.create(
        student=request.user, lesson=lesson, score=score, total_score=total_score
    )
    return redirect("show_exam_result", submission_id=result.id)


@login_required
def show_exam_result(request, submission_id):
    result = get_object_or_404(Submission, pk=submission_id, student=request.user)
    percentage = round(result.score * 100 / result.total_score) if result.total_score else 0
    return render(request, "onlinecourse/exam_result.html", {
        "result": result, "percentage": percentage
    })


def lesson_exam(request, lesson_id):
    lesson = get_object_or_404(
        Lesson.objects.prefetch_related("questions__choices"), pk=lesson_id
    )
    return render(request, "onlinecourse/mock_exam.html", {"lesson": lesson})
