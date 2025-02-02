from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('grievances/', views.GrievanceListView.as_view(), name='grievance-list'),
    path('grievance/new/', views.GrievanceCreateView.as_view(), name='grievance-create'),
    path('grievance/<int:pk>/', views.GrievanceDetailView.as_view(), name='grievance-detail'),
    path('grievance/<int:pk>/update/', views.GrievanceUpdateView.as_view(), name='grievance-update'),
    path('grievance/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('grievance/<int:pk>/escalate/', views.escalate_grievance, name='escalate-grievance'),
    path('reports/', views.reports, name='reports'),
    path('grievance/<int:pk>/feedback/', views.submit_feedback, name='submit-feedback'),
    path('analytics/', views.analytics_dashboard, name='analytics-dashboard'),
    path('reports/generate/', views.generate_report, name='generate-report'),
    path('reports/export/csv/', views.export_csv, name='export-csv'),
    path('reports/export/excel/', views.export_excel, name='export-excel'),
]