from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Property


# class HomeView(ListView):
#     model = Property
#     template_name = "core/index.html"
#     context_object_name = "properties"


def index(request):
    properties = Property.objects.all()
    latest_rentals = Property.objects.filter(category="RE").order_by("-listing_date")[
        :4
    ]
    latest_sales = Property.objects.filter(category="SL").order_by("-listing_date")[:4]
    context = {
        "properties": properties,
        "latest_rentals": latest_rentals,
        "latest_sales": latest_sales,
    }
    return render(request, "core/index.html", context)


def propertyForRent(request):
    rental = Property.objects.filter(category="RE")
    recommended = Property.objects.filter(category="RE").order_by("-listing_date")[:4]
    paginator = Paginator(rental, 4)
    page_request_variable = "page"
    page = request.GET.get(page_request_variable)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        "properties": paginated_queryset,
        "page_request_variable": page_request_variable,
        "recommended": recommended,
    }
    return render(request, "core/property_for_rent.html", context)


def propertyForSale(request):
    sale = Property.objects.filter(category="SL")
    recommended = Property.objects.filter(category="SL").order_by("-listing_date")[:4]
    paginator = Paginator(sale, 4)
    page_request_variable = "page"
    page = request.GET.get(page_request_variable)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        pagginated_queryset = paginator.page(paginator.num_pages)

    context = {
        "properties": paginated_queryset,
        "recommended": recommended,
        "page_request_variable": page_request_variable,
    }
    return render(request, "core/property_for_sale.html", context)


def contact(request):
    return render(request, "core/contact.html", {})


class PropertyDetailView(DetailView):
    model = Property
    template_name = "core/property_details.html"
