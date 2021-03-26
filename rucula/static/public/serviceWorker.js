const version = "rucula-v1"
const assets = [
    "/static/app.js",
    "/static/rucula.svg",
]

self.addEventListener("install", installEvent => {
    installEvent.waitUntil(
        caches.open(version).then(cache => {
            cache.addAll(assets)
        })
    )
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(
        caches.match(fetchEvent.request).then(res => {
            return res || fetch(fetchEvent.request)
        })
    )
})
