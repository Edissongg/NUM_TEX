# convertir/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .convertir_numero import convertir_numero_a_texto
from .serializers import NumeroSerializer

class ConvertirNumero(APIView):
    def post(self, request):
        # Validar los datos de entrada
        serializer = NumeroSerializer(data=request.data)
        if serializer.is_valid():
            numero = serializer.validated_data['numero']
            try:
                # Convertir el número a letras
                resultado = convertir_numero_a_texto(numero)
                return Response({'numero': numero, 'letras': resultado})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
