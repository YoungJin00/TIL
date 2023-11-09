<script setup>
import { RouterLink, RouterView } from 'vue-router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min'
</script>

<template>
  <header>
    <div class="card border-dark text-center mb-4 mx-auto" style="max-width: 30rem;">
      <div class="card-header border-success color">
        <h1>
          Quiz 퀴즈
        </h1> 
      </div>
      <div class="card-body text-success">
        <p class="card-text">
          여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요 지금 바로 도전해보세요!
        </p>
      </div>
      <div class="card-footer bg-transparent border-success">
        <nav>
          <RouterLink :to="{ name: 'home' }">Home</RouterLink>
        </nav>
      </div>
    </div>

  </header>

  <RouterView />
</template>

<style scoped>
.color {
  background-color: orange;
  color: aliceblue;
}

</style>

