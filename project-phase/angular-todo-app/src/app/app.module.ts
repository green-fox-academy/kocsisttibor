import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ClarityModule } from "clarity-angular";


import { AppComponent } from './app.component';
import { DetailsComponent } from './details/details.component';
import { TodosService } from './todos.service';


@NgModule({
  declarations: [
    AppComponent,
    DetailsComponent
  ],
  imports: [
    BrowserModule,
    ClarityModule.forRoot(),
    FormsModule
  ],
  providers: [
    TodosService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
