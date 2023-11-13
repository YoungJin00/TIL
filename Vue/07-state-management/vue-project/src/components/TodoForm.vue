<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js';

const todoText = ref(null)
const store = useCounterStore()

const createTodo = function () {
  store.addTodo(todoText.value)

  todoText.value = ''
}

</script>

<template>
    <div>
      <form @submit.prevent="createTodo(todoText)">
        <input type="text" v-model="todoText">
        <input type="submit">
      </form>
    </div>
</template>

<style scoped>

</style>
