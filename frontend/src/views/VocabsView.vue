<script setup lang="ts">
import {ref} from "vue";

interface GetNewWordResponse {
  german: string;
  english: string;
}

type COLOR =
  "primary"
  | "secondary"
  | "success"
  | "info"
  | "warning"
  | "error"
  | "neutral"
  | undefined

const newWord = ref<GetNewWordResponse | null>(null)
const showMeaning = ref<boolean>(false)
const userInput = ref<string>("")
const inputColor = ref<COLOR>("neutral")

function resetInputField() {
  inputColor.value = "neutral"
  userInput.value = ""
}

async function getNewWord() {
  const response = await fetch('http://127.0.0.1:8000/vocab')
  newWord.value = await response.json()
  toggleEnglish(false)
  resetInputField()
}

function toggleEnglish(toggleValue: boolean) {
  showMeaning.value = toggleValue
}

function checkUserInput() {
  toggleEnglish(true)
  if (userInput.value.toLowerCase() !== newWord.value?.english.toLowerCase()) {
    inputColor.value = "error"
  } else {
    inputColor.value = "success"
  }
}
</script>

<template>
  <UContainer>
    <UButton class="mt-6" @click=getNewWord>Get New Word</UButton>
    <!--  card  -->
    <div class="flex flex-row gap-5 mt-6">
      <UCard class="grow basis-0">
        <template #header>
          German
        </template>

        {{ newWord?.german }}

        <!--   <template #footer>
              <Placeholder class="h-8" />
            </template>-->
      </UCard>
      <div class="grow basis-0">
        <UButton v-show="!showMeaning" @click="toggleEnglish(true)">Show Meaning</UButton>
        <Transition name="fade">
          <UCard v-show="showMeaning">
            <template #header>
              English
            </template>

            {{ newWord?.english }}

            <!--   <template #footer>
                    <Placeholder class="h-8" />
                  </template>-->
          </UCard>
        </Transition>
      </div>
    </div>
    <div class="flex flex-row gap-2 mt-6">
      <UInput :color="inputColor" highlight v-model="userInput"/>
      <UButton @click=checkUserInput>Check</UButton>
    </div>
  </UContainer>
</template>


<style scoped>
.fade-enter-active {
  transition: all 0.5s ease;
}

.fade-leave-active {
  transition: none;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 1;
  scale: 0;
}
</style>
