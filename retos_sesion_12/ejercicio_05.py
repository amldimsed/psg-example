""""
Nombre: Jhon Doe
Gustos musicales: rock,pop,jazz
"""
usuario = {'registro1':{'nombre':'Jhon Doe', 'Gustos_musicales':{'rock', 'pop', 'jazz'}}}

conjunto = usuario['registro1']['Gustos_musicales']

if usuario['registro1']['nombre']:
    musica_lista = list(conjunto)
    print('Si tiene la musica rock: ', musica_lista) if ('rock' in musica_lista) else print('no hay registro')
else:
    print('no hay nombre')