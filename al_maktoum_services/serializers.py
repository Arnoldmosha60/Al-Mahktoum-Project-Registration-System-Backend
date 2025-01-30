from rest_framework import serializers
from .models import Project, Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

    def validate_project(self, value):
        # Ensure the project is valid
        if not value:
            raise serializers.ValidationError("Project is required.")
        return value


class ProjectSerializer(serializers.ModelSerializer):
    supervisor = serializers.JSONField(write_only=True)  # Handle nested supervisor data

    class Meta:
        model = Project
        fields = ['id', 'title', 'location', 'project_type', 'supervisor', 'created_at']  # Expose supervisor as input only

    def create(self, validated_data):
        # Extract supervisor data from the input
        supervisor_data = validated_data.pop('supervisor')
        validated_data['supervisor_name'] = supervisor_data.get('supervisor_name')
        validated_data['supervisor_contact'] = supervisor_data.get('supervisor_contact')

        # Create and save the project
        return Project.objects.create(**validated_data)