<template>
    <div class="container">
        <h1>Your IP is {{ ip }}</h1>
        <input type="text" v-model="input.query" placeholder="Query" />
        <button v-on:click="sendData()">Send</button>
        <br />
        <br />
        <div class="tile is-ancestor">
            <div class="tile is-vertical is-8">
                <div class="tile" v-for='(item, index) in response.items' :key='index'>
                    <img :src="item.imageSrc" />
                    <div class="tile is-parent">
                        <article class="tile is-child notification is-info">
                        <p class="title">Middle tile</p>
                        <p class="subtitle">With an image</p>
                        <figure class="image is-4by3">
                            <img :src="item.imageSrc">
                        </figure>
                        </article>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'HelloWorld',
        data () {
            return {
                ip: "",
                input: {
                    query: "",
                },
                response: ""
            }
        },
        mounted() {
            axios({ method: "GET", "url": "https://httpbin.org/ip" }).then(result => {
                this.ip = result.data.origin;
            }, error => {
                console.error(error);
            });
        },
        methods: {
            sendData() {
                axios({ method: "GET", "url": "http://localhost:6543/ocado/"+ this.input.query, "headers": { "content-type": "application/json" } }).then(result => {
                    console.log(result.data);
                    this.response = result.data;
                }, error => {
                    console.error(error);
                });
            }
        }
    }
</script>

<style scoped>
    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }

    textarea {
        width: 600px;
        height: 200px;
    }
</style>