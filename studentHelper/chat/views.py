from django.contrib import messages
from django.shortcuts import render
from chat import models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class pair:
    def __init__(self,q,ans):
        self.q=q
        self.ans=ans
@login_required(login_url='/helper/userLogin')
def questAns(request):
    questions=models.question.objects.filter(user=request.user)
    data=[]
    for obj in questions:
        ans=models.answer.objects.filter(question=obj)
        p=pair(obj.msg,ans)
        data.append(p)
    data=data[::-1]
    return render(request,'chat/ask.html',{'quest':questions,'data':data})
@login_required(login_url='/helper/userLogin')
def submitQuestion(request):
    q=models.question()
    q.user=request.user
    q.msg=request.GET['quest']
    q.save()
    return HttpResponseRedirect('/chat/ask')
@login_required(login_url='/helper/userLogin')
def suggest(request):
    q=models.question.objects.all()
    return render(request,'chat/suggest.html',{'q':q})

def takeSuggestion(request):
    q=models.question.objects.get(ques_id=request.GET['b_id'])
    return render(request,'chat/giveSuggest.html',{'q':q})
def submitAns(request):
    q=models.question.objects.get(ques_id=request.GET['q_id'])
    ansObj=models.answer()
    ansObj.ans=request.GET['answer']
    ansObj.question=q
    ansObj.user_id=request.user.id
    ansObj.save()
    messages.success(request,'Ans Submittion Successfully!')
    return render(request,'chat/giveSuggest.html',{'q':q})