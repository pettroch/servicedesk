import './assets/main.css'

import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import CreateTask from './components/CreateTask.vue'
import AuthPage from './components/AuthPage.vue'
import InfoTask from './components/InfoTask.vue'

const router = createRouter({
    routes: [{
        path: "/active_tasks",
        name: "active_tasks",
        component: CreateTask
    },
    {
        path: "/login",
        name: "login",
        component: AuthPage
    },
    {
        path: "/info_task",
        name: "task_info",
        component: InfoTask
    }],
    history: createWebHistory()
})

const app = createApp(App)
app.use(router)
app.mount("#app")
