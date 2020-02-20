from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Property


def index(request):
    properties = Property.objects.all()
    latest_sales = Property.objects.filter(category="SL").order_by("-listing_date")[:4]
    context = {
        "properties": properties,
        "latest_sales": latest_sales,
    }
    return render(request, "core/index.html", context)


def property_for_sale(request):
    sale = Property.objects.filter(category="SL")
    recommended = Property.objects.filter(category="SL").order_by("-listing_date")[:4]
    paginator = Paginator(sale, 8)
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
