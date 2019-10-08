import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-blank',
  templateUrl: './blank.component.html',
  styleUrls: ['./blank.component.css','./blank.materialize.min.css']
})
export class BlankComponent implements OnInit {

  constructor(private http: HttpClient) { }
  onLoginClicked(event: Event)
  {
    this.http.post('http://eisengarth.ddns.net:2283/auth',{'user':'teste','password':'123'} ).subscribe(data=>{console.log(data)})
  }
  ngOnInit() {
  }

}
