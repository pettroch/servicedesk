<script setup>
  import Header from "./components/Header.vue"
  import FilterField from "./components/FilterField.vue"
  import SortField from "./components/SortField.vue"
  import SearchDropField from "./components/SearchDropField.vue";
</script>

<template>
  <div class="bg-white w-4/5 m-auto h-screen rounded-3xl shadow-xl mt-14 mb-14">

    <Header />

    <div class="text-center mt-7">
      <button
        type="button"
        class="text-white bg-green-500 w-64 hover:bg-green-600 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2">
        Создать заявку
      </button>

      <button
        type="button"
        class="text-white bg-slate-400 w-64 hover:bg-slate-500 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2">
        Мои заявки
      </button>
    </div>

    <div class="h-3/4 bg-white w-4/5 m-auto rounded-3xl shadow-xl border mt-7">
      <div class="m-auto w-11/12 h-3/4 mt-4 border">
        <p class="text-3xl font-bold">Активные заявки</p>
        <div class=" w-11/12 m-auto mt-4">
          <div class="flex gap-4">

            <FilterField />
            <SortField />
            <SearchDropField />
            
          </div>
        </div>
      </div>
      

    </div>
  </div>
</template>