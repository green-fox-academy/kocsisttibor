'use strict'

const express = require('express');
const app = express();
const cors = require('cors');
const port = 8080;

app.use(express.json());
app.use(cors());
app.use('/scripts', express.static('./scripts'));
app.use('/style', express.static('./style'));

let mockPlaylist = [
    {playlist_id: 0, playlist_name: "Favourites"},
    {playlist_id: 1, playlist_name: "Best music"}, 
    {playlist_id: 2, playlist_name: "Ambient"}]
let id = 3

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/playlist', (req, res) => {
    res.send(mockPlaylist)
})

app.post('/addplaylist', (req, res) => {
    mockPlaylist.push({playlist_id: id, playlist_name:req.body.playlist_name});
    id += 1;
    res.json(mockPlaylist)
})

app.post('/deleteplaylist', (req, res) => {
    mockPlaylist.splice(mockPlaylist.map(x => x.playlist_id).indexOf(1*req.body.playlist_to_delete), 1);
    res.json(mockPlaylist);
})

app.listen(port, error => error ? console.log(error): console.log('Server running, at ' + port));