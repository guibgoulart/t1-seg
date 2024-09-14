ALFABETO = "abcdefghijklmnopqrstuvwxyz"

# Método para descriptografar o texto cifrado usando a chave
def descriptografar(texto_cifrado, chave):
    texto_descriptografado = []
    chave = chave.lower()

    j = 0  # Índice para a chave
    for i in range(len(texto_cifrado)):
        c = texto_cifrado[i]
        if c < 'a' or c > 'z':  # Se o caractere não for uma letra, adiciona-o diretamente
            texto_descriptografado.append(c)
            continue

        deslocamento = ord(chave[j]) - ord('a')  # Calcula o deslocamento com base na chave
        # Ajuste: assegura que o resultado fique dentro dos limites de 'a' a 'z'
        descriptografado = chr(((ord(c) - ord('a') - deslocamento + 26) % 26) + ord('a'))
        texto_descriptografado.append(descriptografado)

        # Move para o próximo caractere da chave (cíclico)
        j = (j + 1) % len(chave)

    return ''.join(texto_descriptografado)

# Exemplo de uso 
