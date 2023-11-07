<!-- components/singers/SingerDetail.vue -->

<template>
  <div class="singer-card">
    <div class="">
      <h2>가수 이름</h2>
      <img src="@/assets/singer.jpg" alt="Singer Image" class="singer-image singer-image-container">
      <p>가수 소개글</p>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.singer-card {
  border: 1px solid #ccc;
  display: inline-block;
  width: 40%;
  margin: 20px;
  text-align: center;
}

.singer-image-container {
  overflow: hidden;
  border-radius: 50%;
  width: 100px; 
  height: 100px; 
  margin: 0 auto;
}

.singer-image {
  max-width: 100%;
  border-radius: 50%;
  display: block;
  margin: 0 auto;
}

h2 {
  color: #333;
  font-size: 24px;
  margin-top: 10px;
}

p {
  color: #666;
  font-size: 16px;
  margin-bottom: 10px;
}
</style>
