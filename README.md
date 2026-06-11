# Mini GTA Simulator - Proyecto POO 4°e

## 5.1 Nombre del Proyecto
Integrante: Matías Morales  
Curso: 4° Medio E  
Asignatura: Programación Orientada a Objetos  
Profesor: Brandon Baxter  
Fecha: Junio 2026  

---

## 5.2 Descripción del Sistema
Este proyecto es un simulador básico por consola inspirado en el juego GTA. Lo armé para simular cómo funciona una ciudad por dentro, separando a la gente común (civiles) de las fuerzas de la ley (policías). El programa permite guardar los personajes en una lista y jugar a hacer misiones arriesgadas donde puedes ganar dinero para tu billetera o perderlo si te atrapa la policía.

Está pensado para ser un sistema rápido, liviano y fácil de usar directamente desde la pantalla de comandos.

---

## 5.3 Conceptos de POO Utilizados (Explicación Breve y Ubicación)

* Abstracción: Se aplicó en la clase base "Personaje" mediante el uso de la librería "ABC". Define la plantilla obligatoria para que todos los personajes del juego compartan los atributos de nombre, ciudad y el método "realizar_accion()".
* Herencia: Se aplicó en las clases "Civil" y "Policia". Ambas actúan como clases hijas que extienden a "Personaje", lo que permite reutilizar de manera directa el constructor y los atributos de nombre y ciudad sin duplicar código.
* Encapsulamiento: Se aplicó en la variable "_vida" dentro de la clase "Personaje". Al anteponer un guion bajo, el acceso directo queda restringido desde el exterior, obligando al sistema a consultar el dato únicamente a través del método público "@property vida".
* Polimorfismo: Se aplicó en el método ".realizar_accion()" dentro de las clases "Civil" y "Policia". Aunque el método se llama exactamente igual en ambas estructuras, el civil devuelve una cadena relacionada con su trabajo y el policía devuelve una alerta de patrullaje.

---

## Guía de Funcionamiento (Paso a paso)

Al arrancar el archivo main.py, se abre un menú con 4 opciones numéricas:

1. Opción 1 (Registrar): Te pregunta si quieres crear un Civil o un Policía. Escribes su nombre, su ciudad y su rol (trabajo o rango). El sistema lo fabrica y lo guarda.
2. Opción 2 (Mostrar): Te muestra en pantalla a todos los personajes que tiene guardados el juego en ese momento y te dice qué acción está haciendo cada uno gracias al polimorfismo.
3. Opción 3 (Misión): Te ofrece un trabajo criminal para ganar plata. Si aceptas con un "si", el juego calcula al azar si completaste el robo (ganas dinero) o si te atrapó la ley (pierdes dinero por la fianza).
4. Opción 4 (Salir): Corta el programa limpiamente con un mensaje de despedida.

---

## 5.4 Criterios de Aceptación
1. El menú no se puede cerrar solo; se repite todo el tiempo hasta que elijas la opción 4.
2. Si el usuario escribe una opción que no existe (como un número cualquiera o letras), el programa avisa del error y vuelve a mostrar el menú.
3. Cualquier personaje que registres en la opción 1 tiene que aparecer al tiro en la lista de la opción 2.
4. El dinero que ganes o pierdas en las misiones debe actualizarse al tiro en el saldo total.
5. El programa ya viene con dos personajes creados desde el principio (Niko y Tenpenny) para que el profe no vea las listas vacías la primera vez.
6. La vida (_vida) no se puede modificar directamente desde el menú para cumplir con el encapsulamiento.

---

## 5.5 Pruebas de Usuario
| Acción Realizada | Resultado Esperado | Resultado Obtenido | ¿Cumple? |
| :--- | :--- | :--- | :---: |
| Registrar un civil llamado "CJ" en la Opción 1 | El sistema confirma que se guardó con éxito. | Salió el mensaje de éxito en pantalla. | SÍ |
| Listar los personajes en la Opción 2 | Ver los personajes que venían por defecto y al nuevo "CJ". | Se listaron los 3 personajes con sus datos bien puestos. | SÍ |
| Hacer la misión en la Opción 3 escribiendo "si" | El juego decide si gano o pierdo y me cambia el dinero. | Misión procesada; sumó la recompensa a la billetera. | SÍ |
| Salir del juego con la Opción 4 | El programa se detiene de forma limpia. | Se mostró el mensaje de adiós y se cerró la consola. | SÍ |

---

## 5.6 Declaración de Apoyo de IA
Se utilizó inteligencia artificial únicamente como apoyo de redacción y de estructura. Mas materia extraida de guias y trabajos anteriores de POO.