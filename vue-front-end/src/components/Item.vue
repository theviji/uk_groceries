<template>
  <v-flex xs12 mx-auto>
    <v-layout card row class="my-1 mx-2 pa-1">
      <v-flex xs8>
        <div>
          <div class="headline">{{ item.name }}</div>
          <div>GBP {{ item.price }}</div>
          <div>{{ item.quantity }}</div>
          <div>{{ item.brand }}</div>
        </div>
      </v-flex>
      <v-flex xs4>
        <a :href="item.link" target="_new">
          <v-card-media
            :src="item.image"
            height="125px"
            contain
          ></v-card-media>
        </a>
      </v-flex>
    </v-layout>
  </v-flex>
</template>

<script>
export default {
  name: 'Item',
  props: ['item'],
  data () {
    return {
    }
  }
}
</script>

<style scoped>
</style>
