<script setup>
import TodoListItem from '@/components/TodoListItem.vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()
</script>

<template>
    <div>
      <TodoListItem 
      v-for="todo in store.todos"
      :key="todo.id"
      :todo-data="todo"
      />
    </div>
</template>

<style scoped>

</style>
