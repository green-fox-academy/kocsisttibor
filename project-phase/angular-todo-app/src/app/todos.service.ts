import { Injectable } from '@angular/core';

@Injectable()
export class TodosService {

  constructor() { }

  getTodos() {
    return [
      { id: 0,
        todo: 'eat',
        deadline: '2017.12.01',
        description: 'go to the kitchen' }, 
      { id: 1,
        todo: 'sleep',
        deadline: '2017.12.02',
        description: 'go to bed' },
      { id: 2,
        todo: 'repeat',
        deadline: '2017.12.01',
        description: 'start again' }
    ]
  }

}
