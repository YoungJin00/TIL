<script setup>
import { ref } from 'vue'

const question = ref('')
const answer = ref('')
const emit = defineEmits(['createQuizEvent'])
const createQuiz = () => {
  const quiz = {
    question: question.value,
    answer: answer.value
  }
  emit('createQuizEvent', quiz)
  question.value = ''
  answer.value = ''
}

</script>

<template>
  <div class="card w-50 mb-3 mx-auto bg-light">
    <div class="card-body">
      <form>
        <h3>퀴즈 생성</h3>
        <label for="question">문제</label>
        <p></p>
        <textarea v-model="question" name="question" id="question" cols="55" rows="5">

        </textarea>
        <p></p>
        <label for="answer">답안</label>
        <p></p>
        <input v-model="answer" type="text" id="answer" name="answer" style="width: 435px;">
        <p></p>
        <button class="btn btn-primary btn-lg" @click.prevent="createQuiz">퀴즈 생성</button>
      </form>

    </div>
  </div>
  <div>


  </div>
</template>

<style scoped>
.btn {
  width: 100%;
}
</style>
