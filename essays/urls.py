from django.urls import path
from .views import (
    EssayCreateView,
    EssayVersionUploadView,
    EssayVersionListView,
    EssayLatestVersionView,
)

urlpatterns = [
    path('essays/', EssayCreateView.as_view(), name='essay-create'),
    path('essays/<int:essay_id>/versions/', EssayVersionUploadView.as_view(), name='essay-version-upload'),
    path('essays/<int:essay_id>/versions/', EssayVersionListView.as_view(), name='essay-versions-list'),
    path('essays/<int:essay_id>/latestversion/', EssayLatestVersionView.as_view(), name='essay-latest-version'),
]
