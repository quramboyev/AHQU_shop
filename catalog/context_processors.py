from .models import CategoryModel

def categories_processor(request):
    return {
        'categories': CategoryModel.objects.all()
    }
