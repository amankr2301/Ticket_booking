import {createStore} from "vuex" ; 

export default createStore({
    state(){
        return{
            BASEURL: "http://127.0.0.1:5000" , 
            user: {
                token:null , 
            }
            
        }
    },  

    getters:{
        BASEURL(state){
            return state.BASEURL ; 
        }
    },

    mutations:{
        setToken(state , value){
            state.user = value ; 
            sessionStorage.setItem("user" , JSON.stringify(value))
        }

    }


}); 