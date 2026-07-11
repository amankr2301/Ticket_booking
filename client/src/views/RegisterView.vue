<script setup>
import CommonNavBar from "@/components/commonnavbar.vue";
import store from "@/store";
</script>

<template>
    <CommonNavBar />

    <div class="container-fluid section-container">

        <div class="signup-card">

            <div class="alert alert-success mb-4" role="alert" v-if="success">
                🎉 Account created successfully!
                <button
                    type="button"
                    class="btn-close"
                    @click="success = false"
                ></button>
            </div>

            <form @submit="signup">

                <div class="text-center mb-4">

                    <div class="logo-circle">
                        👤
                    </div>

                    <h2>Create Account</h2>

                    <p>
                        Join us today and start your journey.
                    </p>

                </div>

                <div class="row">

                    <div class="col-md-6 mb-3">

                        <input
                            type="text"
                            class="form-control custom-input"
                            placeholder="First Name"
                            v-model="firstname"
                        />

                        <div
                            class="invalid-feedback"
                            :style="{ display: error.firstname ? 'block':'none'}"
                        >
                            {{ error.firstname }}
                        </div>

                    </div>

                    <div class="col-md-6 mb-3">

                        <input
                            type="text"
                            class="form-control custom-input"
                            placeholder="Last Name"
                            v-model="lastname"
                        />

                    </div>

                </div>

                <div class="mb-3">

                    <input
                        type="email"
                        class="form-control custom-input"
                        placeholder="Email Address"
                        v-model="email"
                    />

                    <div
                        class="invalid-feedback"
                        :style="{ display: error.email ? 'block':'none'}"
                    >
                        {{ error.email }}
                    </div>

                </div>

                <div class="row">

                    <div class="col-md-6 mb-3">

                        <input
                            type="password"
                            class="form-control custom-input"
                            placeholder="Password"
                            v-model="password"
                        />

                        <div
                            class="invalid-feedback"
                            :style="{ display: error.password ? 'block':'none'}"
                        >
                            {{ error.password }}
                        </div>

                    </div>

                    <div class="col-md-6 mb-4">

                        <input
                            type="password"
                            class="form-control custom-input"
                            placeholder="Confirm Password"
                            v-model="confirm"
                        />

                        <div
                            class="invalid-feedback"
                            :style="{ display: error.confirm ? 'block':'none'}"
                        >
                            {{ error.confirm }}
                        </div>

                    </div>

                </div>

                <button
                    class="btn btn-primary register-btn"
                    type="submit"
                >
                    Create Account
                </button>

                <hr class="my-4">

                <div class="text-center">

                    <small class="text-secondary">

                        Already have an account?

                        <router-link
                            to="/login"
                            class="login-link"
                        >
                            Login
                        </router-link>

                    </small>

                </div>

            </form>

        </div>

    </div>

</template>

<script>
export default {
    data() {
        return {
            firstname: null,
            lastname: null,
            password: null,
            confirm: null,
            email: null,
            success: false, 

            error: {
                firstname: null,
                lastname: null,
                password: null,
                confirm: null,
                email: null,
            },
        };
    },

    methods: {
        validate() {
            let error = false;

            this.error = {
                firstname: null,
                lastname: null,
                password: null,
                confirm: null,
                email: null,
                
            };

            if (!this.firstname || this.firstname.length < 2) {
                error = true;
                this.error["firstname"] = "Required Field";
            }

            if(!this.password){
                error = true;
                this.error["password"] = "Required Field";

            }

            if (this.password !== this.confirm) {
                error = true;
                this.error["confirm"] = "Passwords do not match";
            }

            if (!this.email || !this.email.match(/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/)) {
                error = true;
                this.error["email"] = "Invalid email address";
            }

            return error ; 

        },

        signup(event) {
            event.preventDefault();

            if (!this.validate()) {

                console.log("✈️ Fetch is firing right now!");
                
                fetch(store.getters.BASEURL +"/signup" , {
                    method: "POST", 
                    headers: {
                    "Content-Type": "application/json"
                        },
                    body : JSON.stringify({
                        firstname: this.firstname , 
                        lastname: this.lastname , 
                        email: this.email , 
                        password : this.password , 
                        confirm: this.confirm

                    })
                    })
                    
                    .then(response => {
                        return [response.json() , response.status]; 

                    }).then(data => {
                        if (data[1] == 400){
                            let error = data[0]["error"]
                            if (error === "Email already exists"){
                                this.error["email"] = "Email already in Use"
                            }
                        }
                        else{
                            this.success = true
                        }
                        
                    })
                        
                
            }

            
        },
    },
};
</script>

<style scoped>
.section-container{

    min-height:90vh;

    display:flex;

    justify-content:center;

    align-items:center;

    padding:40px;

    background:
    linear-gradient(
        135deg,
        #111827,
        #1e293b,
        #0f172a
    );

}


.signup-card{

    width:100%;

    max-width:700px;

    padding:45px;

    border-radius:22px;

    background:rgba(30,41,59,.88);

    backdrop-filter:blur(16px);

    box-shadow:
    0 20px 60px rgba(0,0,0,.45);

}


.logo-circle{

    width:80px;

    height:80px;

    border-radius:50%;

    margin:auto;

    margin-bottom:20px;

    display:flex;

    justify-content:center;

    align-items:center;

    font-size:34px;

    background:#2563eb;

    color:white;

    box-shadow:
    0 8px 25px rgba(37,99,235,.5);

}


h2{

    color:white;

    font-weight:700;

}


p{

    color:#b7c2d1;

}


.custom-input{

    height:52px;

    border-radius:12px;

    border:none;

    background:#374151;

    color:white;

    padding-left:18px;

}


.custom-input::placeholder{

    color:#cbd5e1;

}


.custom-input:focus{

    background:#374151;

    color:white;

    border:1px solid #3b82f6;

    box-shadow:
    0 0 10px rgba(59,130,246,.45);

}


.register-btn{

    width:100%;

    height:52px;

    border-radius:12px;

    font-size:17px;

    font-weight:600;

    transition:.3s;

}


.register-btn:hover{

    transform:translateY(-2px);

}


.invalid-feedback{

    display:block;

    color:#ff9d9d;

    margin-top:6px;

}


.alert{

    border-radius:12px;

}


hr{

    border-color:#475569;

}


.login-link{

    color:#60a5fa;

    text-decoration:none;

    font-weight:600;

}


.login-link:hover{

    color:white;

}


@media(max-width:768px){

    .signup-card{

        padding:30px;

    }

}
</style>
