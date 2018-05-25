<template>
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
