import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post

def post(request, office_id):
    return render(request, 'rabbit/post.html', {'office_id': office_id})

def form(request):
    office_id = int(request.POST['office_id'])
    encrypted_message = request.POST['encrypted']
    posted_date = timezone.now()
    post = Post(
        office_id=office_id,
        encrypted_message=encrypted_message,
        posted_date=posted_date
    )
    post.save()
    return redirect(to='post/' + str(office_id))

def list(request):
    posts = Post.objects.filter(posted_date__lte=timezone.now()-datetime.timedelta(days=28))
    posts.delete()
    posts = Post.objects.all().order_by('office_id')
    for post in posts:
        post.posted_date = post.posted_date.date()
    return render(request, 'rabbit/list.html', {'posts': posts})
