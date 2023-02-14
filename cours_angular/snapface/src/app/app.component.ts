import { FaceSnap } from './models/face-snap.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
  mySnap!: FaceSnap;

  ngOnInit(): void {
    this.mySnap = new FaceSnap(
      'Archibalde',
      'Mon meilleur ami depuis tout petit !',
      new Date(),
      6,
      'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg'
    );
  }
}
