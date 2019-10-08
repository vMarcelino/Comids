import { Component, ElementRef, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Component({
  selector: 'app-grid',
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css', '../homePage/blank.materialize.min.css', '../homePage/blank.materialize.css']
})
export class GridComponent {
  @ViewChild('passwordfield', { static: false }) passwordInput: ElementRef
  @ViewChild('userfield', { static: false }) userInput: ElementRef

  constructor(private http: HttpClient, public router: Router) { }

  onSignupClicked(event: Event) {
    var ip = 'eisengarth.ddns.net'
    var ip = '127.0.0.1'
    var user = this.userInput.nativeElement.value
    var password = this.passwordInput.nativeElement.value
    var data = { 'user': user, 'password': password }
    console.log(user + ', ' + password)
    this.http.post('http://' + ip + ':2283/signup', data)
      .subscribe(
        data => {
          console.log(data)
          this.router.navigate(['home'])
        },
        error => {
          console.log(error.status)
          switch (error.status) {
            case 406:
              alert('Senha muito curta. Minimo 8 caracteres')
              break
            case 409:
              alert('Usuário já em uso')
              break
            default:
              alert('Erro desconhecido')
          }
        }
      )

  }
}
