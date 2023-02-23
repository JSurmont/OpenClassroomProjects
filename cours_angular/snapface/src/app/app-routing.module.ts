import { NewFaceSnapComponent } from './new-face-snap/new-face-snap.component';
import { SingleFaceSnapComponent } from './single-face-snap/single-face-snap.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FaceSnapListComponent } from './face-snap-list/face-snap-list.component';

const routes: Routes = [
  { path: 'facesnaps/:id', component: SingleFaceSnapComponent},
  { path: 'facesnaps', component: FaceSnapListComponent },
  { path: '', component: LandingPageComponent},
  { path: 'create', component: NewFaceSnapComponent}
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {

}
