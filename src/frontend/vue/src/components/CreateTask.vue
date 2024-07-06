<script setup>
    import { ref } from 'vue'
    import Tools from "./Tools.vue"
    import TaskCard from "./TaskCard.vue"

    const name = ref("")
    const desc = ref("")
    const isVisible = ref(false)
    const isVisibleEmptyTasks = ref(true)
    const isShowTaskCard = ref(false)

    const showCreateTask = () => {
        isVisible.value = true
    }

    const hideComponent = () => {
        isVisible.value = false
        isVisibleEmptyTasks.value = false
        isShowTaskCard.value = true
    }
</script>

<template>
    <div class="bg-white ml-36 mr-36 m-auto rounded-3xl shadow-lg border mt-7">
        <div class="p-10">
            <p class="text-3xl font-bold">Активные заявки</p>
            
            <Tools />

            <div v-if="isVisibleEmptyTasks" class="m-auto w-max font-mono mt-16 mb-16">
                <img src="/emoji.svg" class="w-64 m-auto" />
                <p class="font-bold text-2xl">Отсутствуют активные заявки...</p>
                <button
                    @click="showCreateTask"
                    type="button"
                    class="flex justify-center items-center text-lg pr-1 mt-1 text-white bg-gradient-to-r from-green-400 via-green-500 to-green-600 hover:bg-gradient-to-br shadow-lg shadow-green-500/50 rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 w-full">
                    <img src="/plus.svg" class="w-6" />
                    Создать
                </button>
            </div>

            <div v-if="isShowTaskCard" class="mt-7">
                <div class="grid grid-cols-6 gap-5">
                    <TaskCard />
                </div>
            </div>
        </div>


        <div v-if="isVisible" class="fixed top-0 left-0 h-full w-full z-10 bg-[#000000b4]">
            <div class="bg-white w-3/5 h-4/5 m-auto mt-20 rounded-3xl">
                <div class="relative">
                    <p class="font-bold text-3xl text-center pt-5">Создание заявки</p>
                    <p @click="hideComponent" class="cursor-pointer text-xl mt-5 absolute inset-y-0 right-0 mr-7">X</p>
                </div>

                
                <div class="m-auto w-11/12 mb-0 mt-5">
                    <div class="p-5">
                        <div>
                            <div class="mb-3">
                                <label class="ml-2.5">Наименование</label>
                                <input v-model="name" type="text" placeholder="Введите наименование" class="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 ml-2.5">
                            </div>
                        
                            <div>
                                <label class="ml-2.5">Описание</label>
                                <textarea v-model="desc" rows="18" placeholder="Введите описание" class="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 ml-2.5">
                                </textarea>
                            </div>
                        </div>
                        <input type="file" class="ml-1 mt-5 p-1 w-80 text-slate-500 text-sm rounded-full leading-6 file:bg-green-500 file:text-white file:font-semibold file:border-none file:px-4 file:py-1 file:mr-6 file:rounded-full hover:file:bg-green-600 border border-gray-300">
                        <button @click="hideComponent"  type="button" class="text-xl mt-5 w-full focus:outline-none text-white hover:cursor-pointer bg-green-600 hover:bg-green-700 active:bg-green-800 rounded-2xl text-sm px-5 py-2.5 me-2 mb-2">Отправить</button>
                    </div>
                </div>
            </div>
    </div>

    </div>
</template>