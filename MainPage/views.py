from django.shortcuts import render
import pickle

# Create your views here.
def index(request):
     return render(request, 'index.html')

def button1(request):
     return render(request,'Fakenote1.html')

def result(request):
    model = pickle.load(open('model.pkl','rb'))
    lis = []
    lis.append(float(request.POST['v']))
    lis.append(float(request.POST['s']))
    lis.append(float(request.POST['c']))
    lis.append(float(request.POST['e']))

    ans = model.predict([lis])
    if ans[0]==0:
        res = "not"
    if ans[0]==1:
        res = ""

    return render(request, 'Fakenote2.html',{"variable":res})

def button2(request):
    return render(request, 'Diabetes1.html')

def diabetes(request):
    model = pickle.load(open('diab.pkl','rb'))
    lis = []
    lis.append(float(request.POST['p']))
    lis.append(float(request.POST['g']))
    lis.append(float(request.POST['bp']))
    lis.append(float(request.POST['s']))
    lis.append(float(request.POST['i']))
    lis.append(float(request.POST['b']))
    lis.append(float(request.POST['a']))
    ans = model.predict([lis])
    if ans[0]==0:
        res = "You do not have diabetes."
    if ans[0]==1:
        res = "There is a chance you have diabetes."

    return render(request, 'Diabetes2.html',{"variable":res})


def button3(request):
    return render(request, 'Salary1.html')

def salary(request):
    model = pickle.load(open('salary.pkl','rb'))
    lis = []
    lis.append(float(request.POST['e']))
    lis.append(float(request.POST['t']))
    lis.append(float(request.POST['i']))

    ans = model.predict([lis])
    res = int(ans[0])

    return render(request,'Salary2.html',{"variable":res})

def button4(request):
    return render(request, 'Forest1.html')

def forest(request):
    model = pickle.load(open('forest.pkl','rb'))
    lis = []
    lis.append(float(request.POST['o']))
    lis.append(float(request.POST['t']))
    lis.append(float(request.POST['h']))

    ans = model.predict_proba([lis])
    res = '{0:.{1}f}'.format(ans[0][1], 2)

    return render(request,'Forest2.html',{"variable":res})