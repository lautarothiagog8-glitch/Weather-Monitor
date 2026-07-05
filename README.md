#  Weather Monitor

## Descripción

Weather Monitor es un proyecto desarrollado en Python que consulta el clima en tiempo real utilizando la API de Open-Meteo y envía un reporte automáticamente a un canal de Discord mediante un Webhook.

El programa solicita una ciudad al usuario, obtiene sus coordenadas geográficas, consulta el estado actual del clima y genera una recomendación según las condiciones meteorológicas.

---

## Funcionalidades

* Consulta el clima de cualquier ciudad.
* Obtiene automáticamente la latitud y longitud mediante una API de geocodificación.
* Consulta la temperatura y el estado del tiempo en tiempo real.
* Interpreta los códigos meteorológicos de Open-Meteo.
* Genera una recomendación según el clima.
* Envía un reporte formateado a Discord mediante un Webhook.
* Utiliza variables de entorno (`.env`) para proteger información sensible como la URL del Webhook.

---

## Tecnologías utilizadas

* Python
* Requests
* Open-Meteo API
* Discord Webhooks
* python-dotenv

---

## Estructura general del proyecto

1. El usuario ingresa una ciudad.
2. Se obtienen las coordenadas de esa ciudad.
3. Se consulta el clima actual.
4. Se interpreta el estado meteorológico.
5. Se genera un reporte.
6. El reporte se envía automáticamente a Discord.

---

## Objetivo del proyecto

Este proyecto fue realizado como práctica para aprender a:

* Consumir APIs REST.
* Realizar solicitudes GET y POST.
* Trabajar con respuestas JSON.
* Integrar servicios externos mediante Webhooks.
* Proteger credenciales utilizando variables de entorno.
* Desarrollar una automatización sencilla pero funcional en Python.

---

## Próximas mejoras

* Agregar un manejo de errores más completo utilizando `try` y `except`.
* Mejorar el formato de los reportes enviados a Discord.
* Permitir consultas de múltiples ciudades.
* Agregar más información meteorológica, como humedad, velocidad del viento y pronóstico.
