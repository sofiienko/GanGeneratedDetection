<!-- HTML Template -->
<template>
    <div class="container">

        <div id="preview">
          <img v-if="previewImg" :src="previewImg" width="254" />
        </div>
      <div>
        <p :class="data.probability > 0.5? 'generated':'real'" v-if="isSuccess" >
           Result probability to be generated via GAN : {{data.probability}}
        </p>
      </div>

      <h2>Upload images</h2>
      <!--UPLOAD-->
      <form enctype="multipart/form-data" >
        <div class="dropbox">
          <input type="file" multiple :name="uploadFieldName" :disabled="isSaving" @change="filesChange($event.target.name, $event.target.files); fileCount = $event.target.files.length"
            accept="image/*" class="input-file">
            <p v-if="isInitial || isSuccess">
              Drag your file here to begin<br> or click to browse
            </p>
            <p v-if="isSaving">
              Uploading {{ fileCount }} file...
            </p>
            <p v-if="isFailed" >
              Oppps... {{uploadError}}
            </p>
        </div>
      </form>

  </div>
</template>

<!-- Javascript -->
<script>
  import { upload } from '../services/file-upload.service';

  const STATUS_INITIAL = 0, STATUS_SAVING = 1, STATUS_SUCCESS = 2, STATUS_FAILED = 3;

  export default {
    name:'FileUpload',
    data() {
      return {
        data: null,
        previewImg: null,
        uploadedFiles: [],
        uploadError: null,
        currentStatus: null,
        uploadFieldName: 'photos'
      }
    },
    computed: {
      isInitial() {
        return this.currentStatus === STATUS_INITIAL;
      },
      isSaving() {
        return this.currentStatus === STATUS_SAVING;
      },
      isSuccess() {
        return this.currentStatus === STATUS_SUCCESS;
      },
      isFailed() {
        return this.currentStatus === STATUS_FAILED;
      }
    },
    methods: {
      reset() {
        // reset form to initial state
        this.data = null;
        this.previewImg = null;
        this.currentStatus = STATUS_INITIAL;
        this.uploadedFiles = [];
        this.uploadError = null;
      },
      save(formData) {
        // upload data to the server
        this.currentStatus = STATUS_SAVING;

        upload(formData)
          .then(x => {
            this.previewImg = URL.createObjectURL(formData.get('photos'));
            this.uploadedFiles = [].concat(x);
            this.currentStatus = STATUS_SUCCESS;
            this.data = x;
          })
          .catch(err => {
            this.previewImg = URL.createObjectURL(formData.get('photos'));
            this.uploadError = err.response === undefined ? err.message : err.response;
            this.currentStatus = STATUS_FAILED;
          });
      },
      //https://stackoverflow.com/questions/49106045/preview-an-image-before-it-is-uploaded-vuejs
      filesChange(fieldName, fileList) {
        // handle file changes
        const formData = new FormData();

        if (!fileList.length) return;
       // this.previewImg = URL.createObjectURL(fileList[0]);
        // append the files to FormData
        Array
          .from(Array(fileList.length).keys())
          .map(x => {
            formData.append(fieldName, fileList[x], fileList[x].name);
          });

        // save it
        this.save(formData);
      }
    },
    mounted() {
      this.reset();
    },
  }

</script>

<!-- SASS styling -->
<!-- SASS styling -->
<style>
  .container {
    margin: auto;
    width: 50%;
  }

  .generated {
    color : red;
  }

  .real {
    color : green;
  }

  .dropbox {
    outline: 2px dashed grey; /* the dash box */
    outline-offset: -10px;
    background: lightcyan;
    color: dimgray;
    padding: 10px 10px;
    min-height: 70px; /* minimum height */
    position: relative;
    cursor: pointer;
  }

  .input-file {
    opacity: 0; /* invisible but it's there! */
    width: 100%;
    height: 75px;
    position: absolute;
    cursor: pointer;
  }

  .dropbox:hover {
    background: lightblue; /* when mouse over to the drop zone, change color */
  }

  .dropbox p {
    font-size: 1.2em;
    text-align: center;
    padding: 5px 0;
  }

  .error{
    background-color:rgb(158, 110, 110);
  }
  
</style>