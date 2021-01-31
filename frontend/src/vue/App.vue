<template>
  <div id="app">
    <ul>
      <li>
        <router-link to="/page1">Go to Page 1</router-link>
      </li>
      <li>
        <router-link to="/page2">Go to Page 2</router-link>
      </li>
    </ul>
    <router-view></router-view>
    <hr />
    <hr />
    <div>
      <form @submit.prevent>
        <input type="text" v-model="input"/>
        <button type="" @click="sendMessage">Send</button>
      </form>
    </div>
    <h3>Created Messages:</h3>
    <div v-for="(item, index) in messages" :key="index">
      <p>
        {{ item.text }} <small>({{ index }})</small>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      input: '',
    };
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      this.$axios
        .get("api/messages/")
        .then((res) => {
          this.messages = res.data;
        })
        .catch((e) => console.log(e));
    },
    sendMessage() {
      this.$axios
      .post("api/messages/", {
        text: this.input
      })
      .then((res) => {
        this.messages.push(res.data)
      })
      .catch((e) => console.log(e));
    },
  },
};
</script>

<style>
</style>