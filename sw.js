// Service Worker básico para permitir la instalación de la PWA
self.addEventListener('install', (event) => {
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
    // Permite que la app cargue de manera normal mediante internet
    event.respondWith(fetch(event.request));
});
