import { Component } from '@angular/core';
import { TodosService } from './todos.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Todos';
  todos
  display = false;
  newTodo

  constructor(service: TodosService) {
    this.todos = service.getTodos()
  }

  displayTodos() {
    this.display = true;
  }

  addTodo() {
    this.todos.push(this.newTodo);
  }

}
