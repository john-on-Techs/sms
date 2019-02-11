# payments/urls.py
from django.urls import path, re_path
from django.views.generic.dates import ArchiveIndexView
from .models import SaleRecord

from . import views

app_name = "sms"

urlpatterns = [
path('pdf/',views.Pdf.as_view(),name='report'),
    
    path('',views.IndexView.as_view(),name='index'),
    path('station/<int:place>/',views.ByStationView.as_view(),name='by-station'),
    
    path('sale-record/create/', views.SaleRecordCreateView.as_view(), name='create'),
    path('sale-record/<int:pk>/', views.SaleRecordDetailView.as_view(), name='detail'),
    path('sale-record/<int:pk>/delete/', views.SaleRecordDeleteView.as_view(), name='delete'),
    path('sale-record/<int:pk>/edit/', views.SaleRecordUpdateView.as_view(), name='edit'),
     path('<int:year>/', views.SaleRecordYearArchiveView.as_view(), name='sales_year_archive'),
    # Example: /2012/08/
    path('<int:year>/<int:month>/', views.SaleRecordMonthArchiveView.as_view(month_format='%m'),
         name='sales_month_archive_numeric'),
    # Example: /2012/aug/
    path('<int:year>/<str:month>/', views.SaleRecordMonthArchiveView.as_view(), name='sales_month_archive'),
    # Example: /2019/jan/26
    path('<int:year>/<int:month>/<int:day>/', views.SaleRecordDayArchiveView.as_view(month_format='%m'),
         name='sales_day_archive_numeric'),
         # Example: /2012/week/23/
    path('<int:year>/week/<int:week>/',views.SaleRecordWeekArchiveView.as_view(),
         name="archive_week"),
    path('<int:year>/<str:month>/<int:day>/', views.SaleRecordDayArchiveView.as_view(), name="archive_day"),


]