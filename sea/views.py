
from django.shortcuts import render,render_to_response
from .models import Lookup_Site, Lookup_Fish,Survey_Info, Lookup_Invert,Invert_Data, Lookup_Benthic, BenthicSurvey_Data, FishSurvey_data
from django.forms import ModelForm
from django.template import RequestContext

def index(request):
    context = {
        
    }
    return render(request,'sea/index.html',context)
    
def records(request):
    yote  = Lookup_Site.objects.all()
    context = { 
        'yote':yote
    }
    return render(request,'sea/all.html',context)

def query2(request):
    items = Lookup_Site.objects.all()
    think = Lookup_Fish.objects.all()
    context = {
        'items':items,
        'think':think
    }
    return render(request,'sea/fikiri.html',context)
def query3(request):
    stuffs  = Lookup_Site.objects.all()
    listen = Lookup_Invert.objects.all()
    context = {
        'stuffs':stuffs,
        'listen':listen
    }
    return render(request,'sea/skiza.html',context)
def query13(request):
    lastone  = Lookup_Benthic.objects.all()
    balls = Lookup_Site.objects.all()
    context = {
        'lastone':lastone,
        'balls':balls
    }
    return render(request,'sea/phone.html',context)

class Lookup_FishForm(ModelForm):
    class Meta:
        model = Lookup_Fish
        fields = ['Name_Local', 'Name_Common','ID'] 
def query4(request, template_name='sea/input.html'):
    trial  = Lookup_Fish.objects.all()
    form = Lookup_FishForm(request.POST or None)
    if form.is_valid():
        form.save()
    # elif form.is_valid() and request.method == "POST" :
    #     item_id = request.POST.get(Lookup_FishForm, 'Name_Local')
    #     item = Lookup_Fish.objects.get(id=item_id)
    #     item.delete()
    context = {
        'trial':trial,
        'form':form
        }
    return render(request, template_name, context)

# def query12(request, pk, template_name='sea/input.html'):
#     form = Lookup_FishForm(request.POST or None)
#     fine= get_object_or_404(Lookup_Fish, Name_Local=pk)   
#     # fine  = Lookup_Fish.objects.all() 
#     if request.method=='POST':
#         form.delete()
#         return redirect('input')
#     context = {
#         'fine':fine,
#         'form':form
#     }
#     return render(request, template_name, context)
    
    
def query12(request, template_name='sea/input.html'):
    fine  = Lookup_Fish.objects.all()
    form = Lookup_FishForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        item_id = int(request.POST.get('Name_Local'))
        item = Lookup_Fish.objects.get(id=item_id)
        item.delete()
    context = {
        'fine':fine,
        'form':form
        }
    return render(request, template_name, context)

# def query12(request):
#     form = Lookup_FishForm()
#     fine = Lookup_Fish.objects.all()
#     if request.method == 'POST':
#         item_id = int(request.POST.get('item_id'))  
#         item = Lookup_Fish.objects.get(id=item_id)       
#         item.delete()
#     return render(request, template_name, context)

class Lookup_InvertForm(ModelForm):
    class Meta:
        model = Lookup_Invert
        fields = ['Name_Local', 'Name_Common','ID'] 
def query5(request, template_name='sea/input1.html'):
    trial1  = Lookup_Invert.objects.all()
    form = Lookup_InvertForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'trial1':trial1,
        'form':form
        }
     
    return render(request, template_name, context)

class Lookup_BenthicForm(ModelForm):
    class Meta:
        model = Lookup_Benthic
        fields = '__all__'
def query6(request, template_name='sea/input2.html'):
    trial2  = Lookup_Benthic.objects.all()
    form = Lookup_BenthicForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'trial2':trial2,
        'form':form
        }
    return render(request, template_name, context)

class BenthicSurvey_DataForm(ModelForm):
    class Meta:
        model = BenthicSurvey_Data
        fields = '__all__'
def query7(request, template_name='sea/input3.html'):
    trial3  = BenthicSurvey_Data.objects.all()
    form = BenthicSurvey_DataForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'trial3':trial3,
        'form':form
        }
    return render(request, template_name, context)

class FishSurvey_dataForm(ModelForm):
    class Meta:
        model = FishSurvey_data
        fields = '__all__'
def query8(request, template_name='sea/input4.html'):
    trial4  = FishSurvey_data.objects.all()
    form = FishSurvey_dataForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'trial4':trial4,
        'form':form
        }
    return render(request, template_name, context)

class Invert_DataForm(ModelForm):
    class Meta:
        model = Invert_Data
        fields = ['TransID','Name_Invert','No_Invert']
def query9(request, template_name='sea/input5.html'):
    trial5  = Invert_Data.objects.all()
    form = Invert_DataForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'trial5':trial5,
        'form':form
        }
     
    return render(request, template_name, context)

class Lookup_SiteForm(ModelForm):
    class Meta:
        model = Lookup_Site
        fields = '__all__'
def query10(request, template_name='sea/input6.html'):
    trial6  = Lookup_Site.objects.all()
    form = Lookup_SiteForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'trial6':trial6,
        'form':form
        }
     
    return render(request, template_name, context)

class Survey_InfoForm(ModelForm):
    class Meta:
        model = Survey_Info
        fields = '__all__'
def query11(request, template_name='sea/input7.html'):
    trial7  = Survey_Info.objects.all()
    form = Survey_InfoForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'trial7':trial7,
        'form':form
        }
    return render(request, template_name, context)


        
