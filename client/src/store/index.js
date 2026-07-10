import {createStore} from "vuex" ; 

export default createStore({
    state(){
        return{
            BASEURL: "https://supreme-enigma-r5694p49x4ghp47p-5000.app.github.dev/" , 
            message:"hello world from src/store/index.json"
        }
    },  

    getters:{
        BASEURL(state){
            return state.BASEURL ; 
        }
    }
})