const Playlist = function() {
    function showCreatDialog() {
        const plus = document.querySelector('div.playlists > div > span:nth-child(2)');
        plus.addEventListener('click', () => {
            console.log('click')
            let newPlaylist = window.prompt('Enter new playlist name:');
        });
    };
    showCreatDialog()
};
