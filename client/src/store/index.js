import {createStore} from "vuex" ; 

export default createStore({
    state(){
        return{
            BASEURL: "https://sturdy-palm-tree-p5wvjpjv59jh6q6w-5000.app.github.dev" , 
            message:"hello world from src/store/index.json"
        }
    },  

    getters:{
        BASEURL(state){
            return state.BASEURL ; 
        }
    }
})