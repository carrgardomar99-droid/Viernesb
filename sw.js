// Servidor de fondo de YARBIS - Service Worker Activo
const NOMBRE_CACHE = 'yarbis-core-v3';
const ACTIVOS = [
    './',
    './index.html',
    './manifest.json'
];

self.addEventListener('install', (evento) => {
    evento.waitUntil(
        caches.open(NOMBRE_CACHE).then((cache) => {
            return cache.addAll(ACTIVOS);
        })
    );
});

self.addEventListener('fetch', (evento) => {
    evento.respondWith(
        caches.match(evento.request).then((respuesta) => {
            return respuesta || fetch(evento.request);
        })
    );
