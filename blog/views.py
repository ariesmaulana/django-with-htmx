from django.shortcuts import render
from blog.models import Content, Category, SubCategory
from django.views.decorators.http import require_http_methods

# Create your views here.
def hello_world(request):
    contents = Content.objects.all().select_related("category", "sub_category")
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all().select_related("category")
    selected_category = None
    selected_subcategory = None
    return render(request, 'page/dashboard.html',  {'contents': contents, 
    "selected_category": selected_category,
    "selected_subcategory": selected_subcategory,
    'categories': categories, 'sub_categories': sub_categories })


def get_selected(request, **kwargs):
    category = request.GET.get("category")
    sub_category = request.GET.get("sub_category")
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all().select_related("category")
    selected_category = None
    selected_subcategory = None
    if category:
        selected_category = int(category)
        sub_categories = sub_categories.filter(category_id=category)
    if sub_category:
        selected_category =  sub_categories.get(id=sub_category).category.id
        sub_categories = sub_categories.filter(category_id=selected_category)
        selected_subcategory =  int(sub_category)

    return render(request, 'components/filter.html', {
        "selected_category": selected_category,
        "selected_subcategory": selected_subcategory,
        'categories': categories, 'sub_categories': sub_categories})

@require_http_methods(["POST"])
def search_content(request):
    category = request.POST.get("category")
    sub_category = request.POST.get("sub_category")
    
    contents = Content.objects.filter(category_id=category, sub_category=sub_category).select_related("category", "sub_category")

    return render(request, 'components/table.html',  {'contents': contents })