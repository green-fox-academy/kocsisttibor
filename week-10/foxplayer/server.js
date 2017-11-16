'use strict'

const port = 8080;
const express = require('express');
const app = express();
const cors = require('cors');
const mysql = require('mysql');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'alma',
    database: 'foxplayer'
})

connection.connect( err => {
    if (err) {
        console.log('Error connecting to db' + err);
        return;
    } else {
        console.log('DB connection estabilished');
    }
});

app.use(express.json());
app.use(cors());
app.use('/scripts', express.static('./scripts'));
app.use('/style', express.static('./style'));
app.use('/music', express.static('./music'));

let mockPlaylist = [
    {playlist_id: 0, playlist_name: "Favourites"},
    {playlist_id: 1, playlist_name: "Best music"}, 
    {playlist_id: 2, playlist_name: "Ambient"}]
let id = 3

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/playlist', (req, res) => {
    connection.query('SELECT * FROM playlists', (err, result) => {
        if (err) {
            console.error(err);
        } else {
            res.json(JSON.stringify(result))
        }
    })
})

const insertPlaylist = (playlist, callback) => {
    connection.query('INSERT INTO playlists SET ?', playlist, (err, result) => {
        if (err) {
            console.error(err);
            return;
        } else {
            console.error(result);
            callback(result.insertId)
        }
    })
}

const getAddedPlaylistName = (result_id, callback) => {
    connection.query('SELECT * FROM playlists WHERE playlist_id=' + connection.escape(result_id), (err, result) => {
        if (err) {
            console.error(err);
            return;
        } else {
            console.error('result of getAddedPlaylistName: ' + result);
            callback(result)
        }
    })
}

app.post('/addplaylist', (req, res) => {
    let newPlaylist = req.body;
    insertPlaylist(newPlaylist, (result_id) => {
        getAddedPlaylistName(result_id, (result) => {
            res.json(result);
        });
    });
});

app.post('/deleteplaylist', (req, res) => {
    mockPlaylist.splice(mockPlaylist.map(x => x.playlist_id).indexOf(1*req.body.playlist_to_delete), 1);
    res.json(mockPlaylist);
})

app.listen(port, error => error ? console.log(error): console.log('Server running, at ' + port));