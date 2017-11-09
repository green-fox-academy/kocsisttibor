let mysql = require('mysql');
let connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma',
  database: 'bookstore'
});

connection.connect();

connection.query('SELECT book_name FROM book_mast;', function(err, rows) {
    rows.forEach(function(x) {
        console.log(x.book_name);
    });
});