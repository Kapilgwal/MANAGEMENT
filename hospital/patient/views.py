from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import PatientSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
import io 



@csrf_exempt
def home(request):

    if request.method == 'GET':
        id = request.GET.get('id',None)

        if id:
            try:
                doc = Patient.objects.get(id = id)
                serialzer = PatientSerializer(doc)
                return JsonResponse(serialzer.data,safe = False)
            
            except:
                return JsonResponse({'error' : 'Patient not found'})
        
        else:
            doc = Patient.objects.all()
            serialzer = PatientSerializer(doc,many = True)
            return JsonResponse(serialzer.data , safe = False)


    elif request.method == 'POST':
        json_data = request.body;
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serialzer = PatientSerializer(data = pythondata)

        if serialzer.is_valid():
            serialzer.save()
            res = {'msg' : 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
    
        json_data = JSONRenderer().render(serialzer.errors)
        return HttpResponse(json_data,content_type = 'application/json')


    elif request.method == 'PUT':
        try : 
            stream = io.BytesIO(request.body)
            data = JSONParser().parse(stream)
            id = data.get('id')
            doc = Patient.objects.get(id = id)
            serialzer = PatientSerializer(doc,data = data,partial = True)

            if serialzer.is_valid():
                serialzer.save()
                return JsonResponse({'msg' : 'Data Updated'})
            return JsonResponse(serialzer.errors, status = 400)
        
        except Patient.DoesNotExist:
            return JsonResponse({'error' : 'Invalid input'}, status = 400)
        
        except Exception:
            return JsonResponse({'error' : 'Invalid input'}, status = 400)

    elif request.method == 'DELETE':
        try:
            stream = io.BytesIO(request.body)
            data = JSONParser().parse(stream)
            id = data.get('id')
            doc = Patient.objects.get(id=id)
            doc.delete()
            return JsonResponse({'msg': 'Data deleted'})
        except Patient.DoesNotExist:
            return JsonResponse({'error': 'Patient not found'}, status=404)
        except Exception:
            return JsonResponse({'error': 'Invalid input'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
