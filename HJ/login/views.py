from django.shortcuts import render, redirect
from .models import hj_user
from . import testinput

# Create your views here.
def login(request):
	if request.method == "POST":
		name = request.POST.get('user_name')
		password = request.POST.get('user_password')
		if testinput.test_name(name) and testinput.test_pass(password):
			try:
				hj_user.objects.get(name=name, password=password)
				return redirect('/queryorder/main/')
			except Exception as e:
				# 浏览器弹出提示密码错误或用户名不存在
				message = '密码错误或用户名不存在！'
				return render(request, 'login/login.html', {'message': message})
		else:
			# 浏览器弹出提示用户名或密码不符合规范
			message = '用户名或密码不符合规范，请重新输入！'
			return render(request, 'login/login.html', {'message': message})
	return render(request, 'login/login.html')
