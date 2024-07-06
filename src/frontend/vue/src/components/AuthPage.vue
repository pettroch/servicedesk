<script setup>
  import { ref } from "vue"
  import { useRouter } from "vue-router"

  const router = useRouter()

  const login = ref("")
  const password = ref("")

  const onClickAuth = () => {
    if (login.value == "user" && password.value == "user"){
      router.push({name: "active_tasks"})
      
    } else if (login.value == "support" && password.value == "support") {
      alert("yes support")
    } else {
      alert("no")
    }
  }
</script>

<template>
    <div class="pt-2">
      <div class="flex justify-between px-20 border-b border-slate-300">
        <div class="transition hover:-translate-y-0.5 hover:cursor-pointer">
          <img src="/header.png" alt="logo" class="w-80 test" />
          <p class="text-slate-700 text-right font-mono font-bold">ServiceDesk</p>
        </div>
      </div>

      <div class="bg-white m-auto rounded-3xl shadow-lg border w-2/5 mb-40 mt-40">
        <div class="p-10 text-center">
          <p class="text-3xl font-bold">Авторизация</p>
          <div class="p-10">
            <div class="mb-3">
              <label>Логин:</label>
              <input v-model="login" type="text" placeholder="Введите логин" class="w-4/5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 ml-5">
            </div>
            
            <div>
              <label>Пароль:</label>
              <input v-model="password" type="password" placeholder="Введите пароль" class="w-4/5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 ml-2.5">
            </div>
          </div>
          <button @click="onClickAuth" type="button" class="w-4/5 focus:outline-none text-white hover:cursor-pointer bg-green-600 hover:bg-green-700 active:bg-green-800 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2">Войти</button>
        </div>
      </div>
    </div>
</template>