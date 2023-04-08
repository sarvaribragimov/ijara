from .models import Category,StudentWork


def all_categories(request):
    return dict(categories=Category.objects.all())

def all_works(request):
    return dict(studentwork = StudentWork.objects.all())