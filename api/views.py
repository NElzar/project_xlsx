from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DataRecord
from .serializers import DataRecordSerializer
import pandas as pd
from django.http import HttpResponse
from django.template.loader import render_to_string
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_description="Upload an Excel file to import data records.",
        manual_parameters=[
            openapi.Parameter(
                'file',
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                description="Upload an Excel file (.xlsx or .xls)"
            )
        ],
        responses={
            201: 'Data imported successfully',
            400: 'No file uploaded or invalid file format',
        }
    )
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        df = pd.read_excel(file)
        records = []
        for _, row in df.iterrows():
            ne = row['ne']
            address = row['address']
            product_status = row['status']

            latitude, longitude = map(float, row['coordinates'].split(','))
            gsm = umts = lte = False
            if pd.notna(row['technology']):
                gsm = 'gsm' in row['technology'].lower()
                umts = 'umts' in row['technology'].lower()
                lte = 'lte' in row['technology'].lower()

            record = DataRecord(
                ne=ne,
                address=address,
                latitude=latitude,
                longitude=longitude,
                gsm=gsm,
                umts=umts,
                lte=lte,
                status=product_status
            )
            records.append(record)

        DataRecord.objects.bulk_create(records)
        return Response({'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED)


class DataRecordListView(generics.ListAPIView):
    queryset = DataRecord.objects.all()
    serializer_class = DataRecordSerializer


class DataRecordHTMLView(APIView):
    def get(self, request):
        data = DataRecord.objects.all()
        html = render_to_string('data_table.html', {'data': data})
        return HttpResponse(html)
