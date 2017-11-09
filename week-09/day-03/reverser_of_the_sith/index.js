let express = require('express');
let cors = require('cors');
let app = express();
let urlencodedParser = express.urlencoded({extended: false});
let port = 8080;

app.use(express.json());
app.use(cors());

// app.use(function(req, res, next) {
//     res.header("Access-Control-Allow-Origin", "*");
//     res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
//     next();
//   });

function changeWordOrder (words) {
    let yoda = []
    for (let i = 0; i + 2 <= words.length; i += 2) {
        yoda.push(words[i + 1]);
        yoda.push(words[i]);
    }
    return yoda;
}

function convert (sentences) {
    let result = [];
    let randoms = ['Uhm', 'Urggh', 'Hmm...', 'Hm..hm', 'Grrrh', 'Argggh', 'Groh']
    sentences.forEach(function(sentence) {
        let words = sentence.split(' ');
        words[0] = words[0].toLowerCase();
        let yoda = changeWordOrder(words);
        if (words.length > yoda.length) {
            yoda.push(words[words.length - 1]);
        }
        yoda[0] = yoda[0].charAt(0).toUpperCase() + yoda[0].slice(1)
        yoda[yoda.length - 1] += '.'; 
        result.push(yoda.join(' '))
        result.push(randoms[Math.round(Math.random() * randoms.length)])
    })
    return result.join(' ');
}

// app.post('/', urlencodedParser, function(req, res){
//     if (req.body.text === '' || req.body.text === undefined){
//         res.json({'error': 'Feed me some text you have to, padawan young you are. Hmmm.'})
//     } else {
//         let words = req.body.text.split('.');
//         res.json({'sith-text': convert(words)})
//     }
// });

app.post('/', function(req, res) {
    // res.setRequestHeader("Access-Control-Allow-Origin", "*");
    res.send('Landed');
})


app.listen(port);