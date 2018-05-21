<template>
  <v-app light>
    <v-container fluid>
      <v-toolbar dense>
        <v-text-field prepend-icon="search"
                      v-model="searchText"
                      hide-details single-line></v-text-field>
        <v-btn @click="sendData" class="primary">submit</v-btn>                    
      </v-toolbar>
      <v-layout row>
        <v-flex xs6 order-rg2>
          <v-layout row>
            <v-flex d-flex>
              <v-layout row wrap>
                <v-flex v-for='(item, index) in response.items' :key='index' d-flex xs6>
                  <v-layout card row>
                    <v-flex xs7>
                      <div>
                        <div class="headline">{{ item.name }}</div>
                        <div>GBP {{ item.price.currentPrice.replace('&poun', '').replace('d;', '') }}</div>
                      </div>
                    </v-flex>
                    <v-flex xs5>
                      <a :href="item.simplifiedBopUrl">
                        <v-card-media
                          :src="item.imageSrc"
                          height="125px"
                          contain
                        ></v-card-media>
                      </a>
                    </v-flex>
                  </v-layout>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs6>
          <v-card dark tile flat color="red darken-4">
            <v-card-text>#2</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  name: 'App',
  components: {
  },
  data () {
      return {
          searchText: "",
          response: ""
      }
  },
  methods: {
      sendData() {
          axios({ method: "GET", "url": "http://localhost:6543/ocado/"+ this.searchText, "headers": { "content-type": "application/json" } }).then(result => {
              console.log(result.data);
              this.response = result.data;
          }, error => {
              console.error(error);
          });
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
