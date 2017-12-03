import { Injectable } from '@angular/core';

@Injectable()
export class TodosService {

  constructor() { }

  getTodos() {
    return [
      { todo: 'eat',
        deadline: '2017.12.01',
        description: 'go to the kitchen' }, 
      { todo: 'sleep',
        deadline: '2017.12.02',
        description: 'go to bed' },
      { todo: 'repeat',
        deadline: '2017.12.01',
        description: 'start again' }
    ]
  }

}
