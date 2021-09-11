import * as axios from 'axios';

const BASE_URL = 'http://35.247.71.216:5000/predict';

function upload(formData) {
    //console.log(JSON.stringify(formData))
    const url = `${BASE_URL}`;
    return axios.post(url, formData)
        // get data
        .then(x => x.data)
}

export { upload }