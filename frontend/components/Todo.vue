<template lang="pug">
	div
		div.columns.is-centered
			div.column.is-10-desktop.is-12-mobile.is-10-tablet
				input(type="text", class="input is-medium", placeholder="Insira uma tarefa", v-model="name", v-on:keyup.enter="add")
			div.column.is-expanded.is-mobile
				button(class="button is-primary is-medium is-fullwidth", @click="add") Salvar
		div
			ul.todo-list.todo-list-divider
				li(v-for="todo in todoList", :key="todo._id")
					div
						span(v-if="todo.status", class="is-flex is-justified-between")
							span.is-size-4-desktop.is-size-5-mobile {{ todo.name }}
							button(class="button is-primary is-outlined", @click="done(todo._id)") Concluir
						span(v-else, class="is-flex is-justified-between")
							span
								del.is-size-4-desktop.is-size-5-mobile {{ todo.name }}
							span.has-text-warning Tarefa concluída

</template>

<script>
import Axios from "axios";
import { mapState, mapActions } from "vuex";

const http = Axios.create({
  baseURL: "/ws/v1/todos"
});

export default {
  name: "Todo",
  data() {
    return {
      name: ""
    };
  },
  async mounted() {
    await this.getTodos();
  },
  computed: {
    ...mapState(["todoList"])
  },
  methods: {
    ...mapActions(["getTodos", "addTodo", "doneTodo"]),

    add() {
      this.addTodo({
        name: this.name,
        status: true
      });
      this.name = "";
    },
    done(id) {
      this.doneTodo(id);
    }
  }
};
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

.todo-list-divider > li:nth-child(n + 2) {
  margin-top: 10px;
  margin-bottom: 10px;
  padding-top: 2rem;
  border-top: 1px solid #e5e5e5;
}

.is-justified-between {
  justify-content: space-between;
}
</style>
