# Simple static site - no build needed
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
COPY kliently.html /usr/share/nginx/html/
COPY images/ /usr/share/nginx/html/images/
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
