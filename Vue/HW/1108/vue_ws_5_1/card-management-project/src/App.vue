<template>
  <div class="container">
    <header class="header">
      <h1>명함 관리 페이지</h1>
    </header>
    <main class="main">
      <span>명함을 관리하는 페이지입니다.</span>
    </main>
    <article class="article">
      <span>여기에 명함 목록이 표시됩니다.</span>
    </article>
    <footer class="footer">
      <p>&copy;2023 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>
</script>

<style scoped>
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

.main {
  padding: 20px;
}

.footer {
  background-color: grey;
  padding: 10px;
  text-align: center;
  width: 100%;
  position: fixed;
  bottom: 0;
}
</style>
