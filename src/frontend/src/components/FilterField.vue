<template>
    <div class="relative">
        <button class="inline-flex justify-center items-center border p-2 rounded-lg hover:bg-gray-50">
            <img src="/filter.svg" class="w-5" />
            <p class="font-mono pl-1">Фильтр</p>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 ml-4"
                viewBox="0 0 20 20"
                fill="currentColor"
            >
                <path
                fill-rule="evenodd"
                d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                clip-rule="evenodd"
                />
            </svg>
        </button>
    </div>
        <!--
        <div
            class="absolute z-10 mt-2 w-56 divide-y divide-gray-100 rounded-md border border-gray-100 bg-white shadow-lg"
            role="menu"
        >
            <div class="p-2">
            <strong class="block p-2 text-sm font-bold text-gray-400"> Статус </strong>

            <a
                href="#"
                class="block rounded-lg px-4 py-2 text-sm text-green-500 hover:bg-gray-50 hover:font-bold"
                role="menuitem"
            >
                Создано
            </a>

            <a
                href="#"
                class="block rounded-lg px-4 py-2 text-sm text-yellow-500 hover:bg-gray-50 hover:font-bold"
                role="menuitem"
            >
                В процессе
            </a>

            <a
                href="#"
                class="block rounded-lg px-4 py-2 text-sm text-purple-500 hover:bg-gray-50 hover:font-bold"
                role="menuitem"
            >
                Запрос
            </a>

            <a
                href="#"
                class="block rounded-lg px-4 py-2 text-sm text-blue-500 hover:bg-gray-50 hover:font-bold"
                role="menuitem"
            >
                Проверка
            </a>
            </div>

            <div class="p-2">

            <form method="POST" action="#">
                <button
                type="submit"
                class="flex w-full items-center gap-2 rounded-lg px-4 py-2 text-sm text-red-700 hover:bg-red-50 hover:font-bold"
                role="menuitem"
                >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2"
                >
                    <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                    />
                </svg>

                Очистить
                </button>
            </form>
            </div>
        </div> -->
</template>