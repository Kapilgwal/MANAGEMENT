from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
import io

@csrf_exempt
def mapping_list_create(request):
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id', None)

        if patient_id:
            mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        else:
            mappings = PatientDoctorMapping.objects.all()

        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        try:
            stream = io.BytesIO(request.body)
            data = JSONParser().parse(stream)

            # Prevent duplicate mapping
            if PatientDoctorMapping.objects.filter(
                patient=data.get('patient'), doctor=data.get('doctor')
            ).exists():
                return JsonResponse({'error': 'Mapping already exists'}, status=400)

            serializer = PatientDoctorMappingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'Mapping created'}, status=201)

            return JsonResponse(serializer.errors, status=400)

        except Exception:
            return JsonResponse({'error': 'Invalid input'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def mapping_delete(request, id):
    if request.method == 'DELETE':
        try:
            mapping = PatientDoctorMapping.objects.get(id=id)
            mapping.delete()
            return JsonResponse({'msg': 'Mapping deleted'})
        except PatientDoctorMapping.DoesNotExist:
            return JsonResponse({'error': 'Mapping not found'}, status=404)
        except Exception:
            return JsonResponse({'error': 'Invalid input'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
