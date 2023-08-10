// server.js
require('dotenv').config({ path: './.env' });
const express = require('express');
const app = express();

const PORT = process.env.PORT || 4242;
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const { resolve } = require('path')
const bodyParser = require('body-parser')

app.use(express.static(process.env.STATIC_DIR));
app.use(bodyParser.json());

app.get('/', (request, response) => {
    const path = resolve(process.env.STATIC_DIR + 'index.html');
    response.sendFile(path);
});

app.get('/public-keys', (request, response) => {
    response.send({ key: process.env.STRIPE_PUBLISHABLE_KEY });
});

app.post('/my-route', (request, response) => {
    console.log(request.body);
    // put data in db
    // make api call
    response.send(request.body);
})



app.listen(PORT, () => { console.log(`Server running on http://localhost:${PORT}`) });