<template>
  <div>
    <p>{{ myMsg }}</p>
    <button @click="updateName">이름 변경 !</button>
  </div>
</template>

<script setup>
defineProps({
  myMsg: String,
})

// 이 업데이트 네임은 밑에 에밋메서드 안과 연관
const emit = defineEmits(['updateName'])

// 이 변수 명은 상관없음
const updateName = function () {
  // emit 안에 네임이 중요
  emit('updateName')
}

</script>

<style scoped>

</style>