from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Property, Testimonial, Contact, About
from .forms import ContactForm, BookingForm
from blog.models import Post


class PropertyDetailView(DetailView):
    model = Property
    template_name = "core/property_details.html"


def index(request):
    properties = Property.objects.all()
    latest_sales = Property.objects.filter(category="SL").order_by("-listing_date")[:4]
    clients = Testimonial.objects.all()
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
                request, f"Thank you {name} for contacting us, we will get back to you."
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


class AboutUsView(TemplateView):
    template_name = "core/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        return context
