import { FaceSnap } from './../models/face-snap.model';
import { Injectable } from "@angular/core";

@Injectable({
  providedIn: 'root'
})
export class FaceSnapsService {

  getAllFaceSnaps(): FaceSnap[] {
    return this.faceSnaps;
  }

  getFaceSnapById(faceSnapId: number): FaceSnap {
    const faceSnap = this.faceSnaps.find(faceSnap => faceSnap.id === faceSnapId);

    if (faceSnap) {
      return faceSnap;
    } else {
      throw new Error('FaceSnap not found!');
    }
  }

  snapFaceSnapById(faceSnapId:number, snapType: 'snap' | 'unSnap'): void {
    (snapType == 'snap') ?
      this.getFaceSnapById(faceSnapId).snaps ++
      :
      this.getFaceSnapById(faceSnapId).snaps --;
  }


  faceSnaps: FaceSnap[] = [
    {
      id: 1,
      title: 'Archibalde',
      description:'Mon meilleur ami depuis tout petit !',
      createdDate: new Date(),
      snaps: 6,
      imageUrl: 'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg',
      location: 'Paris'
    },
    {
      id: 2,
      title: 'Three Rock Mountain',
      description:'Un endroit magnifique pour les randonnées.',
      createdDate: new Date(),
      snaps: 90,
      imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Three_Rock_Mountain_Southern_Tor.jpg/2880px-Three_Rock_Mountain_Southern_Tor.jpg',
      location: 'la montagne'
    },
    {
      id: 3,
      title: 'Un bon repas',
      description:'Mmmh que c\'est bon !',
      createdDate: new Date(),
      snaps: 50,
      imageUrl: 'https://wtop.com/wp-content/uploads/2020/06/HEALTHYFRESH.jpg',
    },
    {
      id: 4,
      title: 'Archibalde',
      description:'Mon meilleur ami depuis tout petit !',
      createdDate: new Date(),
      snaps: 150,
      imageUrl: 'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg',
      location: 'Paris'
    },
    {
      id: 5,
      title: 'Three Rock Mountain',
      description:'Un endroit magnifique pour les randonnées.',
      createdDate: new Date(),
      snaps: 250,
      imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Three_Rock_Mountain_Southern_Tor.jpg/2880px-Three_Rock_Mountain_Southern_Tor.jpg',
      location: 'la montagne'
    },
    {
      id: 6,
      title: 'Un bon repas',
      description:'Mmmh que c\'est bon !',
      createdDate: new Date(),
      snaps: 350,
      imageUrl: 'https://wtop.com/wp-content/uploads/2020/06/HEALTHYFRESH.jpg',
    }
  ];
}
