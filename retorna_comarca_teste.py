import requests
import json
import re

def chamada_api(numero_processo):
  url = "https://api-publica.datajud.cnj.jus.br/api_publica_tjrj/_search"  # Substitua isso pela URL da sua API

  headers = {
    'Authorization': 'ApiKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw==',
    'Content-Type': 'application/json'
  }

  payload = json.dumps({
    "query": {
        "match": {
            "numeroProcesso": numero_processo
        }
    }
  })

  response = requests.post(url, headers=headers, data=payload)

  # Imprimir o resultado da solicitação
  retorno = response.json()
  return retorno


def retirada_pontos_numerocnj(numero):
  dicionario = {".": "", "-": ""}
  for letras in dicionario.keys():
    numero = numero.replace(letras, "")
  return numero


def retorna_numero_vara(retorno):
    vara = re.findall(r'\d+', retorno)
    return vara

dados = {
    "0209": "Regional da Barra da Tijuca",
    "0207": "Regional da Ilha do Governador",
    "0210": "Regional da Leopoldina",
    "0211": "Regional da Pavuna",
    "0212": "Regional da Região Oceânica",
    "0087": "Regional de Alcântara",
    "0204": "Regional de Bangu",
    "0205": "Regional de Campo Grande",
    "0079": "Regional de Itaipava",
    "0203": "Regional de Jacarepaguá",
    "0202": "Regional de Madureira",
    "0206": "Regional de Santa Cruz",
    "0208": "Regional do Méier",
    "0001": "Comarca da Capital",
    "0255": "Comarca da Capital - 1ª Vara da Infância, Juventude e Idoso",
    "0256": "Comarca da Capital - 2ª Vara da Infância, Juventude e Idoso",
    "0251": "Comarca da Capital - Copacabana",
    "0252": "Comarca da Capital - Lagoa",
    "0253": "Comarca da Capital - Tijuca",
    "0254": "Comarca da Capital - Vila Isabel",
    "0003": "Comarca de Angra dos Reis",
    "0052": "Comarca de Araruama",
    "0005": "Comarca de Arraial do Cabo",
    "0006": "Comarca de Barra do Piraí",
    "0007": "Comarca de Barra Mansa",
    "0008": "Comarca de Belford Roxo",
    "0009": "Comarca de Bom Jardim",
    "0010": "Comarca de Bom Jesus de Itabapoana",
    "0078": "Comarca de Búzios",
    "0011": "Comarca de Cabo Frio",
    "0012": "Comarca de Cachoeiras de Macacu",
    "0013": "Comarca de Cambuci",
    "0014": "Comarca de Campos dos Goytacazes",
    "0015": "Comarca de Cantagalo",
    "0084": "Comarca de Carapebus / Quissamã",
    "0016": "Comarca de Carmo",
    "0017": "Comarca de Casimiro de Abreu",
    "0018": "Comarca de Conceição de Macabu",
    "0019": "Comarca de Cordeiro",
    "0020": "Comarca de Duas Barras",
    "0021": "Comarca de Duque de Caxias",
    "0022": "Comarca de Engenheiro Paulo de Frontin",
    "0073": "Comarca de Guapimirim",
    "0069": "Comarca de Iguaba Grande",
    "0023": "Comarca de Itaboraí",
    "0024": "Comarca de Itaguaí",
    "0080": "Comarca de Italva",
    "0025": "Comarca de Itaocara",
    "0026": "Comarca de Itaperuna",
    "0081": "Comarca de Itatiaia",
    "0083": "Comarca de Japeri",
    "0027": "Comarca de Laje do Muriaé",
    "0028": "Comarca de Macaé",
    "0029": "Comarca de Magé",
    "0075": "Comarca de Magé - Regional de Inhomirim",
    "0030": "Comarca de Mangaratiba",
    "0031": "Comarca de Maricá",
    "0032": "Comarca de Mendes",
    "0033": "Comarca de Miguel Pereira",
    "0034": "Comarca de Miracema",
    "0035": "Comarca de Natividade",
    "0036": "Comarca de Nilópolis",
    "0002": "Comarca de Niterói",
    "0037": "Comarca de Nova Friburgo",
    "0038": "Comarca de Nova Iguaçu",
    "0039": "Comarca de Paracambi",
    "0040": "Comarca de Paraíba do Sul",
    "0041": "Comarca de Paraty",
    "0072": "Comarca de Paty do Alferes",
    "0042": "Comarca de Petrópolis",
    "0082": "Comarca de Pinheiral",
    "0043": "Comarca de Piraí",
    "0044": "Comarca de Porciúncula",
    "0071": "Comarca de Porto Real - Quatis",
    "0067": "Comarca de Queimados",
    "0045": "Comarca de Resende",
    "0046": "Comarca de Rio Bonito",
    "0047": "Comarca de Rio Claro",
    "0048": "Comarca de Rio das Flores",
    "0068": "Comarca de Rio das Ostras",
    "0049": "Comarca de Santa Maria Madalena",
    "0050": "Comarca de Santo Antônio de Pádua",
    "0051": "Comarca de São Fidelis",
    "0070": "Comarca de São Francisco do Itabapoana",
    "0004": "Comarca de São Gonçalo",
    "0053": "Comarca de São João da Barra",
    "0054": "Comarca de São João de Meriti",
    "0076": "Comarca de São José do Vale do Rio Preto",
    "0055": "Comarca de São Pedro da Aldeia",
    "0056": "Comarca de São Sebastião do Alto",
    "0057": "Comarca de Sapucaia",
    "0058": "Comarca de Saquarema",
    "0077": "Comarca de Seropédica",
    "0059": "Comarca de Silva Jardim",
    "0060": "Comarca de Sumidouro",
    "0061": "Comarca de Teresópolis",
    "0062": "Comarca de Trajano de Moraes",
    "0063": "Comarca de Três Rios"
}



def busca_comarca(numero_processo):

  sigla_comarca = numero_processo[-4:]
  numero_enviar_api = retirada_pontos_numerocnj(numero_processo)
  retorno = chamada_api(numero_enviar_api)
  comarca = retorno['hits']['hits'][0]['_source']['orgaoJulgador']['nome']
  nome_comarca = dados[sigla_comarca].upper()
  numero_vara, = retorna_numero_vara(comarca)
  cabecalho = (f"AO JUÍZO DA {numero_vara}ª VARA CÍVEL DA {nome_comarca}")
  print(cabecalho)
  return cabecalho



