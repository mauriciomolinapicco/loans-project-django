from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoanApplicationForm, LoanApplicationUpdateForm
from .utils.api_call import make_api_call
from .models import LoanApplication
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from .permissions import allowed_users
from django.contrib import messages
from .filters import LoanApplicationFilter



def index(request):   
    """
    HOME PAGE
    """   
    form = LoanApplicationForm()
    context = {'form':form}
    return render(request, "loans/index.html", context)


@allowed_users(allowed_roles=['admin'])
def admin_view(request):
    """
        Dashbaord del administrador
    """
    applications = LoanApplication.objects.all()

    qs_filter = LoanApplicationFilter(request.GET, queryset=applications)
    applications = qs_filter.qs

    context = {
        "applications":applications,
        "qs_filter":qs_filter
    }
    return render(request, "loans/admin_panel.html", context)


def new_application(request):
    """
    POST => crear una nueva aplicacion
    """
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            cuil = form.cleaned_data['cuil']
            approved = make_api_call(cuil)
            if approved:
                print(approved)
                form.instance.is_approved = True
            instance = form.save()
            return redirect(f"/application_sent/{instance.id}")
        else:
            for field in form:
                for error in field.errors:
                    message = f"{error}\n"
                    messages.error(request, message)

            return render(request, 'loans/index.html', {'form': form})

    return redirect('/')


def application_detail(request, pk):
    """
        GET single application
    """
    try:
        application = LoanApplication.objects.get(pk=pk)
    except (LoanApplication.DoesNotExist, ValidationError):
        # la excepcion salta si no encuentra ninguna aplicacion con el ID o si el formato no es UUID
        # simplemente devuelvo un dict vacio para que de 404 en el template
        application = {}
    context = {
        "application":application
    }
    return render(request, "loans/application_detail.html", context)


def application_detail_form(request):
    
    if request.method == 'POST':
        application_id = request.POST.get("application_id")
        return redirect("application_detail", pk=application_id)

    return render(request, "loans/application_detail_form.html")


@allowed_users(allowed_roles=['admin'])
def edit_application(request, pk):
    """
        PUT => editar una aplicacion
        Permitido solo por grupo admin
    """
    application = LoanApplication.objects.get(pk=pk)
    if request.method == 'POST':
        form = LoanApplicationUpdateForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('/admin_view')
        else:
            for field in form:
                for error in field.errors:
                    message = f"{error}\n"
                    messages.error(request, message)

            return redirect('edit_application', pk=pk)
        
    form = LoanApplicationUpdateForm(instance=application)
    context = {
        'form':form,
        'application_id':pk
        }
    return render(request, "loans/edit_application.html", context)


@allowed_users(allowed_roles=['admin'])
def delete_application(request, pk):
    """
        DELETE -> destruir una aplicacion
        Permitido solo por el grupo admin
    """
    application = LoanApplication.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            application.delete()
            messages.success(request, "Se elimino el registro")
        except (LoanApplication.DoesNotExist, ValidationError):
            application = {}
        finally:
            return redirect('/admin_view')

    context = {"application":application}
    return render(request, "loans/delete_application.html", context)


def application_sent(request, pk):
    """
        renderiza la pagina de exito en la creacion de aplicacion
    """
    application = LoanApplication.objects.filter(pk=pk).first()
    context = {
        "application":application
    }
    return render(request, "loans/application_sent.html", context)


def login_view(request):
    #login
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "loans/login.html", {
                "message": "Credenciales invalidas 🕵️"
            })
    else:
        return render(request, "loans/login.html")


def logout_view(request):
    #logout
    logout(request)
    return HttpResponseRedirect(reverse("index"))