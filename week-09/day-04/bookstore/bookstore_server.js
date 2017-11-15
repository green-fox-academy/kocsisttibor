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

app.get('/books', function(req, res) {
    let filters = {
        category: req.query.category,
        publisher: req.query.publisher,
        plt: req.query.plt,
        pgt: req.query.pgt
    }   
    let basic_query = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price \
                       FROM book_mast \
                       JOIN author ON author.aut_id=book_mast.aut_id \
                       JOIN category ON book_mast.cate_id=category.cate_id \
                       JOIN newpublisher ON book_mast.pub_id=newpublisher.pub_id' 

    if (filters.category !== undefined) {
        basic_query += ' WHERE cate_descrip="' + filters.category + '"';
    }
    if (filters.publisher !== undefined) {
        basic_query += ' AND pub_name="' + filters.publisher + '"';
    }

    if (filters.plt !== undefined) {
        basic_query += ' AND book_price<"' + filters.plt + '"';
    }

    if (filters.pgt !== undefined) {
        basic_query += ' AND book_price>"' + filters.pgt + '"';
    }

    basic_query += ';'
    connection.query(basic_query, function(err, rows) {
        let html = '<table><thead>'
        Object.keys(rows[0]).forEach(function(x) {
            html += '<th>' + x + '</th>';
        })
        html += '</thead><tbody>';
        rows.forEach(function(x) {
            html += '<tr>' + 
                    '<td>' + x.book_name + '</td>' +
                    '<td>' + x.aut_name + '</td>' + 
                    '<td>' + x.cate_descrip + '</td>' +
                    '<td>' + x.pub_name + '</td>' +
                    '<td>' + x.book_price + '</td>' +
                    '</tr>';
        })
        html += '</tbody></table>';
        res.send(html);
    })
})

app.listen(port);