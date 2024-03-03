from django.shortcuts import render,redirect
from TestApp.models import *
# Create your views here.

def Team(request):
    TeamData=tbl_Team.objects.all()
    if request.method == 'POST':
        tbl_Team.objects.create(Team_Name=request.POST.get('TeamName'),Team_Photo=request.FILES.get('Team_Photo'), Team_Password=request.POST.get('TeamPassword')) 
        return render(request,"TestApp/Team.html",{"Teamdata":TeamData})
    else:
        return render(request,"TestApp/Team.html",{"Teamdata":TeamData})
    
def delete_Team(request,id):
    tbl_Team.objects.get(id=id).delete()
    return redirect("webclass:Team")

def Player_Category(request):
    Player_CategoryData=tbl_Player_Category.objects.all()
    if request.method == 'POST':
        tbl_Player_Category.objects.create(Player_Category=request.POST.get('Player_Category')) 
        return render(request,"TestApp/Player_Category.html",{"Player_Categorydata":Player_CategoryData})
    else:
        return render(request,"TestApp/Player_Category.html",{"Player_Categorydata":Player_CategoryData})
    
def delete_Player_Category(request,id):
    tbl_Player_Category.objects.get(id=id).delete()
    return redirect("webclass:Player_Category")
    
def Player_Detail(request):
    TeamData=tbl_Team.objects.all()
    Player_Category_Data=tbl_Player_Category.objects.all()
    playerData=tbl_Player.objects.all()
    if request.method == 'POST': 
        Team= tbl_Team.objects.get(id=request.POST.get('sel_team'))
        Category= tbl_Player_Category .objects.get(id=request.POST.get('sel_category'))
        tbl_Player.objects.create(Player_Name=request.POST.get('PlayerName'),Player_Photo=request.FILES.get('Player_Photo'), Player_Password=request.POST.get('Player_Password')) 
        return render(request,"TestApp/Team.html",{"playerData":playerData})
    else:
        return render(request,"TestApp/Team.html",{"playerData":playerData})