import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-questionaire-page',
  templateUrl: './questionaire.page.html',
  styleUrls: ['./questionaire.page.scss'],
})
export class QuestionairePage implements OnInit {

  slideOpts = {
    initialSlide: 0,
    speed: 400
  };

  questions: {question: string, options: string[]};
  constructor() { }

  ngOnInit() {}

}
