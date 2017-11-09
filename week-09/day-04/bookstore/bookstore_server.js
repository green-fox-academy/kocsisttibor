'use strict';

let mysql = require('mysql');
let connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma',
  database: 'bookstore'
});

connection.connect(function(err) {
    if (err) {
        console.log('Error connecting to DB');
        return;
    }
    console.log('Connection estabilished')
});

let express = require('express');
let app = express();
let port = 8080;

app.use('/assets', express.static('./assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/titles', function(req, res) {
    connection.query('SELECT book_name FROM book_mast;', function(err, rows) {
        let html = '<h2>Titles</h2><ul>';
        for (let i = 0; i < rows.length; i += 1) {
            html += '<li>' + rows[i].book_name + '</li>'
        }
        html += '</ul>'
        res.send(html);
    });
});

app.listen(port);