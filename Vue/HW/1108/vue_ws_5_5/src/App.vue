<template>
    <div class="container">
      <header class="header">
        <h1>명함 관리 페이지</h1>
      </header>
      <main class="main">
        <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
        <h1>보유 명함 목록</h1>
  
      </main>
      <article>
        <CreateCardForm @create-card-event="updateCard"/>
        <BusinessCard :newCard="newCard" />
      </article>
      <footer class="footer">
        <p>&copy;2023 My Business Cards</p>
      </footer>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import BusinessCard from '@/components/BusinessCard.vue'
  import CreateCardForm from '@/components/CreateCardForm.vue'
  const newCard = ref({})
  const updateCard = function (card) {
    newCard.value = card
  }

  </script>
  
  <style scoped>
  * {
    text-align: center;
  }
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .header {
    background-color: rgb(56, 130, 228);
    color: #fff;
    padding: 20px;
    text-align: center;
  }
  h1 {
    text-align: center;
  }
  
  .main {
    padding: 20px;
  }
  
  .footer {
    background-color: grey;
    text-align: center;
    width: 100%;
    position: fixed;
    bottom: 0;
  }
  </style>
  