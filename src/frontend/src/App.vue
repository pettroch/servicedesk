<script setup>

</script>

<template>
  <div class="bg-white w-4/5 m-auto h-screen rounded-3xl shadow-xl mt-14 mb-14">
    <header class="flex justify-between px-20 py-6 border-b border-slate-300">
      <div class="hover:-translate-y-0.5 hover:cursor-pointer">
        <img src="/header.png" alt="logo" class="w-80 test" />
        <p class="text-slate-700 text-right font-mono font-bold">ServiceDesk</p>
      </div>
            
      <ul class="flex items-center gap-6">
        <li class="flex items-center hover:cursor-pointer hover:-translate-y-0.5 hover:font-bold">
          <img src="/create_task.svg" class="w-5" />
          <p class="text-sm font-mono">Создать заявку</p>
        </li>

        <li class="flex gap-1 items-center hover:cursor-pointer hover:-translate-y-0.5 hover:font-bold">
          <img src="/my_tasks.svg" class="w-5"/>
          <p class="text-sm font-mono">Мои заявки</p>
        </li>

        <li class="flex items-center hover:cursor-pointer hover:-translate-y-0.5 hover:font-bold">
          <img src="/exit.svg" class="w-5" />
          <p class="text-sm font-mono">Выход</p>
        </li>
      </ul>
    </header>
  </div>
</template>