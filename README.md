# RETO-VISUALIZACIÓN
## EXPLICACIÓN DE LOS PASOS SEGUIDOS

Primero, me he asegurado de tener Docker instalado en mi sistema. Luego, creo los contenedores de Elasticsearch y Kibana utilizando Docker. Configuro Elasticsearch para que esté accesible desde Kibana y aseguro que ambos contenedores estén en ejecución.

Después, he desarrollado un archivo Python para manejar el envío de datos a un índice en Elasticsearch. He usado la biblioteca elasticsearch-py para interactuar con el cluster de Elasticsearch desde Python.

Una vez que tengo los datos fluyendo hacia Elasticsearch, paso a Kibana para crear visualizaciones. Inicio sesión en la interfaz web de Kibana y configuro un índice pattern para que Kibana pueda reconocer los datos. Luego, creo visualizaciones personalizadas según los requisitos del proyecto, utilizando las herramientas de gráficos y tablas que ofrece Kibana.

Finalmente, reviso y ajusto las visualizaciones según sea necesario para asegurarme de que representen adecuadamente los datos. Esto implica jugar con los tipos de gráficos, filtros y agregaciones para obtener la presentación más clara y significativa de los datos en Kibana.

## INSTRUCCIONES DE USO
- docker-compose up -d: Este comando levanta los contenedores de Elasticsearch y Kibana en segundo plano. 
- python3 generar_datos.py: Una vez que los contenedores de Elasticsearch y Kibana estén en funcionamiento, ejecutó este comando para ejecutar el script de Python generar_datos.py. Este script se encarga de generar y enviar datos a Elasticsearch.

## POSIBLES VÍAS DE MEJORA
- Añadir seguridad: Implementar autenticación y autorización en Elasticsearch y Kibana para garantizar que solo usuarios autorizados puedan acceder y manipular los datos.
Configura certificados SSL/TLS para cifrar las comunicaciones entre los clientes y los servicios de Elasticsearch y Kibana, asegurando así la privacidad y la integridad de los datos en tránsito.
- Controlar mejor las funcionalidades de Kibana: Explorar y utiliza plugins y complementos de Kibana para extender sus capacidades y personalizar su funcionalidad.
Trabajar con datos más reales: Considerar la posibilidad de integrar fuentes de datos más diversas y complejas, como datos en tiempo real provenientes de sensores IoT, registros de servidores, feeds de redes sociales, etc.

## RETOS ENCONTRADOS
- Juntar Elasticsearch con Kibana(quitar seguridad)
- Entender el funcionamiento de Kibana: En un principio, no entendía como podía visualizar los datos ya qué me aparecía que era obligatoria alguna funcionalidad que no me intersaba como la medía, la máxima, el ultimo valor... Me costó darme cuenta que era para los valores que no entraban en las gráficas.

## ALTERNATIVAS POSIBLES
Grafana junto con Prometheus ofrece una solución poderosa y ampliamente utilizada para la visualización y monitoreo de datos. Grafana es conocida por su facilidad de uso, amplia compatibilidad con diversas fuentes de datos, flexibilidad y personalización, así como una comunidad activa que proporciona soporte y recursos de aprendizaje. Junto con Prometheus, que es una herramienta de monitoreo de código abierto popular, Grafana ofrece escalabilidad y capacidad para manejar grandes volúmenes de datos, siendo una opción sólida para aplicaciones empresariales y entornos distribuidos.


