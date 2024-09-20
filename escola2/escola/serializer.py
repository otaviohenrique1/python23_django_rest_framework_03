from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ["id", "nome", "email", "cpf", "data_nascimento", "celular"]


    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({"cpf": "O CPF deve ter um valor válido."})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({"nome": "O nome só pode ter letras!"})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({"celular": "O celular precisa seguir o modelo: 86 99999-9999 (respeitando traços e espaços)."})
        return dados

    # def validate_cpf(self, cpf: str):
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError("O CPF deve ter 11 digitos!")
    #     return cpf
    
    # def validate_nome(self, nome: str):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("O nome só pode ter letras!")
    #     return nome
    
    # def validate_celular(self, celular: str):
    #     if len(celular) != 13:
    #         raise serializers.ValidationError("O celular precisa ter 13 digitos!")
    #     return celular


class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ["id", "nome", "email", "celular"]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        # fields = "__all__ "
        fields = ["codigo", "descricao", "nivel"]


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasEstudantesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source="estudante.nome")

    class Meta:
        model = Matricula
        fields = ["estudante_nome"]
