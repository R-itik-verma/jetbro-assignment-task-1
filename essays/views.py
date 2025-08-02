import random
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Essay, EssayVersion
from .serializers import EssaySerializer, EssayVersionSerializer

def generate_scorecard():
    return {
        "structure": random.randint(1, 5),
        "clarity": random.randint(1, 5),
        "impact": random.randint(1, 5),
    }

class EssayCreateView(generics.CreateAPIView):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

class EssayVersionUploadView(generics.CreateAPIView):
    serializer_class = EssayVersionSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, essay_id):
        try:
            essay = Essay.objects.get(pk=essay_id)
        except Essay.DoesNotExist:
            return Response({"error": "Essay not found"}, status=404)

        file = request.FILES.get('content')
        if not file:
            return Response({"error": "File is required"}, status=400)

        if not file.name.endswith(('.pdf', '.docx')):
            return Response({"error": "Only .pdf and .docx files are allowed"}, status=400)

        scorecard = generate_scorecard()

        version = EssayVersion.objects.create(
            essay=essay,
            content=file,
            scorecard=scorecard
        )

        serializer = EssayVersionSerializer(version)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EssayVersionListView(generics.ListAPIView):
    serializer_class = EssayVersionSerializer

    def get_queryset(self):
        return EssayVersion.objects.filter(essay_id=self.kwargs['essay_id']).order_by('-submitted_at')

class EssayLatestVersionView(generics.RetrieveAPIView):
    serializer_class = EssayVersionSerializer

    def get(self, request, essay_id):
        latest = EssayVersion.objects.filter(essay_id=essay_id).order_by('-submitted_at').first()
        if not latest:
            return Response({"error": "No versions found"}, status=404)
        serializer = self.get_serializer(latest)
        return Response(serializer.data)
