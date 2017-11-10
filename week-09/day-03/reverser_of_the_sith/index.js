let express = require('express');
let cors = require('cors');
let app = express();
let urlencodedParser = express.urlencoded({extended: false});
let port = 8080;

app.use(express.json());
app.use(cors());

function changeWordOrder (words) {
    let yodaOrder = []
    for (let i = 0; i + 2 <= words.length; i += 2) {
        yodaOrder.push(words[i + 1]);
        yodaOrder.push(words[i]);
    }
    return yodaOrder;
}

function convertToYodaish (sentences) {
    let newSentences = [];
    let randoms = ['Uhm', 'Urggh', 'Hmm...', 'Hm..hm', 'Grrrh', 'Argggh', 'Groh']
    sentences.forEach(function(sentence) {
        let words = sentence.split(' ');
        words[0] = words[0].toLowerCase();

        let yodaOrder = changeWordOrder(words);
        
        if (words.length > yodaOrder.length) {
            yodaOrder.push(words[words.length - 1]);
        }
        yodaOrder[0] = yodaOrder[0].charAt(0).toUpperCase() + yodaOrder[0].slice(1)
        yodaOrder[yodaOrder.length - 1] += '.'; 
        newSentences.push(yodaOrder.join(' '))
        newSentences.push(randoms[Math.round(Math.random() * randoms.length)])
    })
    return newSentences.join(' ');
}

app.post('/', urlencodedParser, function(req, res){
    console.log(req.body)
    if (req.body.text === '' || req.body.text === undefined){
        res.json({'error': 'Feed me some text you have to, padawan young you are. Hmmm.'})
    } else {
        let words = req.body.text.split('.');
        res.json({'sithtext': convertToYodaish(words)})
    }
});

app.listen(port);