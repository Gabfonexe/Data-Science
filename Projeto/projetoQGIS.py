# Importe as bibliotecas necessárias
from qgis.core import QgsProject, QgsVectorLayer, QgsGeometryChecker
from qgis.gui import QgsMessageBar

# Nome das camadas
camada_terrenos = 'terrenos'
camada_divisas = 'divisas'
camada_edificacoes = 'edificacoes'
camada_tetos_pavimentos = 'tetos_pavimentos'

# Acesse o projeto QGIS
projeto = QgsProject.instance()

# Função para verificar e corrigir erros de topologia
def corrigir_topologia(camada_edficacoes):
    # Obtenha a camada
    camada = projeto.mapLayersByName(camada_edficacoes)[0]
    
    # Verifique erros de topologia
    checker = QgsGeometryChecker(camada)
    erros = checker.checkGeometry()
    
    # Corrija erros de topologia
    if erros:
        camada.startEditing()
        for erro in erros:
            erro.fixGeometry()
        camada.commitChanges()
        
        # Atualize a exibição
        camada.triggerRepaint()
        
        # Exiba uma mensagem de sucesso
        msg = f'Erros de topologia corrigidos na camada {camada_nome}.'
        iface.messageBar().pushMessage('Sucesso', msg, level=QgsMessageBar.SUCCESS)
    else:
        msg = f'Nenhum erro de topologia encontrado na camada {camada_nome}.'
        iface.messageBar().pushMessage('Informação', msg, level=QgsMessageBar.INFO)

# Execute a função de correção de topologia para cada camada
corrigir_topologia(camada_terrenos)
corrigir_topologia(camada_divisas)
corrigir_topologia(camada_edificacoes)
corrigir_topologia(camada_tetos_pavimentos)
