
# Mensagem para Whatsapp via "linha de comando"

Enviar mensagem para o Whatsapp através de "linha de comando", utilizando Python e Selenium.

> O desenvolvimento foi feito em Linux (Fedora 28).

## Requisitos
* Python 3
* Navegador Firefox
* Interface Gráfica (SO)
* Celular com Whatsapp instalado

## Instalação
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Execução

### 1 - Execute em seu terminal
```
$ python send.py -R "Nome do Contato" -M "Mensagem a ser enviada"
```
Onde **-R** é o nome do seu contato que esta cadastrado previamente em seu Whatsapp (deve ser idêntico ao cadastrado), e **-M** é a mensagem a ser enviada.

### 2 - O site https://web.whatsapp.com/ irá abrir em seu navegador Firefox e será necessário fazer a leitura do QRCODE.

### 3 - Após a leitura é necessário pressionar enter no terminal para continuar com o envio da mensagem.

### 4 - A mensagem será enviada e o navegador será fechado.
