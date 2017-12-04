const Tracklist = function() {

    function render(tracklist) {
        let container = document.querySelector('div.tracks')
        let divs = document.querySelectorAll('div.tracks > div');
        for (let i = divs.length - 1; i > 0; i -= 1) {
            container.removeChild(divs[i])
        }
        JSON.parse(tracklist).forEach(track => {
            let container = document.querySelector('div.tracks');
            let newDiv = document.createElement('div');
            newDiv.setAttribute('class', 'track');
            let structure = `<div>${track.track_id}</div>
                             <div>${track.path}</div>
                             <div>DUR</div>`;
            newDiv.innerHTML = structure;
            container.appendChild(newDiv);
        });
    }

    function load() {
        getTracklist(render);
    }

    load();

};