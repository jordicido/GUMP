from rest_framework import serializers


from exercises.models import Exercise

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Exercise
        fields = ('url', 'id', 'title', 'description', 'experience')


