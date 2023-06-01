import http.server
import socketserver

puerto=5000
handler= http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",puerto),handler) as servidor:
    print (f"servidor en ejecucion en el pueto {puerto}")
    servidor.serve_forever
"""
Identifique qué paquetes se descargan automáticamente. Investigue la utilidad que tienen estos
paquetes.
asgiref==3.7.2: Este paquete proporciona una implementación de referencia de la especificación ASGI (Asynchronous Server Gateway Interface) para la comunicación entre servidores web y aplicaciones web en Django. ASGI es una interfaz que permite la comunicación asincrónica entre servidores web y aplicaciones, lo que es útil para aplicaciones en tiempo real y que requieren un alto rendimiento.

Django==4.2.1: Django es un framework de desarrollo web de alto nivel y de código abierto en Python. Es utilizado para crear aplicaciones web robustas y escalables de manera rápida y eficiente. La versión 4.2.1 es una versión específica del framework Django. Proporciona una amplia gama de características y herramientas que facilitan el desarrollo web, incluyendo el manejo de la base de datos, la generación de formularios, la administración de usuarios y la gestión de URL.

sqlparse==0.4.4: Este paquete es una biblioteca de análisis de SQL en Python. Proporciona una interfaz para analizar consultas SQL y formatearlas de manera legible. Puede ser útil en el contexto de Django para analizar y manipular consultas SQL generadas por el ORM (Object-Relational Mapping) de Django.

tzdata==2023.3: Este paquete es una base de datos de zona horaria utilizada por Django y otros sistemas para manejar la conversión de fechas y horas en diferentes zonas horarias. Contiene información sobre los desplazamientos horarios, las reglas de horario de verano y otra información relacionada con las zonas horarias de todo el mundo. La versión 2023.3 es una versión específica de la base de datos de zona horaria utilizada por Django en ese momento.

"""

"""
¿Qué facilidades nos proporciona Django?

Rápido.
Django fue diseñado para ayudar a los desarrolladores a llevar aplicaciones desde el concepto hasta la finalización lo más rápido posible.

Seguro.
Django se toma en serio la seguridad y ayuda a los desarrolladores a evitar muchos errores comunes de seguridad.

Escalable.
Algunos de los sitios más transitados en la web aprovechan la capacidad de Django para escalar rápidamente y de forma flexible.
"""

"""
¿Qué desventajas nos trae este tipo de proyectos sin Django?
es posible desarrollar proyectos web sin utilizar frameworks como Django, hacerlo conlleva más complejidad, riesgos de seguridad y una mayor carga de trabajo. 
os frameworks web están diseñados para agilizar el desarrollo, mejorar la seguridad y facilitar la escalabilidad, por lo que su uso suele ser recomendado en la mayoría de los proyectos web.


"""

"""
utilidad de django-admin
startproject
 es un comando proporcionado por Django que se utiliza para crear un nuevo proyecto de Django. Al ejecutar este comando en la línea de comandos, se genera una estructura de directorios y archivos básicos que conforman un proyecto de Django

"""