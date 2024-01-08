from django.shortcuts import render, get_object_or_404
from .models import Article, Category




def homepage(request):
    articles = Article.objects.all()
    return render(request, 'homepage.html', {'articles': articles})

def category_page(request, category_id):
    Category = get_object_or_404(Category, pk=category_id)
    articles = Category.article_set.all()
    return render(request, 'category_page.html', {'Category': Category, 'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})





def create_article(request):

    if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            Categore = request.POST.get('Categore')
            userform = Article(title = title , content = content, Categore = Categore )
            userform.save()
            print(userform)
                 
       
    return render(request , 'create_article.html')



def create_category(request):
         if request.method == 'POST':
            Categore = request.POST.get('Categore') 
            cform =  Category(Categore=Categore) 
            cform.save()
         return render(request, 'create_category.html')














# def create_article(request):
#     if request.method == 'POST':
#       title = request.POST.get('title')
#       content = request.POST.get('content')
#     #   dop = request.POST.get('dop')
#       Article.objects.create( title= title , content = content)  
#     else:
#         return render ( request , 'create_article.html' , { 'msg': 'Article is created Sucessfully'})
           

             
    

# def create_category(request):
#     if request.method == 'POST':
#         pass
#     else:
#         return render(
#             request , 'create_category.html',

#             {}


#         )   













