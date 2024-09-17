import kasiski
import frequencia
import vigenere

textoCifrado = open("textos/cipher31.txt", "r").read()
palavrasRepetidas = kasiski.get_repeating_words(textoCifrado)
distancias = kasiski.get_distances(textoCifrado,palavrasRepetidas)
tamanhoChave = kasiski.encontrar_comprimento_chave_provavel(distancias)

grupos = frequencia.dividir_em_grupos(textoCifrado,tamanhoChave)
chave = frequencia.analisar_frequencia_dos_grupos(grupos,frequencia.Idioma.PORTUGUES)

textoClaro = vigenere.descriptografar(textoCifrado,chave)
print(textoClaro)
print(tamanhoChave)
print(chave)