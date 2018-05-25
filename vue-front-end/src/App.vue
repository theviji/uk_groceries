<template>
  <v-app light>
    <v-container fluid>
      <v-toolbar dense>
        <v-text-field ref="inputField" 
                      @keyup.enter="submit" 
                      prepend-icon="search"
                      v-model="searchText"
                      hide-details single-line required></v-text-field>
        <v-btn @click="submit" class="primary">submit</v-btn>
        <v-btn @click="clear">clear</v-btn>
      </v-toolbar>
      <v-layout row>
        <v-flex xs6 order-rg2>
          <v-card tile flat>
            <v-card-media src="/static/ocado.PNG" contain height="100px"></v-card-media>
          </v-card>
          <v-layout row>
            <v-flex>
              <v-layout row wrap>
                <Item
                  v-for='item in ocadoResponse.items' 
                  :key='item.index'
                  :item='item'
                  />
              </v-layout>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs6>
          <v-card tile flat>
            <v-card-media src="/static/sainsburys.PNG" contain height="100px"></v-card-media>
          </v-card>
          <v-layout row>
            <v-flex>
              <v-layout row wrap>
                <Item
                  v-for='item in sainsburysResponse.items' 
                  :key='item.index'
                  :item='item'
                  />
              </v-layout>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import Item from './components/Item'

import axios from "axios";
axios.defaults.baseURL = process.env.NODE_ENV === 'production' ? process.env.PROD_API : process.env.DEV_API;

export default {
  name: 'App',
  components: {
    Item
  },
  data () {
      return {
          searchText: "",
          ocadoResponse: "",
          sainsburysResponse: "",
      }
  },
  methods: {
      submit () {
        axios.all([
          axios.get("/ocado/"+ this.searchText),
          axios.get("/sainsburys/"+ this.searchText)
        ])
        .then(axios.spread((ocadoRes, sainsburysRes) => {
          this.ocadoResponse = ocadoRes.data,
          this.sainsburysResponse = sainsburysRes.data,
          console.log(this.ocadoResponse),
          console.log(this.sainsburysResponse)
        }));
    },
    clear () {
      this.$refs.inputField.reset()
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
