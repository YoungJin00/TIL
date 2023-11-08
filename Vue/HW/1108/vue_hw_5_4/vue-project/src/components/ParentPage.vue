<template>
  <div>
    <h1> 부모 페이지입니다. </h1>
    <ChildPage 
     v-for="child in children"
     :key="child.name"
     :child="child"
     @some-event="updateBalance(child)"
    />
  </div>
</template>

<script setup>
   import { ref } from 'vue'
   import ChildPage from './ChildPage.vue';
   const children = ref([
    {
      name: '김하나',
      age:30,
      balance:100000 
    },
    {
      name: '김두리',
      age:20,
      balance:10000
    },
    {
      name: '김서이',
      age:10,
      balance:1000
    },
   ])
   const updateBalance = function (children) {
      // console.log(children.balance)

      children.balance += 1000
   }
</script>

<style scoped>
.box {
  border: 1px solid black;
  padding: 10px;
  margin: 5px;
}
</style>