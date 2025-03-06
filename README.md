# E3P1_README_PEQUIPO

Sistema Inteligente de Monitoreo en Hospitales

Descripción:
Este proyecto consiste en el desarrollo e implementación de un sistema de monitoreo en hospitales basado en visión por computadora e inteligencia artificial para detectar el uso de mascarillas en tiempo real. Su objetivo es fortalecer las medidas de bioseguridad, reducir riesgos de contagio y facilitar la gestión de acceso y cumplimiento de normativas sanitarias.

El sistema empleará tecnologías como OpenCV y TensorFlow para el procesamiento de imágenes, así como algoritmos de aprendizaje profundo para mejorar la precisión en la detección de mascarillas. Además, se integrará con cámaras de seguridad hospitalarias y un panel de administración para monitoreo en tiempo real.


 👥 Integrantes del Proyecto

| Nombre                          | Rol                           |
|---------------------------------|------------------------------|
| Maria del Carmen Jaime Gallardo | Desarrolladora Backend       |
| Rufino Botello Santos           | Desarrollador Frontend       |
| Lenin Jared Pantoja Guerrero    | Ingeniero de IA             |
| Sonia Itzel Vázquez Bautista    | Administradora de Proyecto  |
| José Manuel Macías García       | Especialista en Seguridad   |



Objetivo
Desarrollar un sistema inteligente capaz de detectar en tiempo real el uso de mascarillas en hospitales y generar alertas automáticas para mejorar la seguridad sanitaria. Se busca alcanzar una tasa de detección superior al 95% y reducir los incidentes de no uso de mascarilla en un 50% dentro de las áreas monitoreadas.


 
Alcance del Proyecto:

•	Implementación de un sistema de visión por computadora para detectar mascarillas.

•	Integración con cámaras de seguridad en los accesos y áreas clave del hospital.

•	Generación de reportes y alertas automáticas para el personal de seguridad.

•	Desarrollo de una interfaz de administración para la gestión de eventos y estadísticas.

•	Análisis de patrones en el uso de mascarillas para mejorar estrategias de seguridad.


Requerimientos Funcionales
1.	Captura de imágenes en tiempo real mediante cámaras de seguridad en los accesos y áreas clave del hospital.
2.	Procesamiento de imágenes usando diferentes técnicas para identificar si una persona lleva puesta una mascarilla.
3.	Generación de alertas en caso de detección de personas sin mascarilla.
4.	Registro de detecciones, almacenando imágenes, fecha, hora y ubicación del evento.
5.	Notificación visual y/o sonora en la entrada del hospital cuando se detecte una persona sin mascarilla.
6.	Envío de alertas al personal de seguridad mediante una aplicación o software de monitoreo.
7.	Integración con un panel de administración, donde los gerentes puedan visualizar reportes y estadísticas.
8.	Ajuste de sensibilidad del reconocimiento para reducir falsos positivos y negativos.
9.	Registro de eventos históricos, permitiendo revisar incidentes pasados.




Requerimientos No Funcionales
1.	Protección de datos personales, garantizando que las imágenes capturadas se almacenen y procesen de manera segura.
2.	Acceso restringido al sistema, con autenticación para administradores y personal autorizado.
3.	Registro y monitoreo del sistema para identificar posibles fallos o mejoras.
4.	Interfaz intuitiva y fácil de usar para que el personal pueda operar el sistema sin necesidad de capacitación avanzada.
5.	Disponibilidad de API para integrarse con otros sistemas de gestión de seguridad.




Metodología de Desarrollo
Se empleará la metodología ágil Scrum, estructurada en los siguientes procesos:

1. Planificación del Producto

Definición del Product Backlog con todas las funcionalidades necesarias.

Priorización de tareas según valor para el usuario y viabilidad técnica.

Asignación de roles y responsabilidades dentro del equipo.

2. Sprints e Iteraciones

Desarrollo en ciclos cortos de 2 a 4 semanas.

Reuniones diarias para revisar avances y resolver impedimentos.

Entregas incrementales para validar funcionalidades clave.

3. Seguimiento y Control

Uso de GitHub Projects como tablero Kanban.

Pruebas constantes para asegurar calidad y estabilidad del sistema.

Documentación continua del código y decisiones técnicas.

4. Revisión y Mejora

Revisión del producto con los interesados al final de cada sprint.

Identificación de mejoras y ajustes en la planificación.

Implementación de retroalimentación para optimizar el producto.

 ####  Tecnologías Utilizadas
Para el desarrollo del Sistema Inteligente de Monitoreo en Hospitales, se utilizarán las siguientes tecnologías:
#### Visión por Computadora e Inteligencia Artificial
•	OpenCV: Para el procesamiento de imágenes en tiempo real y detección de rostros.
•	TensorFlow/Keras: Implementación de modelos de deep learning para la clasificación de imágenes y detección de mascarillas.
•	YOLO (You Only Look Once) o MobileNetV2: Modelos optimizados para detección rápida y eficiente de mascarillas en entornos hospitalarios.
•	Python: Lenguaje principal para el desarrollo de scripts de IA y procesamiento de imágenes.
#### Backend
•	Flask o FastAPI: Framework para desarrollar la API que gestionará la comunicación entre el sistema de detección y la interfaz de usuario.
•	PostgreSQL o MongoDB: Base de datos para almacenar registros de detecciones, imágenes y eventos.
•	Redis: Para el manejo de eventos en tiempo real y caché de datos.
#### Frontend
•	React.js: Para el desarrollo de una interfaz de administración moderna y responsiva.
•	Material-UI o TailwindCSS: Librerías para mejorar la experiencia de usuario con componentes estilizados.
#### Notificaciones y Alertas
•	Twilio o Firebase Cloud Messaging (FCM): Para el envío de notificaciones al personal de seguridad.
•	WebSockets (Socket.io o FastAPI WebSockets): Comunicación en tiempo real entre el sistema de detección y la interfaz de administración.
#### Infraestructura y Despliegue
## Servidores y Computación en la Nube
•	Google Cloud Platform (GCP), AWS o Azure: Para el despliegue del sistema y procesamiento de datos en la nube.
•	Docker y Kubernetes: Para la orquestación y despliegue de contenedores en un entorno escalable.
•	NVIDIA GPU Cloud (NGC) o servidores con GPUs: Para acelerar el entrenamiento y la inferencia de modelos de IA.
## Seguridad y Protección de Datos
•	Cifrado de datos (AES-256, TLS/SSL): Para proteger la información de detecciones y accesos.
•	Autenticación JWT (JSON Web Tokens): Para el control de acceso al sistema.
•	Reglamentos de privacidad (GDPR, HIPAA): Cumplimiento con normativas de protección de datos hospitalarios.
## Monitoreo y Mantenimiento
•	Prometheus y Grafana: Para el monitoreo del sistema en tiempo real.
•	Logging con ELK Stack (Elasticsearch, Logstash, Kibana): Para el análisis de registros y diagnóstico de errores.
•	CI/CD con GitHub Actions o Jenkins: Automatización de pruebas y despliegues.


---

####          Diagrama de Caso de Uso: 
[Monitoreo y Detección](dosc/monitoreo_y_deteccion.md)  


[Gestión y Administración](dosc/gestion_y_administracion.md)  


[Notificación y Respuesta](dosc/notificacion_y_respuesta.md)  

