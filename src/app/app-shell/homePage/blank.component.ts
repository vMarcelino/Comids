import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
    selector: 'app-blank',
    templateUrl: './blank.component.html',
    styleUrls: ['./blank.component.css', './blank.materialize.min.css']
})
export class BlankComponent {
    @ViewChild('passwordinput', { static: false }) passwordInput: ElementRef
    @ViewChild('userinput', { static: false }) userInput: ElementRef
    constructor(private http: HttpClient, public router: Router) { }
    onLoginClicked(event: Event) {
        var ip = 'eisengarth.ddns.net'
        var ip = '127.0.0.1'
        var user = this.userInput.nativeElement.value
        var password = this.passwordInput.nativeElement.value
        var data = { 'user': user, 'password': password }
        console.log(user + ', ' + password)
        this.http.post('http://' + ip + ':2283/auth', data)
            .subscribe(
                data => {
                    console.log(data)
                    var token = data['token']
                    console.log(token)
                    window.localStorage.setItem('user_token', token)
                    this.router.navigate(['listPlace'])
                },
                error => {
                    alert('Erro: login incorreto')
                }
            )
    }
}
