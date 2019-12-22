from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post

def send(request, office_id):
    return render(request, 'rabbit/send.html', {'office_id': office_id})

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
    return redirect(to='send/' + str(office_id))