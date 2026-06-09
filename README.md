# Matias_Morales_POO3
Inspirado en el juego gta aplicado con nuevas funciones y estrucutura


Con este proyecto haremos una "Remasterizacion" del juego de GTA aplicando los nuevos conceptos como:Herencia,Polimorfismo,Encapsulamiento y Abstraccion las cuales nos permitiran desarrollar de manera mas "Limpia y Correcta" Este proyecto 

Primeramente haremos comprobaciones o instrucciones requeridas para esta prueba empezando por:

CLASES
El primer requerimiento a seguir de esta evaluacion es contar con 5 clases minimas de desarrollo de proyecto .
El juego ya desarrollado anteriormente cuenta con un total de 8 CLASES ya integradas y definidas las cuales son:

1.CAMARA:
Es la camara que sigue al personaje principal. El mapa de la ciudad es de Gran tamaño por lo que no se puede aplciar una camara fija sobre el mapa del juego por lo que es necesario aplicar uan camara que siga al personaje en Tercera persona mientras este recorre el mapa.

2.World/Mundo:
Es la estructura o el detalle del juego el cual se encarga de diseñar como si fuera una ciudad añadiendo calles,ceras,edificios y todo lo que tiene una ciudad convencional.

3.El personaje Principal:
Es el usuario que controlamos ala hora de jugar y tiene distintas funciones como caminar,correr,disparar,interactuar,etc y en este juego el personaje cuenta con dinero ,armas,vehiculos los cuales puede usar o interactuar de manera libre durante el juego.

4.Vehiculos:
Son los principales simuladores de carros en este juego.No importa quien lo maneje o si el carro se ensucia ,etc su unico trabajo es saber comoa aceleran los autos,frenan dan vueltas ,basicamente lo basico que tiene que tener un auto sin enfocarse mucgho en los detalles

5.NPCs del videojuego:
Son los caracteres establecidos en el juego de manera aleatoria y su funciones principales ya tener en cuenta son el caminar,correr por disturbios,pasean sin tener un detalle especifico ya que por eso son " EXTRAS".

6.Balas o proyectiles
Son las clases que interactuan alo momento de usar armas ya sean pistolas,escopetas,misiles ,etc y su funcio principal son viajar en linea recta ,viajar en una direccion,hacer daño si golpea a alguien y se deshacen despues luego de ser disparadas para no afectar el rendimiento de la computadora .

7.Particulas
Estas se crean al haber explosiones de coches ,disparos o destruccion colateral creando un monton de chispas rojas dando esa sencacion de particulas o pirotecnia durante el juego.

8.Sistema de Misiones
Este sistema se desarrolla durante el juego y da indicaciones y pasos a seguir al personaje para completarlas a cambio de dinero ,estadisticas,prestigio,etc dentro del juego ,estas misiones pueden ser falladas y si no se cumplen dentro del tiempo establecido o no de manera correcta notificara al usuario indicando "Mision Fallida".

9.Juego Base o Motor
Esta clase se encarga de arrancar el juego preparar todo lo que incluye y es el "motor principal" para que el juego funcione de manera correcta,carga imagenes,musica,objetos,etc y se encarga de guardar nuestra partida y cargar escenarios y criaturas.

ATRIBUTOS Y METODOS

1.Aplicacion en clase:Personaje Principal
ATRIBUTOS: (health,money,ammo_in_mag) estan fijas en el personaje y van cambiandos egun lo que hagamos durante el juego,ya sea robar bancos para ganar dinero,disparar armas o equipar armas o que usenmos botiquines o nos disparen. 

METODOS:(Update,heal ,enter_exit_vehicle) se aplican mediante acciones de teclado ya sea al presionar W para avanzar y que el personaje actualize acciones o que presione F para acceder o salir de vehiculos durante la partida.

2.Aplicacion en clase:Vehiculos
ATRIBUTOS:(max speed,min speed,health_vehicle)son parametros de cada vehiculo indicandos estadisticas o datos sobre este y segun las acciones que hagamos cambiaran por ej:si chocamos demasiado un coche y lo debilitamos si la vida de este llega a 0 se detendra e empezara a incendiarse indicando de que se daño o dejo e funcionar.

METODOS:(Damage,draw)se aplican segun al interaccion con el entorno,cuando el metodo de una bala choca contra el armazon del vehiculo llama al metodo damage(amount) del vehiculo.Este metodo resta la vida del vehiculo y genera particulas de humo.

3.Aplicacion en clase:NPC
ATRIBUTOS:(Police,alive,vx,vy)Definen la identidad y el rumbo del personaje,si POLICE es verdader el personaje tiene permitido cargar un arma.

METODOS:(UPDATE),se aplica en bucle continuo,EN cada milisegundo,este metodo calcula la distancia matematica entre NPC y la del jugador,si estas cerca y tu nivel de busqueda es mayor a 0,elo metodo cambia los atributos de direccion(vx,vy) para que el eprsonaje en vez de deambular corra hacia ti

4.Apliccion en clase:MUNDO
ATributos:(Buildings,roads).Son listas que guardan rectangulos invisibles en la memoria con las coordenadas de cada parte de la ciudad.

METODOS:(Collide buildings).Se aplica como un filtro de seguridad,cada vez que el personaje o un vehiculo inentan dar una opaso hacia adelante,el juego le pregunta al metodo,¿El jugador va a pisar un edificio?,si el metodo dice que si bloquea el movimiento del jugador reinciando sus coordenadas para que rebote y no atraviese la pared.

5.Aplicacion en clase:Juego o motor
Atributos:(Wanted,vehicles,npcs)Es la base de datos viva en el juego,guarda cuantas estrellas tienes y mantiene el registro de cuantos vehiculos y npcs quedan vivos dentro del mapa.

Metodos:(save,load)se aplican junto con archivos en el PC,al presionar la tecla de guardado,el metodo save agarra una foto de todos tus atributos actuales como:(health,money,x y y ) y lo escirbe textualmente en el archivo savegame.json.El metodo LOAD hace lo contrario borran lo que estes haciendo,lee ese archivo y sobreescribe los atributos para regresar donde quedo guardado.


6.Aplicacion en clase:CAMARA
Atributos:(x,y,w,h)Son las dimensiones y coordenadas establecidas segun la posicion del jugador al cargar el juego.

METODOS:update(target):lee la posicion del jugador y recalcula la psoicion de sus atributos x e y para mantener al personaje en el centro de la pantalla mientras se mueve
to_screen(pos):Aplica resta matematica entre las coordenadas del mundo y la posicion de la camara para indicarle a pyGame exactamente en que pixel debe dibujar cada elemento.

7.Aplicacion clase:Balas o proyectiles

Atributos:(x,y):La ubicacion de cada chispa o rafaga de humo individual.
(vx,vy):dircciones y velocidades aleatorias para que las chispan salgan disparadas en cualquier direccion.
(alpha):el nivel de transparencia de la particula(255 o 0)
(color):indicasi es rojo,naranjo o plomo segun su proyectil y el humo.

Metodos:Update():mueve la particula por el espacio y reduce gradualmente al atributo.
(alpha.):cuando la opacidad llega a 0,el sistema cuenta como que la particula se deshizo y la borra

8.Aplicacion clase:Misiones
Atributos:(target_vehicle):el auto especifico marcado al jugador que tiene que robar obligadamente.
(dest.x,dest.y):coordenadas de zona de entrega para finalizar mision.
(reward):ya sea la recompensa que recibe el jugador añadida a sus atributos
(active):una bandera logica,true o flase que indica al motro del juego si hay una mision activ o en progreso

Metodos:update(dt):mide continuamente la distancia del atributo target_vehicle y las coordenadas del destino, si la distancia es minima,modifica el dinero del jugador y desactiva la mision y si el auto se destruye,cancela el encargo.

APARTADO DE ENCAPSULAMIENTO

Uso de encapsulamiento en codigo: se aplico encapsulamiento utilizando el estandar de Python(_atributos y @property).Esto garantiza la integridad de los datos :el estado la salud del personaje o de los autos no puede ser corrompido o modificado accidentalmente ya sean funciones externas de renderizado o fisicas,obligando a toda alteracon pasarn por metodos de validacion(recibir_daño(),modificar_dinero()).

