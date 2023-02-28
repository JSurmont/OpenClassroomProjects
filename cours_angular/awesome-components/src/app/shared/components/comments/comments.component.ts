import { Comment } from 'src/app/core/models/comment.model';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormBuilder, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.scss']
})
export class CommentsComponent implements OnInit {

  @Input() comments!: Comment[];

  @Output() newCommentEvent = new EventEmitter<string>();

  commentCtrl!: FormControl;

  constructor(
    private formBuilder: FormBuilder
  ) {}

  ngOnInit(): void {
    this.commentCtrl = this.formBuilder.control('', [Validators.required, Validators.minLength(10)]);
  }

  onLeaveComment(): void {
    if (this.commentCtrl.invalid) {
      return;
    }

    this.newCommentEvent.emit(this.commentCtrl.value);

    this.commentCtrl.reset();
  }

}
