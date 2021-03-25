from django.shortcuts import render

def index(request):
	if request.method=="POST":
		a = request.POST["txtnum1"]
		b = request.POST["txtnum2"]
		a,b = b,a
		return render(request,"swap/index.html",{'key1':a,'key2':b})
	else:
		return render(request,"swap/index.html")


def operation(request):
	if request.method=="POST":
		a = int(request.POST["txtnum1"])
		b = int(request.POST["txtnum2"])
		if request.POST['btn'] == "+":
			c=a+b
		elif request.POST['btn'] == "-":
			c=a-b
		elif request.POST['btn']=="*":
			c=a*b
		else:
			c=a/b    

		return render(request,"swap/ope.html",{'key1':a,'key2':b,'key':c})
	else:
		return render(request,"swap/ope.html")	
