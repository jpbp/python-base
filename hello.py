#!/usr/bin/env python3

'''Hello world multi linguas.

Dependendo da lingua configurada no ambiente o programa exibe a msg 
correspondente

Como usar: 

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py

'''
__version__ = "0.0.1"
__autor__ = "João Paulo"
__licence__ = "Unlicense"

import os

#current_language = "en_US"
current_language = os.getenv("LANG","en_US")[:5]
msg="Hello, World"
if current_language == "pt_BR":
    msg="Olá, Mundo!"
elif current_language == "it_IT":
    msg="Ciao, Mondo!"

print(msg)