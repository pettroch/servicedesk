<template>
    <label class="inline-flex items-center cursor-pointer">
        <input type="checkbox" value="" class="sr-only peer" checked>
        <p class="text-xs font-mono">Таблица</p>
        <img src="/table.svg" class="w-7 mr-1" />
        <div class="relative w-9 h-5 bg-yellow-300 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-green-400 hover:peer-checked:bg-green-500"></div>
        <img src="/rectangle.svg" class="w-7 ml-1" />
        <p class="text-xs font-mono">Карточки</p>
    </label>
</template>