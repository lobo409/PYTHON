# Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.
parcial1 = int(input("Indique la nota del primer parcial:"))
parcial2 = int(input("Indique la nota del segundo parcial:"))
parcial3 = int(input("Indique la nota del tercer parcial:"))
final = int(input("Indique la nota del examen final:"))
trabajo = int(input("Indique la nota del trabajo final:"))
totalparcial = ((parcial1+parcial2+parcial3) /3 * 0.55)
totalfinal = (final * 0.30)
totaltrabajo = (trabajo * 0.15)
calificacionfinal = (totalparcial+totalfinal+totaltrabajo)
print("La calificacion final es:", calificacionfinal)