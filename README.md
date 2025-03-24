# E3P1_README_PEQUIPO

Sistema Inteligente de Monitoreo para detección de Cubre bocas

Descripción:
Este proyecto consiste en el desarrollo e implementación de un sistema de monitoreo inteligente basado en reconocimiento facial, enfocado en la detección automática del uso de cubrebocas en entornos de alta seguridad, como hospitales, laboratorios y empresas del sector alimentario. El objetivo principal es fortalecer las medidas de bioseguridad, reduciendo el riesgo de contagio de enfermedades respiratorias y asegurando el cumplimiento de normativas sanitarias establecidas.

El sistema utiliza técnicas de visión por computadora y algoritmos de inteligencia artificial para identificar si las personas que ingresan o transitan por las instalaciones llevan cubrebocas de manera correcta. Además, puede integrarse con sistemas de control de acceso para restringir la entrada a quienes no cumplan con esta medida, y generar reportes en tiempo real para la administración y gestión eficiente de la seguridad sanitaria.

El sistema empleará tecnologías como OpenCV y TensorFlow para el procesamiento de imágenes, para mejorar la precisión en la detección de mascarillas. Además, se integrará con cámaras de seguridad y un panel de administración para monitoreo en tiempo real.


 👥 Integrantes del Proyecto

| Nombre                          | Rol                           |
|---------------------------------|------------------------------|
| Maria del Carmen Jaime Gallardo | Desarrolladora Backend       |
| Rufino Botello Santos           | Desarrollador Frontend       |
| Lenin Jared Pantoja Guerrero    | Ingeniero de IA             |
| Sonia Itzel Vázquez Bautista    | Administradora de Proyecto  |
| José Manuel Macías García       | Especialista en Seguridad   |



Objetivo:
---

Desarrollar un sistema inteligente capaz de detectar en tiempo real el uso de mascarillas y generar alertas automáticas para mejorar la seguridad sanitaria. Se busca alcanzar una tasa de detección superior al 95% y reducir los incidentes de no uso de mascarilla en un 50% dentro de las áreas monitoreadas.


 
#### Alcance del Proyecto:

•	Implementación de un sistema de visión por computadora para detectar mascarillas.

•	Integración con cámaras de seguridad en los accesos y áreas clave.

•	Generación de reportes y alertas automáticas para el personal de seguridad.

•	Desarrollo de una interfaz de administración para la gestión de eventos y estadísticas.

•	Análisis de patrones en el uso de mascarillas para mejorar estrategias de seguridad.


### Requerimientos Funcionales
1.	El sistema permite la captura de imágenes en tiempo real mediante cámaras de seguridad en los accesos y áreas clave del hospital.
2.	Procesamiento de imágenes usando diferentes técnicas para identificar si una persona lleva puesta una mascarilla.
3.	Generación de alertas en caso de detección de personas sin mascarilla.
4.	Registro de detecciones, almacenando imágenes, fecha, hora y ubicación del evento.
5.	Notificación visual y/o sonora en la entrada del hospital cuando se detecte una persona sin mascarilla.
6.	Envío de alertas al personal de seguridad mediante una aplicación o software de monitoreo.
7.	Integración con un panel de administración, donde los gerentes puedan visualizar reportes y estadísticas.
8.	Ajuste de sensibilidad del reconocimiento para reducir falsos positivos y negativos.
9.	Registro de eventos históricos, permitiendo revisar incidentes pasados.


####          Diagrama de Caso de Uso: 
[Monitoreo y Detección](dosc/monitoreo_y_deteccion.md)  


[Gestión y Administración](dosc/gestion_y_administracion.md)  


[Notificación y Respuesta](dosc/notificacion_y_respuesta.md)  
           

