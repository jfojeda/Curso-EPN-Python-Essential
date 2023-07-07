n1=input("Cual es tu nombre? ")
a1=input("Cual es tu apellido? ")
edad=float(input("Ingresa tu edad "))
ubi=input("Ingresa tu ciudad ")
spc=""
etr=""

if edad>0 and edad<12:
    etr='Infante'
elif edad>=12 and edad <18:
    etr='Adolescente'
elif edad >=18 and edad <30:
    etr='Adulto Joven'
elif edad >=30 and edad <60:
    etr='Adulto'
else: 
    etr='Adulto Mayor'
   

print('Bienvenido',n1,a1,
      'registro que tu residencia es en la ciudad de',ubi,
      'hemos validado tu edad de',edad,'años',
      'y tu rango de edad es',etr)
