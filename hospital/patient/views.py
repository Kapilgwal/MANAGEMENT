from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .serializers import PatientSerializer
from .models import Patient
from django.views.decorators.csrf import csrf_exempt
import io

@csrf_exempt
def patient_list(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Patient created'}, status=201)
        
        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def patient_detail(request, id):
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        serializer = PatientSerializer(patient, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Patient updated'})
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patient.delete()
        return JsonResponse({'msg': 'Patient deleted'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
