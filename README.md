# PyShell
Cliente/Servidor/Tunnel em Python para conexao remota.

Para executar o "reverse shell", precisamos fazer o seguinte:

Execute o script do servidor em seu sistema local:
$python3 server.py

Crie um túnel local para a internet, usando a biblioteca "pyngrok" ou outro método que você preferir.

Copie o endereço IP público ou a URL gerada pelo túnel e insira-o no script do cliente.

Envie o script do cliente para o sistema remoto e execute-o.

O cliente irá se conectar ao servidor local através do túnel criado, e você poderá executar comandos no sistema remoto digitando-os no terminal do script do servidor.
