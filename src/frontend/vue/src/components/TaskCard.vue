<script setup>
    import { useRouter } from "vue-router"

    const router = useRouter()

    const onClick = () => {
        router.push({name: "task_info"})
    }
</script>

<template>
    <div class="relative border rounded-2xl text-center font-mono transition hover:-translate-y-1 hover:shadow-lg">
        <p class="text-sm bg-green-500 rounded-t-2xl p-1 text-white">Создано</p>
        <p class="font-bold text-lg">Заявка #0001</p>
        <p class="text-xs">Пропал Интернет</p>
        <p class="text-xs mt-4 text-slate-600">06.07.2024 19:48:51</p>
        <button @click="onClick" class="bg-gray-600 text-white text-xs p-1.5 rounded-2xl w-2/3 mb-2 mt-1 hover:bg-gray-700">Подробнее</button>
    </div>
</template>