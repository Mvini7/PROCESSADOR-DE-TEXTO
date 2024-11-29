def processador_texto(texto, **acoes):

    if "contar_palavras" in acoes:
        numero_palavras = len(texto.split())
        print(f"Número de palavras: {numero_palavras}")

    if "contar_letras" in acoes:
        numero_letras = sum(1 for c in texto if c.isalpha())
        print(f"Número de letras: {numero_letras}")

    if "inverter_texto" in acoes:
        texto_invertido = texto[::-1]
        print(f"Texto invertido: {texto_invertido}")

    if "substituir_palavra" in acoes and "nova_palavra" in acoes:

        palavra_antiga = acoes["substituir_palavra"]
        nova_palavra = acoes["nova_palavra"]
        texto = texto.replace(palavra_antiga, nova_palavra)
        print(f"Palavra chave: {palavra_antiga}; será substituida por: {nova_palavra}")
        print(f"Texto com palavras chaves trocadas: {texto}")

    return texto


texto_entrada = "Olá, meu nome é Vinicius e eu sou um Programador Full Stack!"

acoes = {
    "contar_palavras": True,
    "contar_letras": True,
    "inverter_texto": True,
    "substituir_palavra": "Programador Full Stack",
    "nova_palavra": "Desenvolvedor de Varias Areas"
}

print(f"Texto: {texto_entrada}")

resultado = processador_texto(texto_entrada, **acoes)

print(f"Texto final: {resultado}")
