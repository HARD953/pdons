from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from rest_framework import status
from django.http import Http404

from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class CreateDonateur(APIView):
    def post(self,request):
        data=request.data
        serializer = DonateurMSerializer(data=data)
        error_message=None
        message='Votre inscription a bien été pris en charge merci de faire partir de notre communauté'
        if serializer.is_valid():
            print(data)
            error_message=self.validateDonateur(data)
            if not error_message:
                serializer.save()
                return Response({'message':message,'data':serializer.data,'status':status.HTTP_200_OK})
            return Response({'message':error_message,'status':400})
        return Response({'message':serializer.errors ,'status':400})

    def validateDonateur(self,donateur):
        error_message = None
        if (not donateur['last_name']):
            error_message="Svp entrer votre prenom"
        elif (not donateur['numero']):
            error_message="Svp entrer votre numero de téléphone"
        elif (not donateur['email']):
            error_message="Svp entrer votre email"
        elif (not donateur['user_name'] ):
            error_message="Svp entrer un username de 20 caractere min"
        return error_message

class CreateDonateurOr(APIView):
    def post(self,request):
        data=request.data
        serializer = DonateurOrSerializer(data=data)
        error_message=None
        message='Votre inscription a bien été pris en charge merci de faire partir de notre communauté '
        if serializer.is_valid():
            error_message=self.validateDonateur(data)
            if not error_message:
                serializer.save()
                return Response({'message':message,'data':serializer.data,'status':status.HTTP_200_OK})
            return Response({'message':error_message,'status':status.HTTP_400_BAD_REQUEST})
        return Response({'message':serializer.errors ,'status':status.HTTP_400_BAD_REQUEST})

    def validateDonateur(self,donateur):
        error_message = None
        if (not donateur['last_name']):
            error_message="Svp entrer votre prenom"
        elif (not donateur['numero']):
            error_message="Svp entrer votre numero de téléphone"
        elif (not donateur['email']):
            error_message="Svp entrer votre email"
        elif (not donateur['user_name']):
            error_message="Svp entrer un username de 5 caractere min"
        elif (not donateur['organisations']):
            error_message="Svp entrer le nom de votre organisations"
        return error_message

class EffectuerDonsArg(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=EffectuerDonArge.objects.filter(donateur=self.request.user.user_name)
            serializer=EffectuerArgSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        message='Merci pour votre contribution:\n nous vous contacterons dans peut'
        data=request.data
        if self.request.user.is_authenticated:
            data['donateur']=self.request.user.user_name
            serializer = EffectuerArgSerializer(data=data)
        else:
            data['donateur']='issa'
            serializer = EffectuerArgSerializer(data=data)
        error_message=None
        if serializer.is_valid():
            error_message=self.donEffectuer(data)
            if not error_message:
                serializer.save()
                return Response({'message':message,'data':serializer.data,'status':200})
            return Response({'message':error_message,'status':status.HTTP_400_BAD_REQUEST})
        return Response({'message':serializer.errors ,'status':status.HTTP_400_BAD_REQUEST})

    def donEffectuer(self,donateur):
        error_message = None
        if (not donateur['typeDons']):
            error_message="Svp choisissez le type de don"
        elif (not donateur['categorieV']):
            error_message="Svp entrer la categorie de votre don"
        elif (not donateur['cibleV']):
            error_message="Svp entrer votre email"
        elif (not donateur['montant'] ):
            error_message="Svp entrer un username de 5 caractere min"
        elif (not donateur['provider'] ):
            error_message="Svp entrer un username de 5 caractere min"
        return error_message

class EffectuerDonsObj(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=EffectuerDonNature.objects.filter(donateur=self.request.user.user_name)
            serializer=EffectuerNatSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        message='Merci pour votre contribution:\n nous vous contacterons dans peut'
        data=request.data
        if self.request.user.is_authenticated:
            data['donateur']=self.request.user.user_name
            serializer = EffectuerNatSerializer(data=data)
        else:
            data['donateur']='issa'
            serializer = EffectuerNatSerializer(data=data)
        error_message=None
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            error_message=self.donEffectuer(data)
            if not error_message:
                serializer.save()
                return Response({'message':message,'data':serializer.data,'status':status.HTTP_200_OK})
            return Response({'message':error_message,'status':status.HTTP_400_BAD_REQUEST})
        return Response({'message':serializer.errors ,'status':status.HTTP_400_BAD_REQUEST})

    def donEffectuer(self,donateur):
        error_message = None
        if (not donateur['typeDons']):
            error_message="Svp entrer votre nom"
        elif (not donateur['categorieV']):
            error_message="Svp entrer votre prenom"
        elif (not donateur['cibleV']):
            error_message="Svp entrer votre numero de téléphone"
        elif (not donateur['categorieObjet']):
            error_message="Svp entrer votre email"
        elif (not donateur['typeObjet']):
            error_message="Svp entrer un username de 5 caractere min"
        elif (not donateur['lieu_reception']):
            error_message="Svp entrer un username de 5 caractere min"
        elif (not donateur['Etat']):
            error_message="Svp entrer un username de 5 caractere min"
        return error_message


#Liste des dons détailler ou non par utilisateur
class Argend(generics.RetrieveUpdateDestroyAPIView):
    model=EffectuerDonArge
    permission_classes=[AllowAny]
    serializer_class=EffectuerArgSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["donateur","typeDons","categorieV","cibleV","provider"]
    filterset_fields=["donateur","typeDons","categorieV","cibleV","provider"]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return EffectuerDonArge.objects.filter(donateur=self.request.user.user_name)

class Natured(generics.RetrieveUpdateDestroyAPIView):
    model=EffectuerDonNature
    permission_classes=[AllowAny]
    serializer_class=EffectuerNatSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["donateur","typeDons","categorieV","cibleV","categorieObjet","typeObjet"]
    filterset_fields=["donateur","typeDons","categorieV","cibleV","categorieObjet","typeObjet"]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return EffectuerDonNature.objects.filter(donateur=self.request.user.user_name)

class Argen(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            print(self.request.user)
            dons=EffectuerDonArge.objects.filter(donateur=self.request.user.user_name)
            serializer=EffectuerArgSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

class Nature(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=EffectuerDonNature.objects.filter(donateur=self.request.user.user_name)
            serializer=EffectuerNatSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})


class CibleArgent(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            print(self.request.user)
            dons=EffectuerDonArge.objects.filter(cibleV=self.request.user.user_name,affecter=False)
            serializer=EffectuerArgSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

class CibleNature(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=EffectuerDonNature.objects.filter(cibleV=self.request.user.user_name,affecter=False)
            serializer=EffectuerNatSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

            
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DetailConecter(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=DonateurUser.objects.filter(user_name=self.request.user.user_name)
            serializer=DonateurOrSerializer(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})