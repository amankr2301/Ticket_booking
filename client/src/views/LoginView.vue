<script setup>
import CommonNavBar from "@/components/commonnavbar.vue";
import store from "@/store";
</script>

<template>
    <CommonNavBar />

    <div class="container-fluid section-container">
        <div class="login-card">

            <div class="alert alert-success mb-4" role="alert" v-if="success">
                Logged in successfully!
                <button
                    type="button"
                    @click="success = false"
                    class="btn-close"
                    data-bs-dismiss="alert"
                    aria-label="Close"
                ></button>
            </div>

            <form @submit="login">
                <h2 class="text-center text-white mb-4">Welcome Back</h2>
                <p class="text-center text-secondary mb-4">
                    Login to continue
                </p>

                <div class="mb-4">
                    <input
                        type="email"
                        class="form-control custom-input"
                        placeholder="Email Address"
                        v-model="email"
                    />

                    <div
                        class="invalid-feedback"
                        :style="{ display: error['email'] ? 'block' : 'none' }"
                    >
                        {{ error["email"] }}
                    </div>
                </div>

                <div class="mb-4">
                    <input
                        type="password"
                        class="form-control custom-input"
                        placeholder="Password"
                        v-model="password"
                    />

                    <div
                        class="invalid-feedback"
                        :style="{ display: error['password'] ? 'block' : 'none' }"
                    >
                        {{ error["password"] }}
                    </div>
                </div>

                <button class="btn btn-primary login-btn" type="submit">
                    Login
                </button>
            </form>

        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email: null,
            password: null,
            success: false,

            error: {
                email: null,
                password: null,
            },
        };
    },

    methods: {
        validate() {
            let error = false;

            this.error = {
                email: null,
                password: null,
            };

            if (
                !this.email ||
                !this.email.match(/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/)
            ) {
                error = true;
                this.error.email = "Invalid email address";
            }

            if (!this.password) {
                error = true;
                this.error.password = "Password is required";
            }

            return error;
        },

        login(event) {
            event.preventDefault();

            if (!this.validate()) {
                let statuscode ; 

                fetch(store.getters.BASEURL + "/signin", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        email: this.email,
                        password: this.password,
                    }),
                })
                    .then(response => {
                        statuscode = response.status ; 
                        return response.json()
                    })
                    .then((data) => {

                        if (statuscode == 404) {

                            let error = data["error"]

                            if (error === "Invalid email or password") {
                                this.error.email = "Invalid email or password";
                            }

                        } 
                        else if (statuscode == 200) {
                            this.success = true;
                            store.commit("setToken", data);                            
                        }

                    })

            }
        },
    },
};
</script>

<style scoped>
.section-container {
    min-height: 90vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 30px;
}

.login-card {
    width: 100%;
    max-width: 430px;
    background: rgba(30, 41, 59, 0.95);
    border-radius: 18px;
    padding: 40px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.45);
}

.custom-input {
    background-color: #374151;
    border: 1px solid #4b5563;
    color: white;
    height: 50px;
}

.custom-input::placeholder {
    color: #cbd5e1;
}

.custom-input:focus {
    background-color: #374151;
    color: white;
    border-color: #3b82f6;
    box-shadow: 0 0 8px rgba(59, 130, 246, 0.5);
}

.login-btn {
    width: 100%;
    height: 50px;
    font-size: 17px;
    font-weight: 600;
    border-radius: 10px;
    transition: 0.3s;
}

.login-btn:hover {
    transform: translateY(-2px);
}

.invalid-feedback {
    display: block;
    color: #ff8b8b;
    margin-top: 6px;
}

.alert {
    border-radius: 10px;
}
</style>