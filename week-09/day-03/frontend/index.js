let express = require('express');
let app = express();
let bodyParser = require('body-parser')
let urlencodedParser = bodyParser.urlencoded({extended: false});
app.use(bodyParser.json());
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

app.post('/dountil/:type', urlencodedParser, function(req, res) {
    if (req.params.type === 'sum') {
        let number = req.body.until;
        let sums = 0;
        while (number > 0) {
            sums += number;
            number -= 1;
        }
        res.json({'result': sums});
    } 
    else if (req.params.type === 'factor') {
        let number = req.body.until;
        let factor = 1;
        while (number > 0) {
            factor *= number;
            number -= 1;
        }
        res.json({'result': factor});
    } 
});


app.listen(8080);