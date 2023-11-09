<script setup>
defineProps({
  quiz: Object,
})

</script>

<template>
  <div class="quiz-container">
    <div class="card">
      <h5>{{ quiz.pk }}번 문제. {{ quiz.question }}</h5>

      <p>정답 입력</p>
      <input type="text" >
    </div>

  </div>
</template>

<style scoped>
.quiz-container {
  text-align: center; /* 가운데 정렬을 위한 스타일 */
}
.card {
  border: 1px solid rgba(0, 0, 0, 0.178);
  background-color: rgb(240, 236, 236);
  padding: 15px;
  margin: 10px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 70%;
  display: inline-block;
}
.card h5 {
  font-weight: bold;
  text-align: left;
}
.card p {
  text-align: left;
}

.card input {
  width: 100%; /* 필요에 따라 조절 */
  padding: 8px; /* 필요에 따라 조절 */
}


</style>
