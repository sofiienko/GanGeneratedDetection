import * as axios from 'axios';

const BASE_URL = 'http://192.168.43.206:8080/';
const ID = `${BASE_URL}/{img}/id{imagereceive}`;

//
    //console.log('upload')
    //const url = `${BASE_URL}`;
    //const id = ID;
    //return axios.post(url, formData, id)
        // get data
        //.then(x => x.data)
//}
function upload(formData, guid) {
formElem.onsubmit = async (e) => {
    e.preventDefault();

    let response = await fetch(`${BASE_URL}`, {
      method: 'POST',
      body: new FormData(formElem)
    });

    let result = await response.json();

    alert(result.message);
}
}

export { upload }