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
    insertPostToDatabase(post, (result_id) => {         //callback function is used to have some proof that the data is inserted into database
        getAddedPostTitle(result_id, (result) => {      //proof is got by a new query in database, with the uniq id of the newly added record
            res.json(result);                           //result of the query about the newly added record is sent back to the frontend as response/feedback
        });
    });
});

const getScore = (post_id, callback) => {
    connection.query('SELECT score FROM posts WHERE post_id =' + connection.escape(post_id), (err, result) => {
        if (err) {
            console.error(err);
            return;
        } else {
            console.error('result of getScore: ' + parseInt(result[0].score));  // converts string into int  
            callback(parseInt(result[0].score));
        };
    });
};

const incrementScore = (post_id, originalScore, callback) => {
    let score = originalScore + 1;
    connection.query('UPDATE posts SET score =' + connection.escape(score) + ' WHERE post_id =' + connection.escape(post_id), (err, result) => {
        if (err) {
            console.error(err);
            return
        } else {
            console.error('result of incrementScore: ' + JSON.stringify(result));
            callback(score);
        }
    })
}

const decrementScore = (post_id, originalScore, callback) => {
    let score = originalScore - 1;
    connection.query('UPDATE posts SET score =' + connection.escape(score) + ' WHERE post_id =' + connection.escape(post_id), (err, result) => {
        if (err) {
            console.error(err);
            return
        } else {
            console.error('result of decrementScore: ' + JSON.stringify(result));
            callback(score);
        }
    })
}

app.put('/posts/:post_id/upvote', (req, res) => {
    let post_id = req.params.post_id.split('_')[1];         //post_id arrives in id_1 format
    getScore(post_id, result => {                           //with the result of the query is the callback function invocated; the callback function calls the incrementScore function
        incrementScore(post_id, result, newScore => {       //incrementScore also has callback <= to send back response to frontend only if the insertion of new data to database was successfull
            res.json({"score": newScore});
        });
    });
})

app.put('/posts/:post_id/downvote', (req, res) => {
    let post_id = req.params.post_id.split('_')[1];         //post_id arrives in id_1 format
    getScore(post_id, result => {                           //with the result of the query is the callback function invocated; the callback function calls the incrementScore function
        decrementScore(post_id, result, newScore => {       //incrementScore also has callback <= to send back response to frontend only if the insertion of new data to database was successfull
            res.json({"score": newScore});
        });
    });
})

app.listen(port, error => error ? console.log(error): console.log('Server running, at ' + port));