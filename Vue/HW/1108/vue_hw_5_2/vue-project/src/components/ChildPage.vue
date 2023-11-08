<template>
  <div>
    <h3>자식 페이지 입니다.</h3>
    <p>이름 : {{ child.name }} </p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: Object,
})

</script>

<style scoped>

</style>