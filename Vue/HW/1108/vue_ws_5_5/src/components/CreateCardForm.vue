<template>
    <div>
        <form>
            <label for="name">이름 : </label>
            <input type="text" id="name" v-model="name" name="name">
            <label for="title">직함 : </label>
            <input type="text" id="title" v-model="title" name="title">
            <button @click.prevent="createCard">명함 추가</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const name = ref('')
const title = ref('')
const emit = defineEmits(['createCardEvent'])
const createCard = function () {
    const card = {
        name: name.value,
        title: title.value
    }   
    emit('createCardEvent', card)
    name.value = ''
    title.value = ''
}

</script>

<style scoped>

</style>