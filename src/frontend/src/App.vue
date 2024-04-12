<script setup>
  import Header from "./components/Header.vue"
  import Tools from "./components/Tools.vue"
  import TaskCard from "./components/TaskCard.vue"
  import EmptyTasks from "./components/EmptyTasks.vue"
</script>

<template>
  <div class="bg-white w-4/5 m-auto pb-10 rounded-3xl shadow-xl mt-14 mb-14">

    <Header />
    
    <div class="bg-white ml-36 mr-36 m-auto rounded-3xl shadow-lg border mt-7">
      <div class="p-10">
        <p class="text-3xl font-bold">Активные заявки</p>

        <Tools />

        <div class="mt-7">
          <EmptyTasks />
          <!-- <div class="grid grid-cols-6 gap-5">
            <TaskCard />
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>