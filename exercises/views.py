from rest_framework import viewsets
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer

# Create your views here.
class ExerciseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `solve` action.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer