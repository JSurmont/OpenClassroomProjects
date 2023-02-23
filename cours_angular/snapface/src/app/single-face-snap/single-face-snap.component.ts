import { FaceSnap } from './../models/face-snap.model';
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable, tap } from 'rxjs';
import { FaceSnapsService } from '../services/face-snaps.service';

@Component({
  selector: 'app-single-face-snap',
  templateUrl: './single-face-snap.component.html',
  styleUrls: ['./single-face-snap.component.scss']
})
export class SingleFaceSnapComponent {

  faceSnap$!: Observable<FaceSnap>;
  buttonText!: 'Oops, unSnap!' | 'Oh! Snap!';

  constructor(
    private faceSnapsService: FaceSnapsService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    this.buttonText = 'Oh! Snap!'

    const faceSnapId = +this.route.snapshot.params['id'];
    this.faceSnap$ = this.faceSnapsService.getFaceSnapById(faceSnapId);
  }

  onSnap(faceSnapId: number): void {
    if (this.buttonText === 'Oh! Snap!') {
      this.faceSnap$ = this.faceSnapsService.snapFaceSnapById(faceSnapId, 'snap').pipe(
        tap(() => this.buttonText = 'Oops, unSnap!')
      );
    } else {
      this.faceSnap$ = this.faceSnapsService.snapFaceSnapById(faceSnapId, 'unSnap').pipe(
        tap(() => this.buttonText = 'Oh! Snap!')
      );
    }
  }

}
