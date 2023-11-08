<template>
    <div class="business-card">
      <h3>이름 : {{ card.name  }}</h3>
      <p>직함 : {{ card.title }}</p>
      <button @click="deleteCardFunc">명함 삭제</button>
    </div>
  </template>
  
  <script setup>
  
  defineProps({
    card: Object,
  })
  
  const emit = defineEmits(['someEvent'])
  
  const deleteCardFunc = function () {
    emit('someEvent')
  }
  
  </script>
  
  <style scoped>
  .business-card {
    border: 1px solid rgba(0, 0, 0, 0.178);
    background-color: rgb(240, 236, 236);
    text-align: center;
    padding: 15px;
    margin: 10px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
    display: inline-block;
  }
  </style>
  