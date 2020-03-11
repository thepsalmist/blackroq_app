from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.views.generic import DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Property, Testimonial, Contact, About
from .forms import ContactForm, BookingForm
from blog.models import Post
from marketting.models import SignUp


class PropertyDetailView(DetailView):
    model = Property
    template_name = "core/property_details.html"


def index(request):
    properties = Property.objects.all()
    latest_sales = Property.objects.filter(category="SL").order_by("-listing_date")[:4]
    clients = Testimonial.objects.all()
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = SignUp()
        new_signup.email = email
        new_signup.save()
        messages.info(request, "Thank you for subscribing")
        return redirect("core:home")

    context = {
        "properties": properties,
        "latest_sales": latest_sales,
        "clients": clients,
    }
    return render(request, "core/index.html", context)


def property_for_sale(request):
    sale = Property.objects.filter(category="SL")
    recommended = Property.objects.filter(category="SL").order_by("-listing_date")[:4]
    latest_posts = Post.objects.order_by("-publish")[:4]
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
        "latest_posts": latest_posts,
        "page_request_variable": page_request_variable,
    }
    return render(request, "core/property_for_sale.html", context)


def book_property(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(
                request,
                f"Thank you {name} for booking a viewing, we will get back to you.",
            )
            return redirect("core:home")
    else:
        form = BookingForm()

    context = {
        "form": form,
    }

    return render(request, "core/booking.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(
                request, f"Thank you {name} for contacting us, we will get back to you."
            )
            return redirect("core:home")
    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "core/contact.html", context)


def is_valid_query(param):
    return param != "" and param is not None


def search(request):
    properties = Property.objects.all()
    query = request.GET.get("query")
    minimum_price = request.GET.get("minimum_price")
    maximum_price = request.GET.get("maximum_price")
    maximum_area = request.GET.get("maximum_area")
    minimum_area = request.GET.get("minimum_area")
    location = request.GET.get("location")

    if query:
        properties = properties.filter(Q(title__icontains=query)).distinct()
    if is_valid_query(minimum_price):
        properties = properties.filter(price__gte=minimum_price)
    if is_valid_query(maximum_price):
        properties = properties.filter(price__lte=maximum_price)
    if is_valid_query(minimum_area):
        properties = properties.filter(area__gte=minimum_area)
    if is_valid_query(maximum_area):
        properties = properties.filter(area__lte=maximum_area)
    if is_valid_query(location) and location != "Choose...":
        properties = properties.filter(Q(location__icontains=location))

    context = {
        "properties": properties,
    }
    return render(request, "core/search.html", context)


class AboutUsView(TemplateView):
    template_name = "core/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        return context
