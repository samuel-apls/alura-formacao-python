url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

posicao_interrogacao = url.find('?')

url_base = url[:posicao_interrogacao]
url_parametros = url[posicao_interrogacao + 1:]

parametro_buscado = 'moedaOrigem'

posicao_parametro = url_parametros.find(parametro_buscado)
posicao_valor_parametro = posicao_parametro + len(parametro_buscado) + 1
posicao_e_comercial = url_parametros.find('&', posicao_valor_parametro)

if posicao_e_comercial == -1:
    valor_parametro = url_parametros[posicao_valor_parametro:]
else:
    valor_parametro = url_parametros[posicao_valor_parametro:posicao_e_comercial]

print(f'Posição da interrogação: {posicao_interrogacao}')
print(f'URL da base: {url_base}')
print(f'URL dos parâmetros: {url_parametros}')
print(f'Parêmetro buscado: {parametro_buscado}')
print(f'Posição do parâmetro: {posicao_parametro}')
print(f'Posição do valor do parâmetro: {posicao_valor_parametro}')
print(f'Posição do &: {posicao_e_comercial}')
print(f'Valor do parâmetro: {valor_parametro}')