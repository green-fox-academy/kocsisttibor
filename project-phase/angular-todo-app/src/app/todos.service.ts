import { Injectable } from '@angular/core';

@Injectable()
export class TodosService {

  constructor() { }

  getTodos() {
    return ['eat', 'sleep', 'repeat']
  }

}
