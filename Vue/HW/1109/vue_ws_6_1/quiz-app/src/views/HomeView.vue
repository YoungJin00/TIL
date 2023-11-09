<template>
  <div class="sort">
    <h3>퀴즈 앱 사용 방법</h3>

    <h1>1. 퀴즈 목록 확인하기</h1>
    <p>퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요.</p>
    <img src="@/assets/quizList.png" alt="#">
    <h1>2. 퀴즈 생성하기</h1>
    <p>퀴즈는 직접 생성 할 수도 있어요.</p>
    <img src="@/assets/quizCreate.png" alt="#">
    <h1>3. 정답 페이지</h1>
    <p>작성한 답안이 정답인지 확인하세요.</p>
    <img src="@/assets/quizAnswer.png" alt="#">
  </div>
</template>

<script setup>

</script>

<style scoped>
.sort {
  text-align: center;
}

.sort > h1,
.sort > p {
  margin-bottom: 20px;
}


div > img {
  max-width: 70%; /* 이미지가 부모 요소를 넘어가지 않도록 설정 */
  height: auto; /* 가로비율을 유지한 채로 높이를 자동 조절 */
}
</style>