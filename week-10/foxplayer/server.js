'use strict'

const express = require('express');
const app = express();
const cors = require('cors');
const port = 8080;

app.use(express.json());
app.use(cors());

app.get('/playlist', (req, res) => {
    res.send([{playlist_id: 1, playlist_name: "Best music"}, {playlist_id: 2, playlist_name: "Ambient"}])
})

app.listen(port, error => error ? console.log(error): console.log('Server running, at ' + port));