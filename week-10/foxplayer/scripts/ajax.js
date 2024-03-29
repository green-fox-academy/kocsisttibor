const ajax = ( method, data, resource, callback ) => {
    const url = 'http://localhost:8080'
    const xhr = new XMLHttpRequest();
    data = data ? data : null;
    xhr.open( method, url + resource );
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send( JSON.stringify(data) );
    xhr.onreadystatechange = () => {
      if ( xhr.readyState === XMLHttpRequest.DONE ) {
        callback( JSON.parse(xhr.response) );
      }
    };
  };

  const getPlaylist = callback => {
    ajax('GET', false, '/playlist', callback);
  }

  const addPlaylist = (data, callback) => {
    ajax('POST', data, '/addplaylist', callback);
  }

  const deletePlaylist = (data, callback) => {
    ajax('POST', data, '/deleteplaylist', callback);
  }

  const getTracklist = callback => {
    ajax('GET', false, '/tracklist', callback);
  }
