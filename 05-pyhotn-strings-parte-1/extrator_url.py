import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''   

    def valida_url(self):
        if not self.url:
            raise ValueError('URL não está vazia')
        
        padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao.match(self.url)
        if not match:
            raise ValueError('A URL não é válida')
    
    def get_url_base(self):
        posicao_interrogacao = self.url.find('?')
        url_base = self.url[:posicao_interrogacao]
        return url_base

    def get_url_parametros(self):
        posicao_interrogacao = self.url.find('?')
        url_parametros = self.url[posicao_interrogacao + 1:]
        return url_parametros
        
    def get_valor_parametro(self, parametro_buscado):
        posicao_parametro = self.get_url_parametros().find(parametro_buscado)
        posicao_valor_parametro = posicao_parametro + len(parametro_buscado) + 1
        posicao_e_comercial = self.get_url_parametros().find('&', posicao_valor_parametro)

        if posicao_e_comercial == -1:
            valor_parametro = self.get_url_parametros()[posicao_valor_parametro:]
        else:
            valor_parametro = self.get_url_parametros()[posicao_valor_parametro:posicao_e_comercial]
        return valor_parametro
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return f'URL: {self.url}\nURL base: {self.get_url_base()}\nURL parâmetros: {self.get_url_parametros()}'

    def __eq__(self, comparado):
        return self.url == comparado.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")

print(f'O tamanho da URL é: {len(extrator_url)}')
print(extrator_url)
print(f'Valor do parâmetro "quantidade": {valor_quantidade}')
print(f'Os objetos são idênticos: {extrator_url == extrator_url2}')
