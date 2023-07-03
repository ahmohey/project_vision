import json

from django import forms
from django.http import(
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    JsonResponse,
)
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from jeju_cam.models.user import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
# Create your views here.

@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    form_class = UserForm

    #단건조회(pk가 있는경우), 목록조회
    def get(self, request, pk=None):
        if pk is not None:
            user = User.objects.filter(id=pk).values()
            if not user:
                return JsonResponse({"error": "User not Found"}, status=404)
            return JsonResponse(user)
        else:
            members = User.objects.all()
            return JsonResponse(list(members.values()), safe=False)
    #수정
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = json.loads(request.body)

        user.user_id = data.get("user_id") or user.user_id
        user.user_name = data.get("user_name") or user.user_name
        user.user_email = data.get("user_email") or user.user_email
        user.user_pass = data.get("user_pass") or user.user_pass
        user.user_agree = data.get("user_agree") or user.user_agree

        user.save()
        return JsonResponse(data)
    
    #삭제
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return HttpResponse(status=200)
    
    #등록
    def post(self, request):
        data = json.loads(request.body)

        u = User(
            user_id=data.get("user_id"),
            user_name=data.get("user_name"),
            user_email=data.get("user_email"),
            user_pass=data.get("user_pass"),
            user_agree=data.get("user_agree"),
        )
        u.save()
        return JsonResponse({"message": "저장이 완료되었습니다"}, status=200)
    