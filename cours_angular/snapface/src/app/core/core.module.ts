import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { LOCALE_ID, NgModule } from '@angular/core';

import { HeaderComponent } from './components/header/header.component';
import { httpInterceptorProviders } from './interceptors';
import { HttpClientModule } from '@angular/common/http';



@NgModule({
  declarations: [
    HeaderComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    HttpClientModule
  ],
  exports: [
    HeaderComponent
  ],
  providers: [
    { provide: LOCALE_ID, useValue: 'fr-FR' },
    httpInterceptorProviders
  ]
})
export class CoreModule { }
