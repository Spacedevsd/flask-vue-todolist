import Axios from "axios";
import Vue from "vue";
import Vuex from "vuex";

const http = Axios.create({
  baseURL: "/ws/v1/todos"
});

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    todoList: []
  },
  actions: {
    async getTodos(context) {
      const response = await http.get("/");
      context.commit("GET_TODOS", response.data);
    },
    async addTodo(context, obj) {
      const response = await http.post("/insert", { ...obj });
      context.commit("ADD_TODOS", response.data);
    },
    async doneTodo(context, id) {
      const res = await http.put(`/close/${id}`);

      if (res.status == 200 && res.data.modified > 0) {
        context.commit("DONE_TODO", id);
      }
    }
  },
  mutations: {
    GET_TODOS(state, todos) {
      state.todoList = todos;
    },
    ADD_TODOS(state, todos) {
      state.todoList.unshift({ ...todos });
    },
    DONE_TODO(state, id) {
      const index = state.todoList.findIndex(item => item._id == id);
      state.todoList[index].status = false;
    }
  }
});

export default store;
