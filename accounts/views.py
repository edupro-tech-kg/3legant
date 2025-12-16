from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserProfileSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_api(request):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data)
