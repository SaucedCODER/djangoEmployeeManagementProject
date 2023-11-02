from django.shortcuts import render,HttpResponse
sample_posts = [
    {   'id':1,
        'title': 'Sample Post 1',
        'image_url': 'https://images.unsplash.com/photo-1528977695568-bd5e5069eb61?auto=format&fit=crop&q=80&w=1770&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'summary': 'This is the summary of sample post 1.',
    },
    {
    'id':2,

        'title': 'Sample Post 2',
        'image_url': 'https://plus.unsplash.com/premium_photo-1683134070924-75ff53569b11?auto=format&fit=crop&q=80&w=1770&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'summary': 'This is the summary of sample post 2.',
    },
    # Add more sample posts as needed
]
# Create your views here.
def home(request):
    return render(request,'home.html',{'blog_posts': sample_posts})