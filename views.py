from django.shortcuts import render

def index(request):
	if request.method=="POST":
		a = request.POST["txtnum1"]
		b = request.POST["txtnum2"]
		a,b = b,a
		return render(request,"swap/index.html",{'key1':a,'key2':b})
	else:
		return render(request,"swap/index.html")



