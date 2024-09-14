import math
from collections import defaultdict

# Encontra palavras (grupos de letras) repetidas no texto cifrado.
def get_repeating_words(texto_cifrado):
    words_seen = set()
    repeating_words = set()

    for i in range(len(texto_cifrado) - 2):  # A palavra deve ter no mínimo 3 letras
        current_word = texto_cifrado[i:i + 3]
        if current_word in words_seen:
            repeating_words.add(current_word)
        else:
            words_seen.add(current_word)
    
    return repeating_words

# Calcula as distâncias entre repetições das palavras encontradas.
def get_distances(texto_cifrado, repeating_words):
    last_seen_index = {}
    distances = defaultdict(set)

    for i in range(len(texto_cifrado) - 2):
        current_word = texto_cifrado[i:i + 3]
        if current_word in repeating_words:
            if current_word in last_seen_index:
                distance = i - last_seen_index[current_word]
                distances[current_word].add(distance)
            last_seen_index[current_word] = i
    
    return distances

# Função para calcular os fatores primos de um número (seguindo a lógica fornecida)
def fatores_primos(number):
    fatores = []
    i = 2
    while i <= number // i:
        while number % i == 0:
            fatores.append(i)
            number //= i
        i += 1
    if number > 1:
        fatores.append(number)
    return fatores

# Encontra o comprimento provável da chave com base nas distâncias calculadas.
def encontrar_comprimento_chave_provavel(distancias):
    contagem_fatores = defaultdict(int)

    # Fatora cada distância e conta a frequência dos fatores.
    for distancias_set in distancias.values():
        for distancia in distancias_set:
            fatores = fatores_primos(distancia)
            fatores_unicos = set(fatores)
            for fator in fatores_unicos:
                contagem_fatores[fator] += 1

    # Encontra o fator mais frequente
    comprimento_provavel = max(contagem_fatores, key=contagem_fatores.get, default=1)

    return comprimento_provavel

# Cifra de Vigenere
def cifra_vigenere(texto_claro, chave):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto_claro = texto_claro.upper()
    chave = chave.upper()

    texto_cifrado = []
    chave_repetida = (chave * (len(texto_claro) // len(chave))) + chave[:len(texto_claro) % len(chave)]
    
    for i in range(len(texto_claro)):
        if texto_claro[i] in alfabeto:
            posicao_letra = (alfabeto.index(texto_claro[i]) + alfabeto.index(chave_repetida[i])) % len(alfabeto)
            texto_cifrado.append(alfabeto[posicao_letra])
        else:
            texto_cifrado.append(texto_claro[i])
    
    return ''.join(texto_cifrado)

# Função para testar o m etodo de Kasiski com uma chave conhecida
def testar_metodo_kasiski():
    # Texto em claro
    texto_claro = """On voit parfois, sur la fin de l hiver, le jardinier soucieux de son jardin, se promener le long des espaliers et des treilles. Il examine l  etat des bourgeons et du bois, interroge d un œil attentif les myst erieuses enveloppes que va gonfler et d echirer bientot la seve du printemps. Ces promenades ou l anxi et e se mêle toujours a l esp erance, me rappellent par analogie, une autre promenade, plus troublante encore et plus int eressante, celle que peut faire a travers la jeunesse le penseur pr eoccup e de l avenir. La aussi dort, envelopp ee et pourtant apparente d eja sous le voile qui la recouvre, la grande -4- question de demain. Il germe et grandit dans le cœur des jeunes, il fermente sous leur front des choses plus significatives que celles qu essaie de deviner le jardinier sous l  ecorce des bourgeons.

Int eressante toujours, et toujours digne de la plus sympathique attention, la jeunesse m erite surtout de nous attirer aux  epoques critiques, ou des changements d orientation s annoncent. Ne semble-t-il pas que tel soit le cas a la fin de ce siecle ? Sans doute, c est une erreur grossiere que de confondre les p eriodes de l  evolution humaine avec ces divisions chronologiques factices qu on appelle des siecles. On attribue aux siecles une jeunesse et une vieillesse, on parle de leur aurore et de leur d eclin. Rien ne r epond moins a la r ealit e. Des mouvements puissants ont marqu e la fin de certains siecles ; d autres ont commenc e dans le marasme et la s enilit e. Il n en est pas moins vrai qu il peut se produire une coïncidence entre le terme d une p eriode historique et le terme d un siecle. Tel est, je crois, le cas a l heure pr esente. Nous avons derriere nous tout un vaste d eveloppement, dans lequel on peut remarquer, apres les enthousiasmes -5- juv eniles et les efforts virils d une brillante maturit e, les h esitations et les symptomes de lassitude ordinaires a la vieillesse. Mais, comme l humanit e se renouvelle sans cesse et renait de ses cendres, c est au moment ou les choses anciennes sont arriv ees a leur maximum de d ecr epitude, que les choses neuves se pr eparent."""
    
    # Chave conhecida
    chave = "RAPHAELAMBROSIUSCOSTEAU"
    texto_claro = texto_claro.replace(" ","")
    # Cifrar o texto
    texto_cifrado = cifra_vigenere(texto_claro, chave)
    print(f"Texto cifrado: {texto_cifrado}")
    
    # Passo 1: Encontra palavras repetidas
    repeating_words = get_repeating_words(texto_cifrado)
    print(f"Palavras repetidas: {repeating_words}")
    
    # Passo 2: Calcula as distâncias entre as palavras repetidas
    distancias = get_distances(texto_cifrado, repeating_words)
    print(f"Distâncias: {distancias}")
    
    # Passo 3: Encontra o comprimento provável da chave
    comprimento_chave = encontrar_comprimento_chave_provavel(distancias)
    print(f"Comprimento provável da chave (deve ser {len(chave)}): {comprimento_chave}")

# Executar o teste
testar_metodo_kasiski()
