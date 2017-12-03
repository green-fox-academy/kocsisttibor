import { Component } from '@angular/core';
import { DetailsComponent } from './details/details.component'
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
    let newElement = {
      id: this.todos.length,
      todo: this.newTodo,
      deadline: '',
      description: '' 
    }
    this.todos.push(newElement);
  }

  deleteTodo(event: Event) {
    this.todos.forEach( (todo) => {
      if (todo.id.toString() === (<HTMLInputElement>event.target).classList.value) {
        this.todos.splice(this.todos.indexOf(todo), 1);
      }
    })
  }

}
