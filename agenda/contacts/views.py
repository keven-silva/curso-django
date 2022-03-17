from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from django.core.paginator import Paginator

from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

from .models import Contact


def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        show=True
    )
    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def template_contact(request, pk):
    contact = get_object_or_404(Contact, id=pk)

    if not contact.show:
        raise Http404()

    return render(request, 'contacts/template_contact.html', {
        'contact': contact
    })


def busca(request):
    termo = request.GET.get('termo')
    field = Concat('name', Value(' '), 'last_name')

    if termo is None or not termo:
       messages.add_message(
           request, 
           messages.ERROR,
           'Campo termo não pode ficar vazio.'
       )
       return redirect('index')
    
    contacts = Contact.objects.annotate(
        full_name = field
    ).filter(
        Q(full_name__icontains=termo) | Q(phone__icontains=termo)
    )
    
    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/busca.html', {
        'contacts': contacts
    })
