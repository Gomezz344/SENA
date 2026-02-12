# 5.Salario con horas extra: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.

horas = int(input("Digite cuantas horas trabajo esta semana: "))
vhora = 60000

if horas > 40 : 
    horas_extra = horas - 40
    salario = (40 * vhora) + (horas_extra * vhora * 1.5)
    print("Su salario semanal es:", salario)
else:
    salario = horas * vhora
    print("Su salario semanal es:", salario)