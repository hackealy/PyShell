from pyngrok import ngrok

# Definir a porta e protocolo para uso no túnel
port = 5000
protocol = "http"

# Criar o túnel
tunnel = ngrok.connect(port, protocol)

# Imprimir a URL gerada pelo Pyngrok
print("URL do túnel: ", tunnel.public_url)

# Usar o túnel para permitir o acesso à aplicação local pela internet

# ...

# Fechar o túnel quando a aplicação for finalizada
ngrok.disconnect(tunnel.public_url)
