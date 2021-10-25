from guitars.models import Brand, Country

def brands(request):

    total_brands=Brand.objects.all()

    return {'total_brands':total_brands}

def countries(request):

    total_countries=Country.objects.all()

    return {'total_countries':total_countries}
