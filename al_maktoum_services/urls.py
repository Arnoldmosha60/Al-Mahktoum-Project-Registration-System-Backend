from django.urls import path
from .views import ProjectListCreateView, ExpenseListCreateView, ProjectDetailView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/add-expense/', ExpenseListCreateView.as_view(), name='expense-add'),
]
