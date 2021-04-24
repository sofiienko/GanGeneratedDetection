import * as axios from 'axios';

const BASE_URL = 'http://localhost:5000/predict';

function upload(formData) {
    console.log('upload')
    const url = `${BASE_URL}`;
    return axios.post(url, formData)
        // get data
        .then(x => x.data)
}

export { upload }