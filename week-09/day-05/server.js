'use strict'

const express = require('express');
const app = express();
const port = 8080;

app.get('/hello', (req, res) => 
    res.send('hello world')
);


app.listen(port, error => error ? console.log(error): console.log('Server running, at ' + port));