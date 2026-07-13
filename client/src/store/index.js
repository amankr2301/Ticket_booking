import {createStore} from "vuex" ; 

export default createStore({
    state(){
        return{
            BASEURL: "http://127.0.0.1:5000" , 
            // BASEURL: "https://glorious-space-trout-rjr5rg769x3wqr9-5000.app.github.dev/",
            user: {
                roles: [] , 
                token:null , 
            }
            
        }
    },  

    getters:{
        BASEURL(state){
            return state.BASEURL ; 
        },
        getToken(state){
            return state.user["token"]
        }, 
        getRoles(state){
            return state.user["roles"]
        }
        
    },

    mutations:{
        setToken(state , value){
            state.user = value ; 
            sessionStorage.setItem("user" , JSON.stringify(value))
        }

    }


}); 