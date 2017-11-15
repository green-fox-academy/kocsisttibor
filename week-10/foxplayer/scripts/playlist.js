const Playlist = function() {

    function showCreateDialog() {
        const plus = document.querySelector('.addPlaylist');
        plus.addEventListener('click', () => {
            let newPlaylist = window.prompt('Enter new playlist name:');
            create(newPlaylist);
        });
    };

    function render(playlists) {
        let container = document.querySelector('div.playlists')
        let divs = document.querySelectorAll('div.playlists > div');
        for (let i = divs.length - 1; i > 0; i -= 1) {
            container.removeChild(divs[i])
        }
        playlists.forEach(playlist => {
            let container = document.querySelector('div.playlists');
            let newDiv = document.createElement('div');
            newDiv.setAttribute('class', 'added_playlist ' + playlist.playlist_id)
            let structure = `<span>${playlist.playlist_name}</span>
                             <span class="del_button" data-id="${playlist.playlist_id}">X</span>`   //data prefix can store anything linked to the element; name after data (id) is also changeable -> dataset. is used to grab this information
            newDiv.innerHTML = structure;
            container.appendChild(newDiv);
        });
        highlight();
        del();
    }
    
    function load() {
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
                    playlist.classList.remove('highlighted');
                });
                playlist.classList.add('highlighted');
            });
        });
    }

    function del() {
        let del_buttons = document.querySelectorAll('span.del_button');
        del_buttons.forEach((button) => {
            button.addEventListener('click', () => {
                deletePlaylist({playlist_to_delete:button.dataset.id}, render);
            });
        });
    }

    showCreateDialog()
    load()

};
