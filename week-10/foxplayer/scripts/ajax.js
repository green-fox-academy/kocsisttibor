const ajax = ( method, data, resource, callback ) => {
    const xhr = new XMLHttpRequest();
    data = data ? data : null;
    xhr.open( method, url + resource );
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send( JSON.stringify(data) );
    xhr.onreadystatechange = () => {
      if ( xhr.readyState === XMLHttpRequest.DONE ) {
        console.log(JSON.parse(xhr.response));
        callback( JSON.parse(xhr.response) );
      }
    };
  };

  const getPlaylist = callback => {
      ajax('GET', false, '/playlist', callback);
  }

