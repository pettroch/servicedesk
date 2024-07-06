<script setup>
    import { useRouter } from "vue-router"

    const router = useRouter()

    const onClick = () => {
        router.push({name: "login"})
    }
</script>

<template>
    <header class="flex justify-between px-20 py-6 border-b border-slate-300">
        <div class="transition hover:-translate-y-0.5 hover:cursor-pointer">
            <img src="/header.png" alt="logo" class="w-80 test" />
            <p class="text-slate-700 text-right font-mono font-bold">ServiceDesk</p>
        </div>
                
        <ul class="flex items-center gap-6">
            <li class="flex items-center hover:cursor-pointer transition hover:-translate-y-0.5 hover:font-bold active:text-slate-600">
            <img src="/create_task.svg" class="w-6" />
            <p class="text-base font-mono">Создать заявку</p>
            </li>

            <li class="flex gap-1 items-center hover:cursor-pointer transition hover:-translate-y-0.5 hover:font-bold active:text-slate-600">
            <img src="/my_tasks.svg" class="w-6"/>
            <p class="text-base font-mono">Мои заявки</p>
            </li>

            <li class="flex items-center hover:cursor-pointer transition hover:-translate-y-0.5 hover:font-bold active:text-slate-600">
            <img src="/exit.svg" class="w-6" />
            <p @click="onClick" class="text-base font-mono">Выход</p>
            </li>
        </ul>
    </header>
  </template>