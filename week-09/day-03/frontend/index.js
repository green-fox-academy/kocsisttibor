let express = require('express');
let app = express();
app.use('/assets', express.static('./assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html')
});

app.get('/doubling', function(req, res) {
    if (req.query.input !== undefined) {
        res.json({'received': req.query.input * 1, 'result': req.query.input * 2});
    } else {
        res.json({'error': 'Please provide an input!'});
    }
});

app.get('/greeter', function(req, res) {
    if (req.query.name !== undefined && req.query.title !== undefined) {
        res.json({'welcome_message': 'Oh, hi there ' + req.query.name + ', my dear ' + req.query.title + '!'});
    } else if (req.query.name === undefined) {
        res.json({'error': 'Please provide a name!'});
    } else if (req.query.title === undefined) {
        res.json({'error': 'Please provide a title!'});
    }
})

app.get('/appenda/:word', function(req, res) {
    res.json({'appended': req.params.word + 'a'});
})


app.listen(8080);