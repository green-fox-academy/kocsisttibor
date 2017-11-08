let express = require('express');
let app = express();
let urlencodedParser = express.urlencoded({extended: false});
let port = 8080;
app.use(express.json());

app.post('/arrays', urlencodedParser, function(req, res) {
    if (req.body.what === 'sum') {
        let sums = 0;
        req.body.numbers.forEach(function(x) {
           sums += x; 
        });
        res.json({'result': sums});
    } else if (req.body.what === 'multiply') {
        let multi = 1;
        req.body.numbers.forEach(function(x) {
           multi *= x; 
        });
        res.json({'result': multi});
    } else if (req.body.what === 'double') {
        let double = req.body.numbers.map(function(x) {
             return x * 2;
        })
        res.json({'result': double})
    }
})


app.listen(port);