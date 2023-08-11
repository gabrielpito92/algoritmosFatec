import math
segundos = input('Por favor, entre com o número de segundos que deseja converter:')
# segundos = 178615
hrs_dias = int(segundos) // 3600
min_seg = ((int(segundos) / 3600) - (int(segundos) // 3600)) *60

if hrs_dias >= 24:
    dias = int(hrs_dias/24)
else:
    dias = 0

horas = hrs_dias - (dias *24)
minutos = int(min_seg)
segundos = round((min_seg - minutos) * 60)

print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos')