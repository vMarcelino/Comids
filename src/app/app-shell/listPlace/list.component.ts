import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css' , '../homePage/blank.materialize.min.css','../homePage/blank.materialize.css']
})
export class ListComponent implements OnInit {

  WarningMessageText = 'Request to get list items failed:';
  WarningMessageOpen = false;


  ngOnInit() {
  }

  handleWarningClose(open: boolean) {
    this.WarningMessageOpen = open;
    this.WarningMessageText = '';
  }
}
