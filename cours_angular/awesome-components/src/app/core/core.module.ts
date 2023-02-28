import { RouterModule } from '@angular/router';
import { SharedModule } from './../shared/shared.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './components/header/header.component';



@NgModule({
  declarations: [
    HeaderComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    RouterModule
  ],
  exports: [
    HeaderComponent
  ]
})
export class CoreModule { }
