from django.urls import path
from .views import FileUploadView, DataRecordListView, DataRecordHTMLView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('data/json/', DataRecordListView.as_view(), name='data-json'),
    path('data/html/', DataRecordHTMLView.as_view(), name='data-html'),
]
