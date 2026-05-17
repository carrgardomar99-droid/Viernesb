// Servidor de fondo de YARBIS - Service Worker Activo v2.5
const NOMBRE_CACHE = 'yarbis-core-v2';
const ACTIVOS = [
    './',
    './index.html',
    './manifest.json'
];

// Instalación y almacenamiento de interfaz base
self.addEventListener('install', (evento) => {
    evento.waitUntil(
        caches.open(NOMBRE_CACHE).then((cache) => {
            return cache.addAll(ACTIVOS);
        })
    );
});

// Control de peticiones para asegurar velocidad
self.addEventListener('fetch', (evento) => {
    evento.respondWith(
        caches.match(evento.request).then((respuesta) => {
            return respuesta || fetch(evento.request);
        })
    );
});