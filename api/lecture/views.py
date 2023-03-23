from django.http import JsonResponse
from rest_framework import viewsets
from .models import Lecture
from .serializers import LectureSerializer
from django.core.mail import send_mail

# Create your views here.
class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all().order_by('id')
    serializer_class = LectureSerializer 
   

def send_mail(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'siddhipatel704185@gmail.com',
        ['siddhipatel8990@gmail.com'],
        fail_silently=False,
    )
    return JsonResponse({'message': 'Email was sent successfully!'})