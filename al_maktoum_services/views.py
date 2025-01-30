from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project, Expense
from .serializers import ProjectSerializer, ExpenseSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class ProjectListCreateView(APIView):
    """
    Handles listing and creating projects.
    """
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        print(request.data)  # Debugging: Check the raw data received
        print(serializer.is_valid())  # Debugging: Check if valid
        print(serializer.errors)  # Debugging: Check validation errors
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class ExpenseListCreateView(APIView):
    """
    Handles listing and creating expenses for a specific project.
    """

    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        # Get the project object based on the provided project ID (pk)
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response({"detail": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        # Add the project to the request data before saving the expense
        data = request.data.copy()  # Ensure we can modify the request data
        data['project'] = project.id  # Associate the expense with the project
        print(data)

        # Serialize the data
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            # Save the expense
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class ProjectDetailView(APIView):
    """
    Handles retrieving a specific project by its ID.
    """
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
