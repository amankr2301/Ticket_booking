<script setup>
import CommonNavBar from "@/components/commonnavbar.vue";
</script>

<template>
    <CommonNavBar />

    <div class="container-fluid section-container">
        <div class="card">
            <!-- @ is shortcut for v-on -->
            <form @submit="signup">
                <div class="card-body">
                    <h5 class="card-title text-center">Sign Up</h5>

                    <div class="row">
                        <div class="col">
                            <input type="text" class="form-control" placeholder="First name" aria-label="First name"
                                v-model="firstname" />

                            <div class="invalid-feedback" :style="{ display: error['firstname'] ? 'block' : 'none' }">
                                {{ error["firstname"] }}
                            </div>
                        </div>

                        <div class="col">
                            <input type="text" class="form-control" placeholder="Last name" aria-label="Last name"
                                v-model="lastname" />
                        </div>
                    </div>
                </div>

                <div class="card-body">
                    <div class="row">
                        <div class="col">
                            <input type="email" class="form-control" placeholder="Username" 
                                aria-label="username" v-model="email" />

                        <div
                            class="invalid-feedback" :style="{ display: error['email'] ? 'block' : 'none' }">
                        
                            {{ error["email"] }}
                        </div>
                            
                                
                        </div>

                        <div class="col">
                            <input type="password" class="form-control" placeholder="Password" aria-label="password"
                                v-model="password" />

                            <div class="invalid-feedback" :style="{ display: error['password'] ? 'block' : 'none' }">
                                {{ error["password"] }}
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card-body">
                    <div class="row">
                        <div class="col">
                            <input type="password" class="form-control" placeholder="Confirm Password"
                                aria-label="password" v-model="confirm" />

                            <div class="invalid-feedback" :style="{ display: error['confirm'] ? 'block' : 'none' }">
                                {{ error["confirm"] }}
                            </div>
                        </div>

                        <div class="col">
                            <input type="submit" class="btn btn-primary" value="Register" />
                        </div>
                    </div>
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

        },

        signup(event) {
            event.preventDefault();

            if (!this.validate()) {
                return;
            }

            console.log("Form Submitted");
        },
    },
};
</script>

<style scoped>
.section-container {
    display: flex;
    height: 90vh;
    justify-content: center;
    align-items: center;
}

.row {
    margin-top: 20px;
}

.btn {
    width: 100%;
}
</style>
