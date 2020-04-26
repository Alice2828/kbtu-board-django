from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User, TeacherInfo
from users.serializers import UserSerializer, TeacherSerializer
from rest_framework.decorators import api_view, permission_classes


# Create your views here.

class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#  permission_classes = (IsAuthenticated,)


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# permission_classes = (IsAuthenticated,)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def teachers_list(request):
    if request.method == 'GET':
        teachers = TeacherInfo.objects.filter(is_teaching=True)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def teacher_detail(request, teacher_id):
    try:
        teacher = TeacherInfo.objects.get(id=teacher_id)
    except TeacherInfo.DoesNotExist as e:
        return Response({'error': str(e)})

    # Get one objects
    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

        # Update selected objects
    elif request.method == 'PUT':
        serializer = TeacherSerializer(instance=teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({'error': serializer.errors})

        # Delete selected object
    elif request.method == 'DELETE':
        teacher.delete()
        return Response({'deleted': True})
