from django.shortcuts import render
from core.models import Fixture, Prediction
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    # all matches
    fixtures = Fixture.objects.all()
    # show matches with a tip made by the active user
    predictions = [f.predictions.filter(user=request.user).first() for f in fixtures]

    context = {
        'fixtures_and_predictions': zip(fixtures, predictions),
    }
    return render(request, 'index.html', context)
