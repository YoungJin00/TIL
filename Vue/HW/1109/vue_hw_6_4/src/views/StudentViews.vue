<template>
  <div>
    <h1>학생 상세 정보 목록입니다.</h1>
    <a v-for="student in students">
      <router-link :to="{ name: 'student', params: { name: student.name } }">
          <p>{{ student.name }} 학생 정보 보기</p>
      </router-link>
    </a>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const students = ref([
  {name: '김하나'},  
  {name: '김두리'},  
  {name: '김서이'},  
])


</script>

<style scoped>

</style>