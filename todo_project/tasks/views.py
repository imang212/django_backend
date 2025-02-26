from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

#vrátím data GET
@api_view(['GET',"POST"])
def Vrat_seznam_ukolu(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

#from django.http import HttpResponse
#from django.template import loader
#def members(request):
#  template = loader.get_template('main.html')
#  return HttpResponse(template.render())
from rest_framework import status

@api_view(['POST'])
def Vloz_ukol(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()  # Save the task
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created task with id
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#metody podle id get, put, delete
from django.shortcuts import get_object_or_404
import cv2
import numpy as np
import os
from django.conf import settings
import uuid
@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # If there's partial data, use partial=True
        partial = not all(field in request.data for field in TaskSerializer.Meta.fields)
        serializer = TaskSerializer(task, data=request.data, partial=partial)

        if serializer.is_valid():
            # Check if image is being updated
            if 'image' in request.data and request.data['image']:
                # Process the new image with OpenCV
                image_file = request.data['image']

                # Save the uploaded file temporarily
                temp_path = os.path.join(settings.MEDIA_ROOT, f'temp_{uuid.uuid4()}.jpg')
                with open(temp_path, 'wb+') as destination:
                    for chunk in image_file.chunks():
                        destination.write(chunk)

                # Process with OpenCV
                img = cv2.imread(temp_path)
                if img is not None:
                    # Resize the image (example: resize to 500x500 pixels)
                    img_resized = cv2.resize(img, (500, 500))

                    # Save the processed image back to the temporary path
                    cv2.imwrite(temp_path, img_resized)

                    # Open the processed file and update the model
                    with open(temp_path, 'rb') as processed_file:
                        task.image.save(f'{uuid.uuid4()}.jpg', processed_file, save=False)

                # Remove temporary file
                if os.path.exists(temp_path):
                    os.remove(temp_path)

            # Save the task with all updated fields
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.utils import timezone
@api_view(['GET'])
def nearest_deadline_task(request):
    now = timezone.now()
    nearest_task = Task.objects.filter(due_date__isnull=False,due_date__gte=now ).order_by('due_date').first()

    if nearest_task is None: nearest_task = Task.objects.filter(due_date__isnull=False).order_by('due_date').first()

    if nearest_task is None: return Response({"detail": "No tasks with deadline found."},status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(nearest_task)
    return Response(serializer.data)

import heapq #následující LeetCode úkoly budou fungovat pomocí heap algoritmu
@api_view(['POST'])
def rotate_array(request):
    try:
        data = request.data; nums = data.get('nums', []); k = data.get('k', 0)
        # ověř vstup
        if not isinstance(nums, list) or not isinstance(k, int): return Response( {"error": "Špatný vstup. 'nums' musí být pole a 'k' musí být int."}, status=status.HTTP_400_BAD_REQUEST)
        n = len(nums) #rohy
        if n == 0 or k % n == 0: return Response({"result": nums})
        k = k % n #normalizace k
        nums.reverse() #1. reverse the entire array
        nums[:k] = reversed(nums[:k]) # 2. Reverse first k elements
        nums[k:] = reversed(nums[k:]) # 3. Reverse remaining elements
        return Response({"result": nums})
    except Exception as e:
        return Response({"error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def kth_largest(request):
    try:
        data = request.data
        nums = data.get('nums', [])
        k = data.get('k', 0)
        # Ověř vstup
        if not isinstance(nums, list) or not isinstance(k, int): return Response({"error": "Špatný vstup. 'nums' musí být pole a 'k' musí být integer."}, status=status.HTTP_400_BAD_REQUEST)

        if k <= 0 or k > len(nums): return Response({"error": f"3patná hodnota pro k. Musí být mezi 1 a {len(nums)}."}, status=status.HTTP_400_BAD_REQUEST)

        min_heap = [] #použití min heap o velikosti k vyhledání k největších elementů, máme O(n log k) komplexitu
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        return Response({"result": min_heap[0]}) #nejmenší element v min heap je kth nejdelší ze všech
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def longest_increasing_path(request):
    try:
        data = request.data
        matrix = data.get('matrix', [])
        # ověř vstup
        if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
            return Response({"error": "Invalid input. 'matrix' must be a 2D array."}, status=status.HTTP_400_BAD_REQUEST)

        if not matrix: return Response({"result": 0})

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0 for _ in range(cols)] for _ in range(rows)] #vytvoříme memo table
        def dfs(i, j): #nadefinujeme funkci pomocí dfs s memo tabulkou
            if memo[i][j] != 0: return memo[i][j] #vrátíme když je dostupné
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] #všechny možné strany
            max_length = 1 #start cesty
            for di, dj in directions: #prijdem všechny strany
                ni, nj = i + di, j + dj #zkontrolujem jestli nová pozice platí a má lepší hodnotu
                if (0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]):
                    max_length = max(max_length, 1 + dfs(ni, nj)) #aktualizujee maximální délku

            memo[i][j] = max_length #uložíme výsledek
            return max_length
        #najdu nejdelší cestu
        max_path = 0
        for i in range(rows):
            for j in range(cols):
                max_path = max(max_path, dfs(i, j))
        return Response({"result": max_path})

    except Exception as e: return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)