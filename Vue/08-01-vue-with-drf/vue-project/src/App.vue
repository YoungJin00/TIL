<template>
  <header>
    <nav>
      <RouterLink :to= "{ name: ArticleView }">Articles</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'
</script>

<style scoped>
</style>
