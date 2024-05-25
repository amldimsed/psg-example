habitats = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}},
             "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}}
print(habitats['amazonas']['especies'])

#1 Añade al diccionario de habitats 2 habitats más usando update()
habitats.update(Valle_México = {'especies':{'Ajolote'}},
                Antártico_Atlántico = {'especies':{'Ninge','Ballena franca austral','godzi__a'}})
print(habitats,'\n')

#2 Existe en el diccionario de habitats el habitat 'amazonas'?
dato = habitats.get('amazonas')
dato != None and print("Si existe ", dato,'\n\n') 
dato == None and print("no existe",'\n\n')

#3 Añade al diccionario de amazonas la especie 'anaconda'

habitats.update(amazonas = {"especies": {"tigre", "mono", "guacamayo",'anaconda'}})
print(habitats["amazonas"]["especies"])
