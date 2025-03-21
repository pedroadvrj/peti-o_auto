import pandas as pd
import os
import docxtpl
import tkinter as tk
from datetime import datetime
import retorna_comarca_teste




def main():
    caminho_modelo_pag = "modelo_light_pag.docx"
    caminho_modelo_mp = "modelo_light_mandadopagamento.docx"
    caminho_modelo = "modelo_light.docx"
    caminho_modelo_habilitacao = "modelo_habilitacao.docx"
    pasta_saida = datetime.now().strftime("%d-%m-%Y")
    

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    print("Escolha o texto da petição:"
        "\n1 - mandado de pagamento"
        "\n2 - petição de acordo"
        "\n3 - petição cumprimento geral obrigação"
        "\n4 - petição cumprimento geral obrigação e honorários periciais"
        "\n5 - petição cumprimento geral de acórdão"
        "\n6 - petição em provas(prova contabil)"
        "\n7 - petição pagando valor exequendo"
        "\n8 - petição manifestação sobre cálculo judicial"
        "\n9 - embargos de declaração"
        "\n10 - habilitação"

        )

    numero_texto = str(input("Digite o número do texto escolhido: "))

    if numero_texto in ["2", "3", "4", "5", "7"]:
        documento = docxtpl.DocxTemplate(caminho_modelo_pag)

    elif numero_texto == "1":
        documento = docxtpl.DocxTemplate(caminho_modelo_mp)

    elif numero_texto == "10":
        documento = docxtpl.DocxTemplate(caminho_modelo_habilitacao)
    
    else:
        documento = docxtpl.DocxTemplate(caminho_modelo)


    criar_documento_personalizado(pasta_saida, documento, numero_texto)





def criar_documento_personalizado(pasta_saida, documento, numero_texto):
    numero_processo = str(input("Digite o número do processo: "))

    nome_parte = str(input("Digite o nome da parte: "))

    vara_origem = retorna_comarca_teste.busca_comarca(numero_processo)

  

    texto_peticao = {"1": """informar o devido recolhimento das custas para expedição do mandado de pagamento, em favor da ré, light, bem como informar, abaixo, os dados bancários, para transferência dos valores remanescentes.""",

    "2": """vem, a presença de V. Exa comprovar o cumprimento da obrigação de pagar e de fazer pactuadas entre as partes por transação judicial (index. ).
    Pelo exposto, vem requerer a V. Exa. a intimação da parte autora para que oferte ampla quitação em relação a obrigação cumprida.""",
    
    "3": """vem, a presença de V. Exa comprovar o cumprimento da obrigação de pagar e fazer determinada por este Juízo em sentença, conforme comprovante de depósito, planilha de cálculos e telas comprobatórias do cumprimento do decreto condenatório.""",
    
    "4":"""vem, a presença de V. Exa comprovar o cumprimento da obrigação de pagar e fazer determinada por este Juízo em sentença, conforme comprovante de depósito, planilha de cálculos e telas comprobatórias do cumprimento do decreto condenatório. Por fim, vem requerer a V. Exa. a juntada do comprovante de depósito judicial referente ao pagamento dos honorários periciais, no valor de R$......""",
    
    "5": """vem, a presença de V. Exa comprovar o cumprimento da obrigação de pagar determinada pelo V. acórdão, conforme comprovante de depósito e planilha de cálculos em anexo.""",
    
    "6": """vem, a presença de V. Exa.,requerer a produção de prova contábil, por meio da Central de Cálculos do Tribunal de Justiça do Estado do Rio de Janeiro (TJRJ), cujas custas judiciais necessárias serão recolhidas após o deferimento da prova.""",
    "7": """vem, a presença de V. Exa. comprovar o cumprimento integral do valor exequendo apontado pelo exequente (index. xxxxxxxxx). Ressalta-se que o exequente executa a quantia dexxxxxxxxxxxx (xxxxxxxxxxx), porquanto, a executada comprova neste oportunidade o pagamento da quantia total de R$ xxxxxxxxxxx (xxxxxxxxxxxxxxxx). Portanto, diante do pagamento integral da condenação, vem requerer a V. Exa. a intimação do exequente para que oferte ampla quitação em relação a obrigação ora cumprida.""",
    "8": """vem, a presença de V. Exa., em atenção aos cálculos apresentados pela Central de Cálculos Judiciais (index. xxxx), expor para ao final requerer o seguinte:""",
    "9": """em atenção a decisão que ............................, interpor o presente recurso de EMBARGOS DE DECLARAÇÃO, na forma do art. 1.022 e seguintes do CPC, pelas razões de fato e de direito que a seguir expõe:""",
    "10": """ """}

    texto_selecionado = texto_peticao[numero_texto]


    contexto = {
        "NUMERO_PROCESSO": numero_processo,
        "NOME_PARTE": nome_parte,
        "VARA_ORIGEM": vara_origem,
        "texto_escolhido": texto_selecionado
    }


    pasta_parte = os.path.join(pasta_saida, nome_parte)
    os.makedirs(pasta_parte)

    documento.render(contexto)

    nome_arquivo = os.path.join(pasta_parte, f"{nome_parte}.docx")

    documento.save(nome_arquivo)


    print(f"Arquivo gerado: {nome_arquivo}")

    print("Processo concluído!")

    os.startfile(nome_arquivo)







main()

