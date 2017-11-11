'use strict'

const express = require('express');
const app = express();
const port = 8080;

const cors = require('cors');

const mysql = require('mysql');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'alma',
    database: 'reddit'
});

app.use(cors());

app.get('/hello', (req, res) => 
    res.send('hello world')
);

app.get('/posts', (req, res) =>
    connection.query('SELECT * FROM posts', (err, rows) => {
        if (err) {
            res.send('Error occured during database query.')
        } else {
            let posts = [];
            rows.forEach( row => {
                let post = {
                    'id': row.post_id,
                    'title': row.title,
                    'url': row.url,
                    'timestamp': row.timestamp,
                    'score': row.score,
                    'owner': row.owner
                };
                posts.push(post);
            })
            res.json({'posts': posts})
        }
    })
)

app.listen(port, error => error ? console.log(error): console.log('Server running, at ' + port));