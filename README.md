# Productivo Landings 🚀

Proyecto de Landing Pages optimizadas para conversión. Incluye los sitios de **Liga La Paz** y **Kliently Chat**.

## 🛠️ Tecnologías
- **Vite**: Motor de desarrollo y empaquetado.
- **Tailwind CSS**: Estilizado mediante CDN (Próximamente PostCSS).
- **Chart.js**: Visualización de datos interactivos.
- **Docker**: Despliegue en contenedores.

## 🚀 Desarrollo Local

1. Instalar dependencias:
   ```bash
   npm install
   ```
2. Iniciar servidor de desarrollo:
   ```bash
   npm run dev
   ```
3. Abrir en el navegador: `http://localhost:5173`

## 📦 Despliegue en Coolify

Este proyecto está listo para ser desplegado en Coolify mediante el `Dockerfile` incluido.

1. Conecta este repositorio en tu panel de Coolify.
2. Asegúrate de configurar el tipo de despliegue como **Docker**.
3. El build generará la carpeta `dist/` y será servida automáticamente por **Nginx**.

## 📂 Estructura
- `/index.html`: Landing Principal de Kliently Chat.
- `/liga-la-paz.html`: Landing de Liga La Paz (Opcional).
- `/images/`: Activos visuales.
- `/nginx.conf`: Configuración del servidor de producción.
- `/Dockerfile`: Instrucciones de empaquetado.

---
Originalmente diseñado y desarrollado por **Wilfredo Abad**.
