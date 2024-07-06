<script setup>
  import Header from "./components/Header.vue"
</script>

<template>
  <div class="bg-white w-4/5 m-auto pb-10 rounded-3xl shadow-xl mt-14 mb-14">

    <Header />
    
    <router-view />

    <!--<Header />-->

  </div>
</template>