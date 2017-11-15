const Playlist = function() {

    function showCreateDialog() {
        const plus = document.querySelector('div.playlists > div > span:nth-child(2)');
        plus.addEventListener('click', () => {
            let newPlaylist = window.prompt('Enter new playlist name:');
        });
    };

    function render(playlists) {
        playlists.forEach(playlist => {
            let container = document.querySelector('div.playlists');
            let newDiv = document.createElement('div');
            let structure = `<span>${playlist.playlist_name}</span>
                             <span>X</span>`
            newDiv.innerHTML = structure;
            container.appendChild(newDiv);
        });
    }

    function load() {
        getPlaylist(render)
    }

    showCreateDialog()
    load()

};
