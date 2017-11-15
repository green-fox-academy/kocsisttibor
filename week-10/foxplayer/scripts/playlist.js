const Playlist = function() {

    function showCreateDialog() {
        const plus = document.querySelector('.addPlaylist');
        plus.addEventListener('click', () => {
            let newPlaylist = window.prompt('Enter new playlist name:');
            create(newPlaylist);
        });
    };

    function render(playlists) {
        playlists.forEach(playlist => {
            let container = document.querySelector('div.playlists');
            let newDiv = document.createElement('div');
            newDiv.setAttribute('class', 'added_playlist ' + playlist.playlist_id)
            let structure = `<span>${playlist.playlist_name}</span>
            <span>X</span>`
            newDiv.innerHTML = structure;
            container.appendChild(newDiv);
        });
        highlight();
    }
    
    function load() {
        let container = document.querySelector('div.playlists')
        let playlists = document.querySelectorAll('div.playlists > div');
        for (let i = playlists.length - 1; i > 1; i -= 1) {
            container.removeChild(playlists[i])
        }
        getPlaylist(render)
    }
    
    function create(playlist) {
        addPlaylist({playlist_name: playlist}, (result) => {
            console.log('Added playlist: ' + JSON.stringify(result))
        })
        load()
    }
    
    function highlight() {
        let playlists = document.querySelectorAll('div.playlists > div');
        playlists.forEach((playlist) => {
            playlist.addEventListener('click', () => {
                playlists.forEach((playlist) => {
                    playlist.classList.remove('highlighted')
                });
                playlist.classList.add('highlighted');
            });
        });
    }

    showCreateDialog()
    load()

};
