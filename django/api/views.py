from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Greeting
from .serializer import GreetingSerializer
#defining get request
@api_view(['GET'])
def greet(request):
    #defining the message to be received
    greeting = Greeting(message="Hey Yinka!")
    serializer = GreetingSerializer(greeting)
    return Response(serializer.data)