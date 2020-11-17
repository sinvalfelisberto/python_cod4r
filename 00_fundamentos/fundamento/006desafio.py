trabalho_terca = False
trabalho_quinta = False

tv32 = trabalho_terca != trabalho_quinta
tv50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_quinta or trabalho_terca
saudavel = not(tv32) and not(tv50)
