const express = require('express');
const app = express();
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');
require('dotenv').config()
const PORT = process.env.PORT
const HOST = process.env.HOST

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.get('/', (err, res)=>{
    res.write(`Please navigate to http://127.0.0.1:3001/api-docs/ for the documentation`)
})

app.listen(PORT, HOST, ()=>{
    console.log(`Swagger listening at ${HOST}:${PORT}`)
})
