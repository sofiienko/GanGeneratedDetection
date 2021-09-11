<!-- HTML Template -->
<template>
    <div class="container">

      <h3 v-if="!resultImage">Upload source image</h3>

              <div id="preview0">
          <img v-if="previewImg0" :src="previewImg0" width="254" />
        </div>

      <!--UPLOAD-->
      <form enctype="multipart/form-data" v-if="!resultImage">
        <div class="dropbox">
          <input type="file"  :name="uploadFieldName" :disabled="isSaving" @change="filesChange(0, $event.target.files); fileCount = $event.target.files.length"
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

      <h3 v-if="!resultImage">Upload destination image </h3>

        <div id="preview1">
          <img v-if="previewImg1" :src="previewImg1" width="254" />
        </div>
        <form enctype="multipart/form-data" v-if="!resultImage" >
          <div class="dropbox">
          <input type="file"  :name="uploadFieldName" :disabled="isSaving" @change="filesChange(1, $event.target.files); fileCount = $event.target.files.length"
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


        <div id="resultImage">
          <img v-if="resultImage" :src="'data:image/jpeg;base64,' + resultImage" width="254" />
        </div>

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
        previewImg0: null,
        previewImg1: null,
        resultImage: null,
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
        this.formData = null,
        this.data = null;
        this.previewImg0 = null;
        this.previewImg1 = null;
        this.resultImage = null,
        this.currentStatus = STATUS_INITIAL;
        this.uploadedFiles = [];
        this.uploadError = null;
      },
      save(formData) {
        // upload data to the server
        this.currentStatus = STATUS_SAVING;

        upload(formData)
          .then(x => {
            // x.status =  x.status.slice(0, 2)
            // x.status =   x.status.slice(0, -1)
            this.resultImage = x.status;
            // this.resultImage = urlCreator.createObjectURL(t)
            // this.uploadedFiles = [].concat(x);
            // this.currentStatus = STATUS_SUCCESS;
            // this.data = x;
          })
          .catch(err => {
            console.log(err)
            var r  = formData.get(0);
            this.uploadError = err.response === undefined ? err.message : err.response;
            this.currentStatus = STATUS_FAILED;
          });
      },
      //https://stackoverflow.com/questions/49106045/preview-an-image-before-it-is-uploaded-vuejs
      filesChange(fieldName, fileList) {



          console.log(fieldName)
          console.log( fileList)
        // handle file changes

        if (!fileList.length) return;

        if(this.formData)
        {
          this.formData.append(1, fileList[0], fileList[0].name)
          this.previewImg1 = URL.createObjectURL(this.formData.get(1));

          this.save(this.formData);
        }
        else{
          this.formData = new FormData();
          this.formData.append(0,fileList[0], fileList[0].name)
          this.previewImg0 = URL.createObjectURL(this.formData.get(0));
        }
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