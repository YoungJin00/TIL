<template>
  <div>
    <businessCardDetail 
    v-for="card in businessCards"
    :key="card.name" 
    :card="card"
    @some-Event = "deleteCardEvent"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import businessCardDetail from '@/components/businessCardDetail.vue'

const businessCards = ref([
  {name: '일론 머스크', title: '테슬라 테크노킹'},
  {name: '래리 엘리슨', title: '오라클 창업주'},
  {name: '빌 게이츠', title: '마이크로소프트 창업주'},
  {name: '래리 페이지', title: '구글 공동창업주'},
  {name: '세르게이 브린', title: '구글 공동창업주'},
])

const deleteCardEvent = function () {
  
}

</script>

<style scoped>

</style>