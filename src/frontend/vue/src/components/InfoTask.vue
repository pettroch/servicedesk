<template>
    <div class="bg-white ml-36 mr-36 m-auto rounded-3xl shadow-lg border mt-7">
      <p class="text-3xl font-mono ml-20 mt-5">Заявка #0001</p>

      <div class="pt-5 pb-5 bg-white ml-12 mr-12 m-auto rounded-3xl border flex flex-col">
        <div class="flex justify-between mr-10">
          <div>
              <label class="font-bold ml-10">Наименование</label>
              <input readonly class="p-1 ml-8 bg-zinc-300 w-80 rounded-lg pl-3" value="Пропал Интернет">
          </div>
          <div>
              <label class="font-bold ml-10">Статус</label>
              <input readonly class="p-1 ml-12 bg-zinc-300 w-80 rounded-lg pl-3 text-green-600 font-bold" value="Создано">
          </div>
        </div>

        <div class="flex justify-between mt-4 mr-10">
          <div>
              <label class="font-bold ml-10">Исполнитель</label>
              <input readonly class="p-1 ml-12 bg-zinc-300 w-80 rounded-lg pl-3" value="Петроченко С. А.">
          </div>
          <div>
              <label class="font-bold ml-10">Дата</label>
              <input readonly class="p-1 ml-12 bg-zinc-300 w-80 rounded-lg pl-3" value="06.07.2024 19:48:51">
          </div>
        </div>
      </div>

      <p class="text-2xl font-mono ml-20 mt-5">Описание</p>
      <textarea readonly value="asd" rows="10" cols="175" class="ml-10 mr-10 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 ml-2.5">
        Здравствуйте. Я сидел работал в CRM, вдруг просто пропадает Интернет и ничего не грузит</textarea>
    
      <p class="text-2xl font-mono ml-20 mt-5">Чат с исполнителем</p>
      <div class="pb-20 bg-white ml-12 mr-12 m-auto rounded-3xl border flex flex-col"></div>

      <button type="button" class="mt-5 ml-10 w-11/12 focus:outline-none text-white hover:cursor-pointer bg-red-600 hover:bg-red-700 active:bg-red-800 rounded-2xl text-ml py-1.5 me-2 mb-2">Отменить заявку</button>
    </div>
</template>