from django.shortcuts import render
from chat import models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class pair:
    def __init__(self,q,ans):
        self.q=q
        self.ans=ans
@login_required(login_url='http://localhost:8000/helper/userLogin')
def questAns(request):
    questions=models.question.objects.filter(user=request.user)
    data=[]
    for obj in questions:
        ans=models.answer.objects.filter(question=obj)
        p=pair(obj.msg,ans)
        data.append(p)
    data=data[::-1]
    return render(request,'chat/ask.html',{'quest':questions,'data':data})
def submitQuestion(request):
    q=models.question()
    q.user=request.user
    q.msg=request.GET['quest']
    q.save()
    return HttpResponseRedirect('http://localhost:8000/chat/ask')
