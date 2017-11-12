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

app.use(express.json());
app.use(cors());

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

const insertPostToDatabase = (post, callback) => {
    post.timestamp = Date.now();
    connection.query('INSERT INTO posts SET ?', post, (err, result) => {
        if (err) {
            console.error(err);
            return 
        } else {
            console.error(result);
            callback(result.insertId)
        }
    })
}

const getAddedPostTitle = (result_id, callback) => {
    connection.query('SELECT * FROM posts WHERE post_id =' + connection.escape(result_id),  (err, result) => {
        if (err) {
            console.error(err);
            return;
        } else {
            console.error('result of getAddedPostTitle' + result);
            callback(result);
        }
    });
}

app.post('/posts', (req, res) => {
    let post = req.body;
    insertPostToDatabase(post, (result_id) => {         //callback function is used to have some proof that the data is inserter into database
        getAddedPostTitle(result_id, (result) => {      //proof is got by a new query in database, with the uniq id of the newly added record
            res.json(result);                           //result of the query about the newly added record is sent back to the frontend as response/feedback
        });
    });
});

const getScore = (post_id) => {
    connection.query('SELECT score FROM posts WHERE post_id =' + connection.escape(post_id), (err, result) => {
        if (err) {
            console.error(err);
            return;
        } else {
            console.error('result of getScore: ' + result);  //query doesn't results any data while in mysql shell this select works
            // callback(post_id, result);
        };
    });
};

// const incrementScore = (post_id, orignalScore) => {
//     let score = originalScore + 1;
//     connection.query('UPDATE posts SET score =' + connection.escape(score) + 'WHERE post_id =' + connection.escape(post_id), (err, result) => {
//         if (err) {
//             console.error(err);
//             return
//         } else {
//             console.error('result of incrementScore: ' + result);
//         }
//     })

// }

app.put('/posts/:post_id/upvote', (req, res) => {
    // getScore(req.params.post_id, (post_id, originalScore) => {
    //     incrementScore(post_id, originalScore)
    // });
    getScore(req.params.post_id);
})

app.listen(port, error => error ? console.log(error): console.log('Server running, at ' + port));