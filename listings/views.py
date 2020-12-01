from django.shortcuts import get_object_or_404, render
from .choices import price_choices, bedroom_choices, state_choices


from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator

#fetch the data
from .models import Listing, Comment

# Create your views here.
def index(request):
    #varname = modelname.objects.all()
    # listings = Listing.objects.all()//displaying in any order
    
    # now displaying the list in the latest date(descending)
    listings = Listing.objects.order_by('-list_date').filter(is_published = True) 
    
    #creating the pagination
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    if request.method == "POST":
        #  user_id = request.user.id
        name = request.POST['name']
        message = request.POST['message'] 
        stars = request.POST['stars']
        proid = listing_id

        query = Comment(message = message, name = name, stars = stars )
        query.proid_id = proid
        query.stars = stars
        query.save()
    listing = get_object_or_404(Listing, pk = listing_id)
    comment = Comment.objects.all().filter(proid = listing_id)

    context = {
        'listing' : listing,
        'comments':comment
    }
    return render(request,'listings/listing.html',context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)

    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)

    #state'
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)








    
    context = {
        'state_choices':state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices,
        'listings' :queryset_list,
        'values':request.GET

    }

    return render(request,'listings/search.html', context)