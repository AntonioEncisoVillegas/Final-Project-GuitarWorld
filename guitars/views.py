from django.contrib import messages
from django.shortcuts import redirect, render
from guitars.models import Country, GuitarComercial, Brand, GuitarHandMade, PunctuationComercial, PunctuationHandMade
from django.contrib.auth.decorators import login_required
# Create your views here.

#Comercial Guitars
def guitarsByBrand(request, id):

    guitars=GuitarComercial.objects.filter(brand_id=id)
    brand=Brand.objects.get(pk=id)

    return render(request, 'guitarsbybrand.html', {'guitars':guitars, 'brand':brand})

def guitarInformation(request, id):

    guitar=GuitarComercial.objects.get(pk=id)
    sum=0
    punctuations=PunctuationComercial.objects.filter(guuitar_id=id)
    calf=PunctuationComercial.objects.filter(user_id=request.user.id,guuitar_id=id)
    if calf:
        flag=True
    else:
        flag=False
    for puncuation in punctuations:
        sum=sum+puncuation.rate
    if sum > 0:
        sum=sum/len(punctuations)
    return render(request, 'guitarComercial.html', {'guitar':guitar, 'punctuation':sum, 'flag':flag})

@login_required(login_url='login')
def punctuateComercial(request, id):
    if request.method == 'POST':
        pun=request.POST.get('pun')
        save=PunctuationComercial(
            user_id=request.user.id,
            rate=pun,
            guuitar_id=id
        )
        save.save()
        messages.success(request, 'Rated!')
        return redirect('guitarComercial-info', id)
#HandMade Guitars

def allHandMadeGuitars(request):

    guitars=GuitarHandMade.objects.all()

    return render(request, 'handMadeGuitars.html', {'guitars':guitars})

def guitarInformationHandMade(request, id):

    guitar=GuitarHandMade.objects.get(pk=id)
    sum=0
    punctuations=PunctuationHandMade.objects.filter(guuitar_id=id)
    calf=PunctuationHandMade.objects.filter(user_id=request.user.id,guuitar_id=id)
    if calf:
        flag=True
    else:
        flag=False
    for puncuation in punctuations:
        sum=sum+puncuation.rate
    if sum > 0:
        sum=sum/len(punctuations)

    return render(request, 'guitarHandMade.html', {'guitar':guitar, 'punctuation':sum, 'flag':flag})

def guitarsByCountry(request, id):

    guitars=GuitarHandMade.objects.filter(country_id=id)
    country=Country.objects.get(pk=id)
    return render(request, 'guitarsByCountry.html', {'guitars':guitars, 'country':country})

@login_required(login_url='login')
def punctuateHandMade(request, id):
    if request.method == 'POST':
        pun=request.POST.get('pun')
        save=PunctuationHandMade(
            user_id=request.user.id,
            rate=pun,
            guuitar_id=id
        )
        save.save()
        messages.success(request, 'Rated!')
        return redirect('handmade-info', id)

def guitarBySearch(request):
    if request.method == 'POST':
        search=request.POST.get('search')
        guitars1=GuitarComercial.objects.filter(name__contains=search)
        guitars2=GuitarHandMade.objects.filter(name__contains=search)
        return render(request, 'guitarsBySearch.html',{'guitars1':guitars1, 'guitars2':guitars2})