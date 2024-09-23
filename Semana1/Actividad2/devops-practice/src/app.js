const express = require('express');
const client = require('prom-client');

const app = express();
const register = new client.Registry();

// Middleware para medir la duración de las solicitudes
const httpRequestDurationMicroseconds = new client.Histogram({
    name: 'http_request_duration_seconds',
    help: 'Duration of HTTP requests in seconds',
    labelNames: ['method', 'route'],
    registers: [register],
});

// Middleware para registrar la duración de cada solicitud
app.use((req, res, next) => {
    const end = httpRequestDurationMicroseconds.startTimer();
    res.on('finish', () => {
        end({ method: req.method, route: req.route ? req.route.path : req.path });
    });
    next();
});

// Endpoint de métricas
app.get('/metrics', async (req, res) => {
    res.set('Content-Type', register.contentType);
    res.end(await register.metrics());
});

// Rutas de tu aplicación
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/delay', (req, res) => {
    setTimeout(() => {
        res.send('This was delayed by 2 seconds');
    }, 2000);
});

module.exports = app;

if (require.main === module) {
    const port = process.env.PORT || 3000; 
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}
