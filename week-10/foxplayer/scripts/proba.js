// // Simple API - will fetch all tags
// var jsmediatags = require("jsmediatags");

// jsmediatags.read("./kocsisttibor/week-10/foxplayer/music/Todd_Terje_-_Margeritha_(mp3.pm).mp3", {
//   onSuccess: function(tag) {
//     console.log(tag);
//   },
//   onError: function(error) {
//     console.log(':(', error.type, error.info);
//   }
// });

function getDuration(src, cb) {
    var audio = new Audio();
    $(audio).on("loadedmetadata", function(){
        cb(audio.duration);
    });
    audio.src = src;
}
getDuration("./kocsisttibor/week-10/foxplayer/music/Todd_Terje_-_Margeritha_(mp3.pm).mp3", function(length) {
    console.log('I got length ' + length);
});