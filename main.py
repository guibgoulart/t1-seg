import kasiski
import frequencia
import vigenere

texto_claro = """And now   the end is near And so I face the final curtain My friend   I  ll say it clear I  ll state my case   of which I  m certain I  ve lived a life that  s full I traveled each and every highway And more   much more than this I did it my way Regrets   I  ve had a few But then again   too few to mention I did what I had to do And saw it through without exemption I planned each charted course Each careful step along the byway And more   much more than this I did it my way Yes   there were times   I  m sure you knew When I bit off more than I could chew But through it all   when there was doubt I ate it up and spit it out I faced it all   and I stood tall And did it my way I  ve loved   I  ve laughed and cried I  ve had my fill   my share of losing And now   as tears subside I find it all so amusing To think I did all that And may I say   not in a shy way Oh   no   oh   no   not me I did it my way For what is a man   what has he got   If not himself   then he has naught To say the things he truly feels And not the words of one who kneels The record shows I took the blows And did it my way Yes   it was my way"""
chave = "RAPHAELAMBROSIUSCOS"
texto_claro = texto_claro.replace(" ","")
#textoCifrado = kasiski.cifra_vigenere(texto_claro, chave)
textoCifrado = open("textos/portugues.txt", "r").read()
palavrasRepetidas = kasiski.get_repeating_words(textoCifrado)
distancias = kasiski.get_distances(textoCifrado,palavrasRepetidas)
tamanhoChave = kasiski.encontrar_comprimento_chave_provavel(distancias)
print(tamanhoChave)
grupos = frequencia.dividir_em_grupos(textoCifrado,tamanhoChave)
chave = frequencia.analisar_frequencia_dos_grupos(grupos,frequencia.Idioma.PORTUGUES)
print(chave)
textoClaro = vigenere.descriptografar(textoCifrado,chave)
print(textoClaro)
