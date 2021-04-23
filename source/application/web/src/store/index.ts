import Vue from 'vue';
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        rowImage:{},
        processedImage:{},
    },
    mutations:{
        addRowImage(state, image):void{
            state.rowImage = image;
        },
        addProcessedImage(state, image):void{
            state.processedImage = image;
        }
    },
});