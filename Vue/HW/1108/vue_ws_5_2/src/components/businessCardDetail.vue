<template>
  <div class="business-card">
    <h3>이름 : {{ card.name  }}</h3>
    <p>직함 : {{ card.title }}</p>
  </div>
</template>

<script setup>
defineProps({
  card: Object,
})

</script>

<style scoped>
.business-card {
  border: 1px solid black;
  background-color: rgb(201, 200, 200);
  text-align: center;
  padding: 15px;
  margin: 10px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 300px;
  display: inline-block;
}
</style>