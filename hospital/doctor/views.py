from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Doctor
from .serializers import DoctorSerializer
from django.views.decorators.csrf import csrf_exempt
import io

@csrf_exempt
def home(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)

        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Doctor Created'}, status=201)

        return JsonResponse(serializer.errors, status=400)

    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)


@csrf_exempt
def doctor_detail(request, id):
    try:
        doctor = Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return JsonResponse({'error': 'Doctor Not Found'}, status=404)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        serializer = DoctorSerializer(doctor, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Doctor Updated'})
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        doctor.delete()
        return JsonResponse({'msg': 'Doctor Deleted'})

    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
