<template>
  <div id="app" class="singer-detail">
    <MainPage />
    <SingerList />
  </div>
</template>

<script setup>
import MainPage from "@/components/MainPage.vue";
import SingerList from "@/components/SingerList.vue";
</script>

<style scoped>
.singer-detail {
  text-align: center;
  margin: 20px;
}
</style>
