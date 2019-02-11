from .models import SaleRecord, Station, UserStation, Product
# class based views
from io import BytesIO
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.dates import YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, \
    TodayArchiveView
from django.urls import reverse_lazy
from bootstrap_datepicker_plus import DatePickerInput


def home(request):
    pass


from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render


class Pdf(View):


    def post(self, request):

        # qs = request.POST.getlist('qs')[0]
        # print(qs)
        # qs2=request.POST.get('qs')
        # print("=====================================\n",qs2)
        sales = SaleRecord.objects.all()
       
        today = timezone.now()
        params = {
            'today': today,
            'sale_list': sales,
            'request': request
        }
        return Render.render('sms/pdf.html', params)


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'sms/index.html'
    context_object_name = 'sale_list'

    def get_queryset(self):
        """Return the last five published questions."""
        if self.request.user.is_superuser:
            return SaleRecord.objects.filter(entry_at__lte=timezone.now())
        return SaleRecord.objects.filter(author=self.request.user, entry_at__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['product_list'] = Product.objects.all()
        return context


class ByStationView(LoginRequiredMixin, generic.ListView):
    template_name = 'sms/index.html'
    context_object_name = 'sale_list'

    def get_queryset(self):
        """Return the last five published questions."""
        station = None
        if self.kwargs.get('place') != None:
            station = self.kwargs.get('place')

        if self.request.user.is_superuser:
            return SaleRecord.objects.filter(entry_at__lte=timezone.now(), station=station)

        return SaleRecord.objects.filter(author=self.request.user, entry_at__lte=timezone.now(),
                                         station=station)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['product_list'] = Product.objects.all()

        return context


class SaleRecordCreateView(LoginRequiredMixin, generic.edit.CreateView):
    """docstring for SaleRecordCreateView."""
    model = SaleRecord
    fields = ['product', 'number_of_litres', 'entry_at']

    def get_form(self):
        form = super().get_form()
        form.fields['entry_at'].widget = DatePickerInput(format='%Y-%m-%d')
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.station = UserStation.objects.get(user=self.request.user).station
        # obj = form.save(commit=False)
        # obj.author=self.request.user
        # obj.station = UserStation.objects.get(user=self.request.user).station
        # print(obj.station)
        return super().form_valid(form)


class SaleRecordDetailView(LoginRequiredMixin, generic.DetailView):
    model = SaleRecord
    template_name = "sms/sale_detail.html"
    context_object_name = 'sale'


class SaleRecordDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    """docstring for SaleRecordDeleteView."""
    model = SaleRecord
    success_url = reverse_lazy('sms:index')


class SaleRecordUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """docstring for SaleRecordUpdateView."""
    model = SaleRecord
    fields = ['product', 'number_of_litres', 'entry_at']
    template_name_suffix = '_update_form'

    def get_form(self):
        form = super().get_form()
        form.fields['entry_at'].widget = DatePickerInput(format='%Y-%m-%d')
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.station = UserStation.objects.get(user=self.request.user).station
        print(form.instance.author, form.instance.station)
        return super().form_valid(form)


class SaleRecordYearArchiveView(LoginRequiredMixin, YearArchiveView):
    date_field = "entry_at"
    make_object_list = True
    context_object_name = 'sale_list'
    allow_future = True
    template_name = "sms/index.html"

    def get_queryset(self):
        """Return the last five published questions."""
        if self.request.user.is_superuser:
            return SaleRecord.objects.all()
        return SaleRecord.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['product_list'] = Product.objects.all()
        return context


class SaleRecordMonthArchiveView(LoginRequiredMixin, MonthArchiveView):
    date_field = "entry_at"
    allow_future = True
    context_object_name = 'sale_list'
    template_name = "sms/index.html"

    def get_queryset(self):
        """Return the last five published questions."""
        if self.request.user.is_superuser:
            return SaleRecord.objects.all()
        return SaleRecord.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['product_list'] = Product.objects.all()
        return context


class SaleRecordWeekArchiveView(LoginRequiredMixin, WeekArchiveView):
    date_field = "entry_at"
    week_format = "%W"
    allow_future = True
    context_object_name = 'sale_list'
    template_name = "sms/index.html"

    def get_queryset(self):
        """Return the last five published questions."""
        if self.request.user.is_superuser:
            return SaleRecord.objects.all()
        return SaleRecord.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['product_list'] = Product.objects.all()
        return context


class SaleRecordDayArchiveView(LoginRequiredMixin, DayArchiveView):
    date_field = "entry_at"
    allow_future = True
    context_object_name = 'sale_list'
    template_name = "sms/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['product_list'] = Product.objects.all()
        return context

    def get_queryset(self):
        """Return the last five published questions."""
        if self.request.user.is_superuser:
            return SaleRecord.objects.all()
        return SaleRecord.objects.filter(author=self.request.user)

# @login_required
# def sale_create(request):
#     if request.method == 'POST':
#         form = SaleRecordForm(request.POST)
#         if form.is_valid():
#             salerecord = form.save(commit=False)
#             salerecord.user = request.user
#             salerecord.entry_date = timezone.now()
#             salerecord.save()
#             return redirect('sales:sale_detail', pk=salerecord.pk)

#     else:
#         form = SaleRecordForm()
#     return render(request, 'sales/sale_record_edit.html', {'form': form})


# @login_required
# def sale_record_edit(request, pk):
#     error = None
#     salerecord = get_object_or_404(SaleRecord, pk=pk)
#     if request.method == 'POST' and request.user.is_superuser:
#         if request.user.is_superuser:
#             form = SaleRecordForm(request.POST, instance=salerecord)
#             if form.is_valid():
#                 salerecord = form.save(commit=False)
#                 salerecord.user = request.user                
#                 salerecord.save()
#                 return redirect('sales:sale_detail', pk=salerecord.pk)
#         else:
#             error = "Your are not permitted to edit this record"
#     else:
#         form = SaleRecordForm(instance=salerecord)
#     return render(request, 'sales/sale_record_edit.html',
#                   {'form': form, 'error': error})


# @login_required
# def sale_record_remove(request, pk):
#     salerecord = get_object_or_404(SaleRecord, pk=pk)
#     if request.user.is_superuser:
#         salerecord.delete()
#         return redirect('sales:index')
#     else:
#         raise ValueError("Contact the admin to delete this record")
