from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
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
    
    print(termo)

    contacts = Contact.objects.order_by('-id').filter(
        name__icontains=termo,
        show=True
    )
    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/busca.html', {
        'contacts': contacts
    })
