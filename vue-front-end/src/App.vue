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
          <v-card tile flat>
            <v-card-media src="/static/ocado.PNG" contain height="100px"></v-card-media>
          </v-card>
          <v-layout row>
            <v-flex d-flex>
              <v-layout row wrap>
                <v-flex v-for='(item, index) in ocadoResponse.items' :key='index' d-flex xs6>
                  <v-layout card row>
                    <v-flex xs7>
                      <div>
                        <div class="headline">{{ item.name }}</div>
                        <div>GBP {{ item.price }}</div>
                      </div>
                    </v-flex>
                    <v-flex xs5>
                      <a :href="item.link">
                        <v-card-media
                          :src="item.image"
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
          <v-card tile flat>
            <v-card-media src="/static/sainsburys.PNG" contain height="100px"></v-card-media>
          </v-card>
          <v-layout row>
            <v-flex d-flex>
              <v-layout row wrap>
                <v-flex v-for='(item, index) in sainsburysResponse.items' :key='index' d-flex xs6>
                  <v-layout card row>
                    <v-flex xs7>
                      <div>
                        <div class="headline">{{ item.name }}</div>
                        <div>GBP {{ item.price }}</div>
                      </div>
                    </v-flex>
                    <v-flex xs5>
                      <a :href="item.link">
                        <v-card-media
                          :src="item.image"
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
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";
axios.defaults.baseURL = process.env.NODE_ENV === 'production' ? process.env.PROD_API : process.env.DEV_API;

export default {
  name: 'App',
  components: {
  },
  data () {
      return {
          searchText: "",
          ocadoResponse: "",
          sainsburysResponse: "",
      }
  },
  methods: {
      sendData() {
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
