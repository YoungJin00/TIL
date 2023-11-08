<template>
  <div>
    <p v-if="businessCards.length !== 0">현재 보유중인 명함 수 : {{ businessCards.length }} </p>
    <p v-else>명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
    <businessCardDetail 
    v-for="(card, index) in businessCards"
    :key="card.name" 
    :card="card"
    @some-Event = "deleteCardEvent(index)"
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

// splice
const deleteCardEvent = function (idx) {
  businessCards.value.splice(idx, 1)
}

</script>

<style scoped>

</style>