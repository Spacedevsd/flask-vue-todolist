<template lang="pug">
	div
		div.columns.is-centered
			div.column.is-10-desktop.is-12-mobile.is-10-tablet
				input(type="text", class="input is-medium", placeholder="Insira uma tarefa", v-model="name", v-on:keyup.enter="addTodo")
			div.column.is-expanded.is-mobile
				button(class="button is-primary is-medium is-fullwidth", @click="addTodo") Salvar
		div
			ul.todo-list.todo-list-divider
				li(v-for="todo in todos", :key="todo._id")
					div
						span(v-if="todo.status", class="is-flex is-justified-between")
							span {{ todo.name }}
							button(class="button is-primary is-outlined", @click="closeTodo(todo._id)") Concluir
						span(v-else, class="is-flex is-justified-between")
							span
								del.is-size-4-desktop.is-size-5-mobile {{ todo.name }}
							span.has-text-warning Tarefa concluída

</template>

<script>
import Axios from "axios";

const http = Axios.create({
	baseURL: "/ws/v1/todos"
})


export default {
	name: "Todo",
	data() {
		return {
			todos: [],
			name: ""
		}
	},
	async mounted() {
		this.todos = await this.getTodos()
	},
	methods: {
		async addTodo() {
			const res = await http.post("/insert", { name: this.name, status: true })
			this.todos.push({ ...res.data })
			this.name = ""
		},
		async getTodos() {
			const res = await http.get("/")
			return res.data;
		},
		async closeTodo(_id) { 
			const res = await http.put(`/close/${_id}`)

			if(res.status == 200 && res.data.modified > 0){
				const index = this.todos.findIndex(item => item._id == _id)
				this.todos[index].status = false;
			}
		}
	}
}
</script>

<style>
.todo-list {
	margin-top: 3rem;
}

.todo-list li {
	padding-top: 1rem;
	padding-bottom: 1rem;
}

.todo-list li span {
	color: white;
}

.todo-list li button ~ span {
	margin-left: 16px;
}

.todo-list > li::before,
.todo-list > li::after {
	content: "";
	display: table;
}

.todo-list > li::after {
	clear: both;
}

.todo-list-divider > li:nth-child(n+2) {
	margin-top: 10px;
	margin-bottom: 10px;
	padding-top: 2rem;
	border-top: 1px solid #e5e5e5;
}

.is-justified-between {
	justify-content: space-between;
}

</style>