from escola.models import Estudante, Curso, Matricula
from escola.serializer import (
    EstudanteSerializer,
    CursoSerializer,
    EstudanteSerializerV2,
    MatriculaSerializer,
    ListaMatriculasEstudantesSerializer,
    ListaMatriculasCursoSerializer,
)
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Estudante.objects.all()
    # serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]
    
    def get_serializer_class(self):
        if self.request.version == "v2":
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    # authentication_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculaEstudante(generics.ListAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudantes_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaMatriculasEstudantesSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaMatriculasCursoSerializer
