import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-grid',
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css' , '../homePage/blank.materialize.min.css','../homePage/blank.materialize.css']
})
export class GridComponent implements OnInit {

  GreyBox = require('../../../assets/GreyBox.svg') as string;
  WarningMessageText = 'Request to get grid text failed:';
  WarningMessageOpen = false;
  ngOnInit() {
    
  }
  handleWarningClose(open: boolean) {
    this.WarningMessageOpen = open;
    this.WarningMessageText = '';
  }
}
