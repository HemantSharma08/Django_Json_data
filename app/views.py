from django.shortcuts import render
from .models import Data

# Create your views here.
def home(request):
    # Retrieve all Insight objects from the database
    insights = Data.objects.all()
    # Pass the data to the template context
    return render(request, 'index.html', {'insights': insights})
