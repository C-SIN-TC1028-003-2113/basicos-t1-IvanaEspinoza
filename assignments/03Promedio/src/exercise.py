def main():
    #escribe tu código abajo de esta línea
    calf1 = float(input('Calificación de la materia: '))
    calf2 = float(input('Calificación de la materia: '))
    calf3 = float(input('Calificación de la materia: '))
    calf4 = float(input('Calificación de la materia: '))

    promedio = (calf1+calf2+calf3+calf4)/4

    print('El promedio es: '+str(promedio))


if __name__ == '__main__':
    main()
