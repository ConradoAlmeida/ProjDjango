from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Cliente, Veiculo, Ordem
from .forms import ClientesForm, VeiculosForm, OrdemForm


def home(request):
    context = {
        'ordens': Ordem.objects.all()
    }
    return render(request, 'garage/home.html', context)


class HomeListView(ListView):
    model = Ordem
    template_name = 'garage/home.html'
    context_object_name = 'ordens'
    ordering = ['-data_criacao']


class ClienteListView(ListView):
    model = Cliente
    template_name = 'garage/clientes/client_home.html'
    context_object_name = 'clientes'
    ordering = ['-data_criacao']


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'garage/clientes/client_details.html'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'garage/clientes/client_create_form.html'
    form_class = ClientesForm


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = '/garage/clientes'
    template_name = 'garage/clientes/client_confirm_delete.html'


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep']
    template_name = 'garage/clientes/client_update_form.html'


class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_home.html'
    context_object_name = 'veiculos'
    ordering = ['-data_criacao']


class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_details.html'


class VeiculoCreateView(CreateView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_create_form.html'
    form_class = VeiculosForm


class VeiculoDeleteView(DeleteView):
    model = Veiculo
    success_url = '/garage/veiculos'
    template_name = 'garage/veiculos/veiculo_confirm_delete.html'


class VeiculoUpdateView(UpdateView):
    model = Veiculo
    fields = ['marca', 'modelo', 'placa', 'motor', 'ano']
    template_name = 'garage/veiculos/veiculo_update_form.html'


class OrdemListView(ListView):
    model = Ordem
    template_name = 'garage/ordens/ordem_home.html'
    context_object_name = 'ordens'
    ordering = ['-cliente_id']


class OrdemDetailView(DetailView):
    model = Ordem
    template_name = 'garage/ordens/ordem_details.html'


class OrdemCreateView(CreateView):
    model = Ordem
    template_name = 'garage/ordens/ordem_create_form.html'
    form_class = OrdemForm


class OrdemDeleteView(DeleteView):
    model = Ordem
    success_url = '/garage/ordens'
    template_name = 'garage/ordens/ordem_confirm_delete.html'


class OrdemUpdateView(UpdateView):
    model = Ordem
    form_class = OrdemForm
    template_name = 'garage/ordens/ordem_update_form.html'
    success_url = '/garage/ordens'
