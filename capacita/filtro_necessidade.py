from .models import *
from .forms import *

def necessidade_query(area,nivel,plano,turno, qtd_servidor):
    if (area and nivel and plano and turno and qtd_servidor):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_nivel = nivel, cod_plano_capacitacao = plano, cod_turno = turno, qtd_servidor__range = (qtd_servidor - 2, qtd_servidor + 2))
    if (area and nivel and (not plano) and turno and qtd_servidor):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_nivel = nivel, cod_turno = turno, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if (area and (not nivel) and plano and turno and qtd_servidor): 
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_plano_capacitacao = plano, cod_turno = turno, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if ((not area) and nivel and plano and turno and qtd_servidor):
        necessidades = Necessidade.objects.filter(cod_plano_capacitacao = plano, cod_nivel = nivel, cod_turno = turno, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if (area and (not nivel) and (not plano) and turno and qtd_servidor):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_turno = turno, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if ((not area) and nivel and (not plano) and turno and qtd_servidor):
         necessidades = Necessidade.objects.filter(cod_nivel = nivel, cod_turno = turno, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if ((not area) and (not nivel) and plano and turno and qtd_servidor):
         necessidades = Necessidade.objects.filter(cod_plano_capacitacao = plano, cod_turno = turno, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if ((not area) and (not nivel) and (not plano) and turno and qtd_servidor):
         necessidades = Necessidade.objects.filter(cod_turno = turno, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if (area and nivel and plano and (not turno) and qtd_servidor):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_nivel = nivel, cod_plano_capacitacao = plano, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if (area and nivel and (not plano) and (not turno) and qtd_servidor):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_nivel = nivel, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if (area and (not nivel) and plano and (not turno) and qtd_servidor): 
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_plano_capacitacao = plano, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if ((not area) and nivel and plano and (not turno) and qtd_servidor):
        necessidades = Necessidade.objects.filter(cod_plano_capacitacao = plano, cod_nivel = nivel, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if (area and (not nivel) and (not plano) and (not turno) and qtd_servidor):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if ((not area) and nivel and (not plano) and (not turno) and qtd_servidor):
         necessidades = Necessidade.objects.filter(cod_nivel = nivel, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if ((not area) and (not nivel) and plano and (not turno) and qtd_servidor):
         necessidades = Necessidade.objects.filter(cod_plano_capacitacao = plano, qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if ((not area) and (not nivel) and (not plano) and (not turno) and (qtd_servidor)):
         necessidades = Necessidade.objects.filter(qtd_servidor__range = (qtd_servidor - 1, qtd_servidor + 1))
    if (area and nivel and plano and turno and (not qtd_servidor)):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_nivel = nivel, cod_plano_capacitacao = plano, cod_turno = turno)
    if (area and nivel and (not plano) and turno and (not qtd_servidor)):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_nivel = nivel, cod_turno = turno)
    if (area and (not nivel) and plano and turno and (not qtd_servidor)): 
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_plano_capacitacao = plano, cod_turno = turno)
    if ((not area) and nivel and plano and turno and (not qtd_servidor)):
        necessidades = Necessidade.objects.filter(cod_plano_capacitacao = plano, cod_nivel = nivel, cod_turno = turno)
    if (area and (not nivel) and (not plano) and turno and (not qtd_servidor)):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_turno = turno)
    if ((not area) and nivel and (not plano) and turno and (not qtd_servidor)):
         necessidades = Necessidade.objects.filter(cod_nivel = nivel, cod_turno = turno)
    if ((not area) and (not nivel) and plano and turno and (not qtd_servidor)):
         necessidades = Necessidade.objects.filter(cod_plano_capacitacao = plano, cod_turno = turno)
    if ((not area) and (not nivel) and (not plano) and turno and (not qtd_servidor)):
         necessidades = Necessidade.objects.filter(cod_turno = turno)
    if (area and nivel and plano and (not turno) and (not qtd_servidor)):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_nivel = nivel, cod_plano_capacitacao = plano)
    if (area and nivel and (not plano) and (not turno) and (not qtd_servidor)):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_nivel = nivel)
    if (area and (not nivel) and plano and (not turno) and (not qtd_servidor)): 
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area, cod_plano_capacitacao = plano)
    if ((not area) and nivel and plano and (not turno) and (not qtd_servidor)):
        necessidades = Necessidade.objects.filter(cod_plano_capacitacao = plano, cod_nivel = nivel)
    if (area and (not nivel) and (not plano) and (not turno) and (not qtd_servidor)):
        necessidades = Necessidade.objects.filter(cod_sub_area_conhecimento_id__cod_area_conhecimento = area)
    if ((not area) and nivel and (not plano) and (not turno) and (not qtd_servidor)):
         necessidades = Necessidade.objects.filter(cod_nivel = nivel)
    if ((not area) and (not nivel) and plano and (not turno) and (not qtd_servidor)):
         necessidades = Necessidade.objects.filter(cod_plano_capacitacao = plano)
    if ((not area) and (not nivel) and (not plano) and (not turno) and (not qtd_servidor)):
         necessidades = Necessidade.objects.all()

    return necessidades