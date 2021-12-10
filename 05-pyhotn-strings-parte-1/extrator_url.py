class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url(url)
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''   

    def valida_url(self, url):
        if not self.url:
            raise ValueError('URL não está vazia')
    
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

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
