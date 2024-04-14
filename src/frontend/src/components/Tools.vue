<script setup>
    import FilterField from "./FilterField.vue"
    import SortField from "./SortField.vue"
    import SearchField from "./SearchField.vue"
    import Switch from "./SwitchTools.vue"
</script>

<template>
    <div class="m-auto mt-4">
        <div class="flex justify-between">
            <div class="flex gap-2">
                <FilterField />
                <SortField />
                <SearchField />
            </div>
            
            <div class="flex gap-1">
                <button
                    type="button"
                    class="flex justify-center items-center pr-1 text-white bg-blue-500 hover:bg-blue-600 w-36 font-medium rounded-xl text-sm text-center">
                    <img src="/plus.svg" class="w-5" />
                    Создать заявку
                </button>
                <button
                    type="button"
                    class="flex justify-center items-center text-white bg-blue-500 hover:bg-blue-600 w-36 font-medium rounded-xl text-sm text-center">
                    <img src="/my_tasks_btn.svg" class="w-5 mr-1" />
                    Мои заявки
                </button>
            </div>

            <Switch />

        </div>
    </div>
</template>