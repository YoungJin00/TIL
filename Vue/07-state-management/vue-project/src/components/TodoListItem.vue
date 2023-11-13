<script setup>
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()

defineProps({
  todoData: Object,
})
</script>

<template>
    <div>
      <span @click="store.updateTodo(todoData.id)" 
      :class="{'is-done': todoData.isDone}">
        {{ todoData.text }}
      </span>
      <button @click="store.deleteTodo(todoData.id)">x</button>
    </div>
</template>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>
