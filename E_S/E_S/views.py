# from django.http import JsonResponse
# from .models import Profile
# from .serializers import ProfileSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# @api_view(['GET','POST'])
# def profile_list(request, format = None):


#     # get all the profiles
#     # serialize them
#     # return json


#     if request.method == 'GET':
#         profile  = Profile.objects.all()
#         serializer = ProfileSerializer(profile, many=True)

#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)



        
# @api_view(['GET','PUT','DELETE'])

# def profile_details(request, id,format = None):

#     try:

#         profile = Profile.objects.get(pk=id)
#     except Profile.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
    
#     if request.method == 'GET':
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)
        
#     elif request.method == 'PUT':
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)