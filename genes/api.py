from rest_framework import serializers, viewsets

from genes.models import GeneAutocomplete


class GeneAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneAutocomplete
        fields = ['species', 'stable_id', 'display_label', 'location', 'db']


class GeneAutocompleteViewSet(viewsets.ModelViewSet):
    serializer_class = GeneAutocompleteSerializer

    def get_queryset(self):
        query = self.kwargs['query']
        species = self.kwargs['species']
        limit = self.kwargs['limit']
        return GeneAutocomplete.objects.using('remote').filter(
            display_label__contains=query, species=species)[:limit]
