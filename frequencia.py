from collections import defaultdict
import string

class Idioma:
    PORTUGUES = "PORTUGUES"
    INGLES = "INGLES"

# Alfabeto
ALFABETO = list(string.ascii_lowercase)

# Frequências para Português e Inglês
FREQUENCIAS_PORT = {
    'a': 14.634, 'b': 1.043, 'c': 3.882, 'd': 4.992, 'e': 12.570, 'f': 1.023, 'g': 1.303, 'h': 0.781, 
    'i': 6.186, 'j': 0.397, 'k': 0.015, 'l': 2.779, 'm': 4.738, 'n': 4.446, 'o': 9.735, 'p': 2.523, 
    'q': 1.204, 'r': 6.530, 's': 6.805, 't': 4.336, 'u': 3.639, 'v': 1.575, 'w': 0.037, 'x': 0.253, 
    'y': 0.006, 'z': 0.470
}

FREQUENCIAS_ING = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 
    'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 
    'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 
    'y': 1.974, 'z': 0.074
}

frequencias_atuais = defaultdict(float)
texto_cifrado = ""

def set_frequencias(idioma):
    global frequencias_atuais
    if idioma == Idioma.INGLES:
        frequencias_atuais = FREQUENCIAS_ING
    else:
        frequencias_atuais = FREQUENCIAS_PORT

def inicializar_frequencias():
    # Esse método é desnecessário em Python, pois usamos dicionários diretamente
    pass

# Divide o texto cifrado em N grupos com base no comprimento da chave
def dividir_em_grupos(texto_cifrado, comprimento_chave):
    grupos = [list() for _ in range(comprimento_chave)]

    for i, c in enumerate(texto_cifrado):
        grupos[i % comprimento_chave].append(c)

    # Transformar cada grupo em uma string
    return ["".join(grupo) for grupo in grupos]

# Função para analisar a frequência dos grupos e determinar a chave mais provável
def analisar_frequencia_dos_grupos(grupos, idioma):
    set_frequencias(idioma)
    chave = []

    for grupo in grupos:
        letra_chave_mais_provavel = 'a'
        min_diferenca = float('inf')

        for deslocamento in range(len(ALFABETO)):
            soma_quadrados_diferencas = 0

            for letra in ALFABETO:
                indice_original = (ord(letra) - ord('a') - deslocamento + len(ALFABETO)) % len(ALFABETO)
                letra_original = ALFABETO[indice_original]

                freq_observada = grupo.count(letra) / len(grupo) if len(grupo) > 0 else 0
                freq_esperada = frequencias_atuais.get(letra_original, 0.0)

                if freq_esperada > 0:
                    soma_quadrados_diferencas += (freq_observada - freq_esperada) ** 2 / freq_esperada

            if soma_quadrados_diferencas < min_diferenca:
                min_diferenca = soma_quadrados_diferencas
                letra_chave_mais_provavel = ALFABETO[deslocamento]

        chave.append(letra_chave_mais_provavel)

    return "".join(chave)
